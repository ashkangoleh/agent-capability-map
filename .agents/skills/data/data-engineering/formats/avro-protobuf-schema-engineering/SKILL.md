---
name: avro-protobuf-schema-engineering
description: "Design Avro and Protobuf schemas for durable serialization, compatibility, field identity and replay."
metadata:
  version: "1.0.0"
---

# avro-protobuf-schema-engineering

## Activation boundary
Design Avro and Protobuf schemas for durable serialization, compatibility, field identity and replay.

## Required context
Format, registry, producer/consumer languages, field IDs, defaults and retention.

## Production procedure
1. Verify reader/writer support and logical-type mappings for every engine and deployed release.
2. Tune row groups, stripes, encoding and compression from representative scan patterns.
3. Preserve decimals, timestamps, nested structures and schema evolution rules.
4. Inspect statistics and pruning effectiveness.
5. Test cross-engine reads, historical files, null/nested values and corrupt objects.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://avro.apache.org/docs/
- https://protobuf.dev/programming-guides/proto3/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
