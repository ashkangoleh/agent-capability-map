# end-to-end-delivery-semantics — independent acceptance and recovery

## Capability and observed inputs
Event-time, offsets and sink delivery contracts. Required context from the existing specialist: Source offset/ack model; processor checkpoint/state; sink transaction; idempotency key; retry; ordering scope; replay horizon; external side effects.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Inject late events, duplicate retries and restart with divergent state. | Event-time windows and output effects follow explicitly proven guarantee. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Rewind replayable source and perform idempotent/transactional sink recovery. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Crash after sink write before source ack causes duplicates unless sink is idempotent or transactionally coupled. - Ack before durable sink commit can lose data; move ack after commit or use a supported transaction. - Checkpoint restore after source retention expires may be impossible; retain external snapshots. - External HTTP side effects need outbox/idempotency; processor exactly-once does not cover arbitrary APIs. - DLQ replay can reorder data; preserve source identity/version and correction semantics.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://kafka.apache.org/documentation/#semantics
- https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/state/checkpoints/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
