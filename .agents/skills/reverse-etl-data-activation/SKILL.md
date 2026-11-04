---
name: reverse-etl-data-activation
description: "Design reverse ETL to synchronize governed warehouse data into CRM, marketing and product systems."
metadata:
  version: "1.0.0"
---

# reverse-etl-data-activation

## Activation boundary
Design reverse ETL to synchronize governed warehouse data into CRM, marketing and product systems.

## Required context
Warehouse model, target API, sync frequency, identity keys, rate limits, deletion policy and PII scope.

## Production procedure
1. Define consumer contract, grain, stable IDs, freshness, latency and access requirements.
2. Choose API, materialized read model, reverse ETL or Arrow transport from concurrency and data size.
3. Enforce authorization and tenant-aware caching; set query budgets and response limits.
4. Handle rate limits, partial writes, retries, deletion and schema evolution.
5. Test cache leakage, auth bypass, target outage, timeout and staleness.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://hightouch.com/docs
- https://www.getcensus.com/docs

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
