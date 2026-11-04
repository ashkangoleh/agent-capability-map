---
name: end-to-end-delivery-semantics
description: "Reason about at-most-once, at-least-once and exactly-once across source offsets, processor state and external sinks."
metadata:
  version: "1.0.0"
---

# end-to-end-delivery-semantics

## Activation boundary
Reason about at-most-once, at-least-once and exactly-once across source offsets, processor state and external sinks.

## Required context
Source ack/offset, checkpoint, transaction coordinator, sink commit protocol and idempotency key.

## Production procedure
1. Define event identity, key/partition strategy, ordering and source retention.
2. Separate event time, processing time, watermarks, windows, lateness and corrections.
3. Align offsets, checkpoints, state stores and sink commits; document the actual exactly-once boundary.
4. Bound state, retries, backpressure and DLQ growth; monitor lag and recovery.
5. Test late events, rebalance, worker loss, sink timeout and replay.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://kafka.apache.org/documentation/#semantics
- https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/fault_tolerance/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
