"""Read-only, dependency-free static preflight for an Iceberg maintenance plan.

This intentionally cannot connect to Spark, a catalog, object storage, or a shell.
A successful static plan result never authorizes a table operation.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

TABLE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*\\.[A-Za-z_][A-Za-z0-9_]*\\.[A-Za-z_][A-Za-z0-9_]*$")
OPERATIONS = {"rewrite_data_files", "rewrite_manifests", "expire_snapshots", "remove_orphan_files"}
MAX_BYTES = 65536


def _integer(value, minimum=0):
    return type(value) is int and value >= minimum


def _dict(value):
    return value if type(value) is dict else {}


def validate_plan(plan):
    errors = []
    if type(plan) is not dict:
        return ["Plan must be a JSON object"]
    if plan.get("schema_version") != 1 or type(plan.get("schema_version")) is not int:
        errors.append("schema_version must be integer 1")
    operation = plan.get("operation")
    if operation not in OPERATIONS:
        errors.append("operation is not recognized")
        return errors
    table = plan.get("table")
    if type(table) is not str or not TABLE.fullmatch(table):
        errors.append("table must be a simple, qualified catalog.namespace.table name")
    for key in ("spark_version", "iceberg_version"):
        if type(plan.get(key)) is not str or not plan[key].strip():
            errors.append(f"{key} is required as version evidence")
    if plan.get("environment") not in ("staging", "production"):
        errors.append("environment must be staging or production")
    if plan.get("environment") == "production":
        ticket = plan.get("change_ticket")
        if type(ticket) is not str or not ticket.strip():
            errors.append("production plan requires a change_ticket")
    if plan.get("catalog_commit_contract_reviewed") is not True:
        errors.append("catalog_commit_contract_reviewed must be true")
    if not _integer(plan.get("baseline_snapshot_id"), 1):
        errors.append("baseline_snapshot_id must be a positive integer")

    concurrency = _dict(plan.get("concurrency"))
    writers = concurrency.get("writers_active")
    if type(writers) is not bool:
        errors.append("concurrency.writers_active must be boolean")
    if concurrency.get("policy") not in ("pause_writers", "validate_and_retry"):
        errors.append("concurrency.policy must be pause_writers or validate_and_retry")
    if not _integer(concurrency.get("longest_inflight_write_hours")):
        errors.append("concurrency.longest_inflight_write_hours must be a nonnegative integer")
    if writers is True and concurrency.get("policy") == "pause_writers":
        errors.append("writers are active but concurrency policy claims they are paused")

    retention = _dict(plan.get("retention"))
    for field in ("time_travel_days", "rollback_days", "consumer_lag_days", "planned_retention_days"):
        if not _integer(retention.get(field)):
            errors.append(f"retention.{field} must be a nonnegative integer")
    days = [retention.get(f) for f in ("time_travel_days", "rollback_days", "consumer_lag_days")]
    if all(_integer(d) for d in days) and _integer(retention.get("planned_retention_days")):
        if retention["planned_retention_days"] < max(days):
            errors.append("planned_retention_days violates declared consumer/rollback/time-travel floor")
    if type(retention.get("legal_hold")) is not bool:
        errors.append("retention.legal_hold must be boolean")
    if type(retention.get("protected_refs_reviewed")) is not bool:
        errors.append("retention.protected_refs_reviewed must be boolean")

    params = _dict(plan.get("parameters"))
    if operation == "rewrite_data_files":
        if params.get("partition_scoped") is not True:
            errors.append("rewrite_data_files requires a reviewed, partition-scoped canary")
        if not _integer(params.get("estimated_candidate_files"), 2):
            errors.append("rewrite_data_files requires at least two measured candidate files")
    elif operation == "rewrite_manifests":
        if not _integer(params.get("spec_id")):
            errors.append("rewrite_manifests requires reviewed nonnegative spec_id")
        if params.get("planning_baseline_reviewed") is not True:
            errors.append("rewrite_manifests requires a query-planning baseline")
    elif operation == "expire_snapshots":
        if retention.get("legal_hold") is True:
            errors.append("legal hold blocks expiration")
        if retention.get("protected_refs_reviewed") is not True:
            errors.append("review all protected branch/tag refs before expiration")
        if not _integer(params.get("retain_last"), 1):
            errors.append("expire_snapshots retain_last must be at least one")
        cutoff = params.get("older_than_utc")
        if type(cutoff) is not str:
            errors.append("expire_snapshots requires timezone-aware older_than_utc")
        else:
            try:
                parsed = datetime.fromisoformat(cutoff.replace("Z", "+00:00"))
                if parsed.tzinfo is None or parsed.utcoffset() is None:
                    raise ValueError("no timezone")
                age_days = (datetime.now(timezone.utc) - parsed).total_seconds() / 86400
                floor = retention.get("planned_retention_days")
                if _integer(floor) and age_days < floor:
                    errors.append("older_than_utc is newer than the declared retention floor")
            except ValueError:
                errors.append("older_than_utc must be an ISO 8601 timezone-aware timestamp")
    elif operation == "remove_orphan_files":
        if retention.get("legal_hold") is True:
            errors.append("legal hold blocks orphan deletion")
        if params.get("dry_run") is not True:
            errors.append("remove_orphan_files must start with dry_run=true")
        if params.get("path_equivalence_reviewed") is not True:
            errors.append("orphan cleanup requires verified filesystem/metadata path equivalence")
        older = params.get("older_than_hours")
        buffer = params.get("safety_margin_hours")
        duration = concurrency.get("longest_inflight_write_hours")
        if not _integer(older, 1) or not _integer(buffer, 1):
            errors.append("older_than_hours and safety_margin_hours must be positive integers")
        elif _integer(duration) and older <= duration + buffer:
            errors.append("orphan age must exceed maximum in-flight writer duration plus margin")
    return errors


def _unique_keys(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError(f"duplicate JSON key: {key}")
        obj[key] = value
    return obj


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        if args.plan.stat().st_size > MAX_BYTES:
            raise ValueError("plan exceeds 64 KiB")
        plan = json.loads(
            args.plan.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_keys,
            parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"non-finite JSON number {value}")),
        )
        errors = validate_plan(plan)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        errors = [f"invalid plan: {exc}"]
    report = {
        "status": "rejected" if errors else "manual_review_required",
        "can_execute": False,
        "checks": "offline_static_checks_only",
        "errors": errors,
    }
    print(json.dumps(report, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
