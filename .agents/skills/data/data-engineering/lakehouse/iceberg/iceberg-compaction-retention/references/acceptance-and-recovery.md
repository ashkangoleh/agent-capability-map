# iceberg-compaction-retention — independent acceptance and recovery

## Capability and observed inputs
Iceberg snapshot, field-ID and partition evolution. Required context from the existing specialist: Use for Iceberg small files, manifest planning overhead, historical snapshot retention and orphan-file investigation. For schema/partition evolution use `iceberg-table-schema-partition-evolution`; for REST-catalog availability or authentication use the catalog specialist. Do not treat unmanaged Parquet folders as Iceberg tables.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Concurrently rewrite files and expire snapshots while readers pin older refs. | Protected refs, field-ID compatibility and visible rows remain valid. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Restore retained snapshot only when data files still exist; otherwise fail closed. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
1. Run only read-only inspection first: see [inspection and guarded SQL examples](examples/spark_maintenance.sql). Snapshot IDs, refs, current file counts and distribution must be observed from a real catalog, not invented. 2. Choose **one** operation using [operation contracts](references/operations.md). File compaction, manifest rewrite, snapshot expiration and orphan deletion solve different problems and have different reversibility. 3. For any proposed operation, prepare the JSON [offline plan](examples/preflight_plan.json). When **Python 3.10+ is available**, optionally run `python scripts/check_plan.py --plan examples/preflight_plan.jso

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://iceberg.apache.org/docs/latest/maintenance/
- https://iceberg.apache.org/docs/latest/spark-procedures/
- https://iceberg.apache.org/docs/latest/spark-queries/
- https://iceberg.apache.org/spec/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
