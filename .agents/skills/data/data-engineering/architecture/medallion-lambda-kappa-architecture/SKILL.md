---
name: medallion-lambda-kappa-architecture
description: "Choose medallion, Lambda or Kappa architectures from latency, replayability and operational complexity."
metadata:
  version: "1.0.1"
---

# medallion-lambda-kappa-architecture

## Activation boundary
Choose medallion, Lambda or Kappa architectures from latency, replayability and operational complexity.

## Required context
Freshness target, raw retention, batch/stream sources, serving latency and replay horizon.

## Production procedure
1. Start from use cases, workload SLOs, ownership, classification and operating model.
2. Assign clear responsibility to ingestion, compute, table format, catalog, orchestration and serving.
3. Define interoperability contracts, transaction boundaries, replay/backfill and schema evolution.
4. Compare cost, team skills, failure domains, lock-in, observability and migration.
5. Validate with failure scenarios, recovery exercises and measurable acceptance criteria.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://docs.databricks.com/aws/en/lakehouse/medallion

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For production-impacting recommendations or incident handling, load [acceptance and recovery protocol](references/acceptance-and-recovery.md) only after this skill is selected. It defines a domain-specific fault-injection oracle, evidence ledger and safe recovery conditions. Do not imply the tests were executed or that this reference grants tool permissions.
