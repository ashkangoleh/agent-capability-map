---
name: data-pipeline-testing-ci-cd
description: "Build pipeline tests spanning unit, contract, integration, end-to-end, replay and performance validation."
metadata:
  version: "1.0.0"
---

# data-pipeline-testing-ci-cd

## Activation boundary
Build pipeline tests spanning unit, contract, integration, end-to-end, replay and performance validation.

## Required context
Engine, source/sink doubles, schemas, fixtures, CI runner, data volume and deployment target.

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
- https://docs.getdbt.com/docs/build/data-tests
- https://docs.pytest.org/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
