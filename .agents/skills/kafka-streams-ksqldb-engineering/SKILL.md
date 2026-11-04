---
name: kafka-streams-ksqldb-engineering
description: "Build Kafka Streams and ksqlDB applications with partition-aware joins, state stores and changelog topics."
metadata:
  version: "1.0.0"
---

# kafka-streams-ksqldb-engineering

## Activation boundary
Build Kafka Streams and ksqlDB applications with partition-aware joins, state stores and changelog topics.

## Required context
Kafka/client versions, keys, partitions, join windows, state-store backend and latency.

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
- https://kafka.apache.org/documentation/streams/
- https://docs.ksqldb.io/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
