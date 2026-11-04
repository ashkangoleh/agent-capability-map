---
name: data-schema-migration-release-management
description: "Plan schema migrations with expand-contract rollout, compatibility windows, backfills and rollback limits."
metadata:
  version: "1.0.0"
---

# data-schema-migration-release-management

## Activation boundary
Plan schema migrations with expand-contract rollout, compatibility windows, backfills and rollback limits.

## Required context
Schema versions, producers/consumers, engine, compatibility, deployment order, volume and rollback constraints.

## Production procedure
1. Separate unit, contract, integration, end-to-end, replay and performance tests.
2. Pin runtimes, native dependencies, containers and fixtures; keep secrets outside source.
3. Review migration plans, compatibility windows and rollback limits.
4. Gate releases on reproducible checks, provenance and owner approval.
5. Test partial deployment, concurrent writers, backfill interruption and rollback.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
