---
name: data-engineering-implementation
description: Use when designing, implementing, debugging, or reviewing data pipelines, batch or streaming jobs, SQL transformations, data models, warehouses, lakehouses, and data quality workflows.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Purpose

Build data systems whose correctness, replayability, operational behavior, and cost can be reasoned about from explicit contracts.

## Inputs and prerequisites

Establish source and sink, engine and versions, data volume, throughput, latency/SLO, retention, security, governance, deployment model, and acceptable recovery objectives. Mark unknowns rather than inventing them.

## Procedure

1. Inspect schemas, sample data, existing SQL/code, engine versions, orchestration, and sink semantics.
2. Define grain, keys, event time, timezone, null behavior, deduplication rules, and late-arrival policy.
3. Define delivery semantics honestly. Exactly-once is an end-to-end property, not a label for one component.
4. Design idempotency, retries, timeouts, backoff, checkpointing, replay, backfill, and recovery.
5. Analyze partitioning, skew, hot keys, shuffle, memory, spill, file sizing, compaction, and metadata growth where relevant.
6. Handle schema evolution and drift with explicit compatibility rules.
7. Define data quality checks, reconciliation, lineage, freshness, and observability.
8. Estimate cost from measured or stated assumptions; do not invent benchmarks.
9. Implement the smallest valid architecture. Avoid introducing engines or catalogs without a demonstrated requirement.
10. Validate row counts, key uniqueness, nulls, aggregates, time windows, duplicate behavior, and source-to-sink reconciliation.
11. Provide deployment, backfill, rollback, and incident recovery steps.

## Evidence requirements

Use actual schemas, query plans, execution logs, data samples, source/sink documentation, and version-specific engine references. Separate observed performance from estimates.

## Output contract

Include data flow, assumptions, contracts, implementation, failure modes, validation queries or tests, operational metrics, and recovery plan.

## Failure modes and abstention

Do not recommend a production design without understanding source/sink consistency and recovery requirements. Do not claim zero data loss, exactly-once, or performance gains without evidence.

## Validation checklist

- [ ] Grain and keys are explicit.
- [ ] Idempotency and duplicate handling are defined.
- [ ] Replay, backfill, late data, and schema evolution are covered.
- [ ] Data quality and reconciliation are measurable.
- [ ] Performance and cost assumptions are labeled.
- [ ] Failure and recovery paths are documented.
