---
name: dremio-presto-query-federation
description: "Design Dremio and Presto/Trino federation with pushdown, source limits, identity and consistency boundaries."
metadata:
  version: "1.0.0"
---

# dremio-presto-query-federation

## Activation boundary
Design Dremio and Presto/Trino federation with pushdown, source limits, identity and consistency boundaries.

## Required context
Engine release, connector catalog, sources, pushdown, join sizes, network and credentials.

## Production procedure
1. Inspect EXPLAIN/runtime profiles for scan, exchange, join, aggregation, skew and pushdown.
2. Choose partitioning, clustering, sort/distribution and indexes using real predicates.
3. Set workload isolation, concurrency, memory/spill, quotas and cost attribution.
4. Verify type, timezone, transaction, MERGE and delete semantics by release.
5. Test source outage, queue saturation, large joins, partial loads and recovery.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://docs.dremio.com/
- https://prestodb.io/docs/current/
- https://trino.io/docs/current/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
