# kafka-consumer-rebalance-replay — independent acceptance and recovery

## Capability and observed inputs
Kafka offset, transaction and rebalance semantics. Required context from the existing specialist: Kafka/broker/client versions, group.id, partition/key distribution, retention, offset commit strategy, sink contract, throughput and allowed replay.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Rebalance after sink write but before offset commit; replay a poisoned event. | Sink deduplication and source offset recovery reconcile with input partition order. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Pause, recover offsets and replay from retained log with idempotent sink writes. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Verify identical sink state after reprocessing a sample offset range. - Monitor consumer lag distribution, commit failures, retry rate and duplicate suppression. - Do not assert a test, benchmark, compatibility or rollout succeeded without actual tool evidence.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://kafka.apache.org/documentation/
- https://kafka.apache.org/40/design/design/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
