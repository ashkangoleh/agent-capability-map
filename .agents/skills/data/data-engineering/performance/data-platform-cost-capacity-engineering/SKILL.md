---
name: data-platform-cost-capacity-engineering
description: "Plan data platform capacity and FinOps across compute, storage, network, metadata, ingestion and query concurrency."
metadata:
  version: "1.0.1"
---

# data-platform-cost-capacity-engineering

## Activation boundary
Plan data platform capacity and FinOps across compute, storage, network, metadata, ingestion and query concurrency.

## Required context
Volumes, peak concurrency, query profiles, storage growth, pricing, egress, SLO and forecast horizon.

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
- https://www.finops.org/framework/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
