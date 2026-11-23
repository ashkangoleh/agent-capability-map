---
name: dataform-warehouse-transformations
description: "Engineer Dataform SQL transformations with dependency graphs, assertions, incremental tables and release controls."
metadata:
  version: "1.0.1"
---

# dataform-warehouse-transformations

## Activation boundary
Engineer Dataform SQL transformations with dependency graphs, assertions, incremental tables and release controls.

## Required context
Dataform release, BigQuery location, repository, service account and incremental keys.

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
- https://cloud.google.com/dataform/docs

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
