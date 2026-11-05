---
name: data-engineering-foundations-lifecycle
description: "Design an end-to-end data engineering lifecycle from acquisition to governed, reliable data products."
metadata:
  version: "1.0.1"
---

# data-engineering-foundations-lifecycle

## Activation boundary
Design an end-to-end data engineering lifecycle from acquisition to governed, reliable data products.

## Required context
Owners, producers/consumers, volume, freshness SLOs, classification, budget, RPO/RTO.

## Production procedure
1. Declare business grain, keys, ownership and event-time semantics before selecting tools.
2. Choose modeling/runtime patterns from audit, history, scale and consumer query requirements.
3. Define canonical types, timezone/decimal rules and schema contracts.
4. Specify corrections, late data, historical reconstruction and migration behavior.
5. Validate grain, uniqueness, referential integrity and reproducibility.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://www.databricks.com/product/data-lakehouse
- https://martinfowler.com/articles/data-monolith-to-mesh.html

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
