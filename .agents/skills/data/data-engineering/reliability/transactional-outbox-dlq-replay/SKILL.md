---
name: transactional-outbox-dlq-replay
description: "Implement transactional outbox, dead-letter queues and poison-message recovery for event-driven integration."
metadata:
  version: "1.0.0"
---

# transactional-outbox-dlq-replay

## Activation boundary
Implement transactional outbox, dead-letter queues and poison-message recovery for event-driven integration.

## Required context
Application DB transaction, outbox schema, CDC relay, event key, broker retention and consumer idempotency.

## Production procedure
1. Define a durable unit of work and stable event key before retries or checkpoints.
2. Choose append/merge/replace/transactional publication from sink guarantees.
3. Persist source progress only after target commit or recoverable manifest handoff.
4. Bound retry budgets and provide controlled replay, DLQ redrive, reconciliation and RPO/RTO.
5. Test crashes before/after commit, duplicate delivery, stale checkpoints and restore.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html
- https://microservices.io/patterns/data/transactional-outbox.html

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
