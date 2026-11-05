"""Conservative, offline Iceberg flat-schema evolution checks — no catalog access.

The tool intentionally refuses nested schema inputs and all live schema changes.
A valid result always requires manual compatibility review.
"""
import argparse
import json
import re
from pathlib import Path

DECIMAL = re.compile(r"^decimal\\(([1-9][0-9]*),([0-9]+)\\)$")


def as_fields(value, label, errors):
    if not isinstance(value, list):
        errors.append(f"{label} must be a flat field list")
        return {}
    fields = {}
    names = set()
    for item in value:
        if not isinstance(item, dict):
            errors.append(f"{label}: each field must be an object")
            continue
        fid = item.get("id")
        name = item.get("name")
        typ = item.get("type")
        req = item.get("required")
        if type(fid) is not int or fid <= 0:
            errors.append(f"{label}: field ID must be positive integer")
            continue
        if fid in fields:
            errors.append(f"{label}: duplicate field ID {fid}")
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
            errors.append(f"{label}: invalid simple field name for ID {fid}")
            continue
        if name in names:
            errors.append(f"{label}: duplicate field name {name}")
        if not isinstance(typ, str) or not re.fullmatch(r"[a-z][a-z0-9(),]*", typ):
            errors.append(f"{label}: invalid or nested/unsupported type for ID {fid}")
            continue
        if type(req) is not bool:
            errors.append(f"{label}: required must be boolean for {name}")
            continue
        fields[fid] = (name, typ, req)
        names.add(name)
    return fields


def supported_promotion(old, new):
    if old == new:
        return True
    if (old, new) in (("int", "long"), ("float", "double")):
        return True
    a, b = DECIMAL.fullmatch(old), DECIMAL.fullmatch(new)
    return bool(a and b and int(b[1]) > int(a[1]) and b[2] == a[2])


def inspect(plan):
    errors = []
    if not isinstance(plan, dict) or type(plan.get("schema_version")) is not int or plan.get("schema_version") != 1:
        return ["schema_version must be integer 1"]
    if type(plan.get("format_version")) is not int or plan["format_version"] not in (1, 2):
        errors.append("only v1/v2 primitive promotion preflight is supported")
    last = plan.get("last_assigned_field_id")
    if type(last) is not int or last < 0:
        errors.append("last_assigned_field_id must be a nonnegative integer from table metadata")
        last = 0
    before = as_fields(plan.get("before"), "before", errors)
    after = as_fields(plan.get("after"), "after", errors)
    if before and max(before) > last:
        errors.append("last_assigned_field_id is below existing field ID")
    raw_renames = plan.get("approved_renames", [])
    if not isinstance(raw_renames, list):
        errors.append("approved_renames must be a list")
        raw_renames = []
    authorized = set()
    for rename in raw_renames:
        if not isinstance(rename, dict) or type(rename.get("id")) is not int or not all(isinstance(rename.get(k), str) for k in ("from","to")):
            errors.append("invalid approved rename")
            continue
        authorized.add((rename["id"], rename["from"], rename["to"]))
    for fid, (name, typ, required) in after.items():
        if fid not in before:
            if fid <= last:
                errors.append(f"field ID {fid} was already assigned historically")
            if required:
                errors.append(f"new required field {name} needs separate, version-aware review")
            if name in {v[0] for v in before.values()}:
                errors.append(f"name {name} reintroduced with a different field ID")
            continue
        old_name, old_type, old_required = before[fid]
        if old_name != name and (fid, old_name, name) not in authorized:
            errors.append(f"field ID {fid} rename not authorized: {old_name} -> {name}")
        if not supported_promotion(old_type, typ):
            errors.append(f"unsupported type change at field ID {fid}: {old_type} -> {typ}")
        if not old_required and required:
            errors.append(f"field ID {fid} became required without backfill proof")
    return errors


def reject_duplicate_keys(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.plan.stat().st_size > 65536:
            raise ValueError("oversized input")
        plan = json.loads(args.plan.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys,
                          parse_constant=lambda x: (_ for _ in ()).throw(ValueError("non-finite number")))
        issues = inspect(plan)
    except (OSError, UnicodeError, ValueError) as exc:
        issues = [str(exc)]
    print(json.dumps({"status": "rejected" if issues else "manual_review_required",
                      "can_execute": False, "issues": issues}, indent=2))
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
