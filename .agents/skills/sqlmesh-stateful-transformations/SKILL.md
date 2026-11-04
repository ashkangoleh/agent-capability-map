---
name: sqlmesh-stateful-transformations
description: "Build SQLMesh models with versioned environments, plans, audits, interval tracking and controlled backfills."
metadata:
  version: "1.0.0"
---

# sqlmesh-stateful-transformations

## Activation boundary
Build SQLMesh models with versioned environments, plans, audits, interval tracking and controlled backfills.

## Required context
SQLMesh/adapter release, model kind, time grain, environment, audits and concurrency.

## Production procedure
1. Declare grain, keys, dependencies, time columns and null semantics.
2. Choose incremental/merge/snapshot behavior from source mutation and target capabilities.
3. Inspect compiled SQL and query plans; bound scans, backfills and concurrency.
4. Add blocking invariants and warning-level anomaly checks.
5. Test late updates, deletes, schema changes, failed plans and restatement.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://sqlmesh.readthedocs.io/en/stable/concepts/plans/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
