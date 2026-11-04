---
name: distributed-query-engine-performance
description: "Tune Trino, Presto and Dremio with plans, pushdown, join distribution, memory, spill and source concurrency."
metadata:
  version: "1.0.0"
---

# distributed-query-engine-performance

## Activation boundary
Tune Trino, Presto and Dremio with plans, pushdown, join distribution, memory, spill and source concurrency.

## Required context
Engine release, plan, connectors, statistics, topology, concurrency, memory and workload.

## Production procedure
1. Capture plan and runtime telemetry before topology or configuration changes.
2. Separate CPU, memory, disk, network, metadata, shuffle, spill and source bottlenecks.
3. Use statistics, pruning, layout, join strategy and compaction only when measured.
4. Model peak concurrency, backfill bursts, recovery headroom and unit cost.
5. Re-run representative workloads and compare correctness, latency, resource use and cost.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://trino.io/docs/current/optimizer/cost-based-optimizations.html
- https://prestodb.io/docs/current/optimizer.html

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
