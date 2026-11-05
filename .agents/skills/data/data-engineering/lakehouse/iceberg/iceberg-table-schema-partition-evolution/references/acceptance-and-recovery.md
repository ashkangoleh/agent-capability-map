# iceberg-table-schema-partition-evolution — independent acceptance and recovery

## Capability and observed inputs
Iceberg snapshot, field-ID and partition evolution. Required context from the existing specialist: Iceberg format version and runtime, catalog implementation, storage, schema/field IDs, partition transforms, snapshot retention, concurrent writers and consumer compatibility.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Concurrently rewrite files and expire snapshots while readers pin older refs. | Protected refs, field-ID compatibility and visible rows remain valid. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Restore retained snapshot only when data files still exist; otherwise fail closed. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Validate snapshot IDs, field IDs, partition transforms and reader compatibility on a cloned table. - Document availability SLO, metadata rollback path, schema-change owner and production acceptance. - Include edge cases, timeouts and partial failures where material; do not claim tests executed without tool traces.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://iceberg.apache.org/docs/latest/evolution/
- https://iceberg.apache.org/docs/latest/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
