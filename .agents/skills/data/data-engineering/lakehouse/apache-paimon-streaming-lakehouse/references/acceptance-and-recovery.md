# apache-paimon-streaming-lakehouse — independent acceptance and recovery

## Capability and observed inputs
Table-format and object-store commit contracts. Required context from the existing specialist: Paimon version; Flink/Spark versions; append-only or primary-key table; bucket/partition keys; merge engine; changelog; snapshots; catalog/storage.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Fail object upload or metadata commit during simultaneous writers. | Reader-visible snapshot atomicity and delete semantics are proven for installed engine versions. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Quarantine uncommitted files; restore last readable catalog head. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Compaction backlog: inspect write rate, bucket skew and compaction resources. - Changelog gaps: verify producer mode and sequence semantics before replay. - Primary-key conflicts: define deterministic ordering and merge behavior. - Snapshot growth: expire only after recovery windows are considered. - Connector mismatch: pin compatible engine and Paimon versions.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://paimon.apache.org/docs/
- https://github.com/apache/paimon

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
