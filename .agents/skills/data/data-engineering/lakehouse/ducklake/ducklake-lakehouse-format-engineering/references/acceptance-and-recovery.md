# ducklake-lakehouse-format-engineering — independent acceptance and recovery

## Capability and observed inputs
Table-format and object-store commit contracts. Required context from the existing specialist: DuckLake/DuckDB versions; catalog backend; object store; writer concurrency; partitioning; snapshot retention; client matrix.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Fail object upload or metadata commit during simultaneous writers. | Reader-visible snapshot atomicity and delete semantics are proven for installed engine versions. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Quarantine uncommitted files; restore last readable catalog head. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Catalog loss: restore a consistent backup and verify referenced files. - Orphan files: never use blind prefix deletion. - Concurrent conflict: serialize or use documented coordination. - Extension mismatch: pin compatible versions and stop mixed writers.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://ducklake.select/docs/stable/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
