---
name: iceberg-compaction-retention
description: Plan safe Apache Iceberg file compaction, manifest rewrites, snapshot expiration and orphan cleanup using catalog-aware preflight, targeted procedures and recovery evidence.
metadata:
  version: "1.1.1"
---

# Iceberg compaction and retention

## Activation boundary
Use for Iceberg small files, manifest planning overhead, historical snapshot retention and orphan-file investigation. For schema/partition evolution use `iceberg-table-schema-partition-evolution`; for REST-catalog availability or authentication use the catalog specialist. Do not treat unmanaged Parquet folders as Iceberg tables.

## Evidence and prerequisites
Before proposing changes, determine the deployed **Spark, Iceberg and catalog** versions; table name/location and format version; current snapshot and refs; file-size/partition distribution; live writers and maximum write duration; time-travel, CDC/consumer, legal hold and RPO/RTO requirements; maintenance budget; data-file/delete-file semantics; and rollback constraints. Unknown inputs are a stop for irreversible operations, not permission to assume defaults.

## Production procedure
1. Run only read-only inspection first: see [inspection and guarded SQL examples](examples/spark_maintenance.sql). Snapshot IDs, refs, current file counts and distribution must be observed from a real catalog, not invented.
2. Choose **one** operation using [operation contracts](references/operations.md). File compaction, manifest rewrite, snapshot expiration and orphan deletion solve different problems and have different reversibility.
3. For any proposed operation, prepare the JSON [offline plan](examples/preflight_plan.json). When **Python 3.10+ is available**, optionally run `python scripts/check_plan.py --plan examples/preflight_plan.json` from this skill directory. Without Python, perform the same checklist in [operation contracts](references/operations.md) manually; the standalone router does **not** require Python and does not automatically execute bundled scripts. The tool checks static guardrails only, never contacts Spark or deletes data, and always returns `manual_review_required` on success.
4. Record the observed baseline snapshot ID, active branches/tags, writer/checkpoint behavior and planned writer-conflict policy. For rewrite jobs, select a bounded partition/filter canary; test concurrent-commit behavior in staging before larger scope. Partial-progress options and retries are version-specific.
5. **Do not execute** `expire_snapshots` or destructive `remove_orphan_files` without a reviewed retention floor, reference inventory, minimum in-flight-writer age, explicit authorization and restore evidence. Start orphan analysis with `dry_run => true`; never infer a safe age solely from the procedure default. See [failure and recovery runbook](references/failure-recovery.md).
6. Execute only after a human-reviewed change plan and version-pinned procedure syntax. Query the resulting snapshot, live file listings, delete-file counts, representative row/business invariants and read behavior. Validate streaming readers and catalog caches separately.
7. Compare recorded before/after file-count distribution, query-planning latency, table scan latency, object-store cost and runtime. Distinguish metadata-only rewrites from data-file rewrites; report partial commits and non-recoverable retention changes honestly.

## Approval and failure gates
- Protect tags/branches, active readers, legal holds and consumer replay windows. Do not confuse Iceberg snapshot isolation with an object-store rename or universal exactly-once guarantee.
- A concurrent writer or commit timeout requires inspecting the **actual current** catalog snapshot before any retry; never replay a non-idempotent cleanup as if it were harmless.
- Do not recommend a snapshot rollback once the required files are expired. After actual file deletion, rollback may be impossible.
- Orphan cleanup must account for uncommitted writers and path scheme/authority mismatches. Unknown path equivalence is a denial, not an opportunity to force deletion.
- The bundled script has no authorization capability. Any `manual_review_required` result is **not** approval to run SQL against production.

## Output contract
Return the exact operation and its purpose, observed vs missing evidence, affected table/partitions, pinned versions, reviewed safety budget, **read-only** diagnostic SQL, a separately marked gated mutation plan, expected business invariants, fault/rollback or restoration procedure, and PASS/FAIL/UNKNOWN for each observed validation. Do not fabricate an execution trace.

## Official references
- Apache Iceberg maintenance: https://iceberg.apache.org/docs/latest/maintenance/
- Apache Iceberg Spark procedures: https://iceberg.apache.org/docs/latest/spark-procedures/
- Apache Iceberg Spark metadata queries: https://iceberg.apache.org/docs/latest/spark-queries/
- Apache Iceberg specification (optimistic concurrency): https://iceberg.apache.org/spec/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
