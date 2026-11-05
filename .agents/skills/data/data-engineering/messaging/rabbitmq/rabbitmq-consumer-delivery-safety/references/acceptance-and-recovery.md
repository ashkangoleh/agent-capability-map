# rabbitmq-consumer-delivery-safety — independent acceptance and recovery

## Capability and observed inputs
Broker ack, ordering and consumer replay. Required context from the existing specialist: RabbitMQ broker/client version, queue/exchange topology, routing keys, durability, ack mode, prefetch, DLX and business idempotency.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Fail consumer after ack and change partition assignments during backlog. | No silently lost/duplicated business effects beyond declared delivery model. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Recover from durable broker position and bounded DLQ redrive. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Run duplicate/requeue resilience tests and compare sink state. - Monitor unacked messages, consumer utilization and DLX backlog. - Disclose unverified guarantees, tests not executed, missing evidence and any unresolved recovery risk.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://www.rabbitmq.com/docs/confirms
- https://www.rabbitmq.com/docs/quorum-queues

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
