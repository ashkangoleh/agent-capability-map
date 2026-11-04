---
name: apache-paimon-streaming-lakehouse
description: "Design Apache Paimon tables with LSM storage, changelog production, Flink/Spark integration and compaction."
metadata:
  version: "1.0.0"
---

# apache-paimon-streaming-lakehouse

## Activation boundary
Design Apache Paimon tables with LSM storage, changelog production, Flink/Spark integration and compaction.

## Required context
Paimon release, Flink/Spark versions, table mode, keys, buckets, compaction and catalog.

## Production procedure
1. Verify format/catalog/engine compatibility for deployed versions and required features.
2. Define authoritative writer, commit protocol, schema/partition evolution and conflict handling.
3. Plan snapshots, manifests, compaction, vacuum and orphan cleanup with retention.
4. Validate identity, credential vending and direct object access separately from catalog policy.
5. Test concurrent commits, metadata outage, maintenance interruption and restore.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://paimon.apache.org/docs/1.4/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
