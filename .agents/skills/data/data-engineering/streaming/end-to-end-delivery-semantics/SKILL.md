---
name: end-to-end-delivery-semantics
description: "Reason about at-most-once, at-least-once and exactly-once across source offsets, processor state, transactions and external sinks."
license: Proprietary
metadata:
  version: "1.1.1"
---

# end-to-end-delivery-semantics

## Activation boundary
Use when a pipeline claims delivery guarantees or must recover without loss/duplication. Never label a pipeline exactly-once based only on a broker, checkpoint or connector setting.

## Required context
Source offset/ack model; processor checkpoint/state; sink transaction; idempotency key; retry; ordering scope; replay horizon; external side effects.

## Production procedure
1. Draw the commit chain: source read/ack, processor state, output write, sink commit and source offset advancement.
2. Identify the atomic boundary. If source offset and sink commit cannot be coordinated, require idempotent writes or deduplication.
3. Define stable event identity and version, including source partition/offset or business key plus sequence where valid.
4. For Kafka distinguish producer idempotence, transactions and consumer offset commits; for Flink inspect checkpoint mode and sink two-phase commit support.
5. For warehouses/object stores validate transaction or manifest commit semantics; processor checkpoints do not make every sink atomic.
6. Define DLQ/replay behavior and ordering guarantees by partition/key; document cross-partition operations.

## Failure modes and recovery
- Crash after sink write before source ack causes duplicates unless sink is idempotent or transactionally coupled.
- Ack before durable sink commit can lose data; move ack after commit or use a supported transaction.
- Checkpoint restore after source retention expires may be impossible; retain external snapshots.
- External HTTP side effects need outbox/idempotency; processor exactly-once does not cover arbitrary APIs.
- DLQ replay can reorder data; preserve source identity/version and correction semantics.

## Validation and acceptance
- Inject crashes at each commit boundary.
- Test duplicates, timeout retries, sink partial failure, checkpoint restore and replay.
- Verify ordering scope and deduplication horizon.
- Produce a guarantee matrix for source, processor, sink and external side effects.

## Output contract
Return commit-boundary diagram, guarantee matrix, idempotency design, fault-injection results and qualified delivery claim.

## Official or primary references
- https://kafka.apache.org/documentation/#semantics
- https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/state/checkpoints/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
