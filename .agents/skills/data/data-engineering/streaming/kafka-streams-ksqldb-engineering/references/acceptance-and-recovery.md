# kafka-streams-ksqldb-engineering — independent acceptance and recovery

## Capability and observed inputs
Event-time, offsets and sink delivery contracts. Required context from the existing specialist: Kafka/client versions; topic keys/partitions; topology; state-store size; processing guarantee; changelog retention; standby replicas; deployment model.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Inject late events, duplicate retries and restart with divergent state. | Event-time windows and output effects follow explicitly proven guarantee. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Rewind replayable source and perform idempotent/transactional sink recovery. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Join partition mismatch: repartition upstream with a stable key and validate serialization. - Rebalance loop: inspect poll interval, processing time, task migration and deployment churn. - Slow state restore: review changelog retention, standby replicas and local disk. - Reset duplicates: require idempotent sinks or reconcile output topics. - Schema evolution break: validate key and value compatibility.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://kafka.apache.org/documentation/streams/
- https://docs.ksqldb.io/en/latest/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
