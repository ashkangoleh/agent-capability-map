# flink-checkpoint-savepoint-recovery — independent acceptance and recovery

## Capability and observed inputs
Checkpoint/recovery and operator state. Required context from the existing specialist: Flink version, deployment mode, job graph/operator UIDs, source and sink guarantees, checkpoint store and retention, state size, restore point, RPO/RTO and update target.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Corrupt checkpoint or restore with changed operator UID/parallelism. | Source replay and sink effects reconcile; state schema migration is explicitly validated. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Restore compatible savepoint and prevent dual writers. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Validate restored event counts and deduplication against source offsets and output keys. - Capture checkpoint duration, failure counters, backpressure and state-size metrics before and after change. - Do not assert a test, benchmark, compatibility or rollout succeeded without actual tool evidence.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/fault-tolerance/checkpointing/
- https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/upgrading/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
