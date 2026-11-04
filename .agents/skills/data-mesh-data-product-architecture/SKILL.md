---
name: data-mesh-data-product-architecture
description: "Design Data Mesh domains and data products with federated governance and explicit producer-consumer contracts."
metadata:
  version: "1.0.0"
---

# data-mesh-data-product-architecture

## Activation boundary
Design Data Mesh domains and data products with federated governance and explicit producer-consumer contracts.

## Required context
Business domains, product owners, consumers, platform capabilities, contracts and SLOs.

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
- https://martinfowler.com/articles/data-monolith-to-mesh.html

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
