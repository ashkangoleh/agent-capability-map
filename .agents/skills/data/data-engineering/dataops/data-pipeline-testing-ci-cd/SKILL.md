---
name: data-pipeline-testing-ci-cd
description: "Test data pipelines from pure transformation logic through connector contracts, engine integration, replay and production deployment."
license: Proprietary
metadata:
  version: "1.1.0"
---

# data-pipeline-testing-ci-cd

## Activation boundary
Use for pipeline test strategy and CI/CD. Green unit tests do not prove source/sink integration, replay or production data correctness.

## Required context
Pipeline DAG/assets; transformations; sources/sinks; schemas/contracts; environments; volumes; replay/backfill; secrets and identity.

## Production procedure
1. Separate unit, schema/contract, connector integration, engine integration and end-to-end reconciliation tests.
2. Build deterministic fixtures for nulls, duplicates, late data, deletes, skew, malformed records and schema evolution.
3. Test first run, incremental cursor, overlap, empty interval, retry and restart.
4. Use ephemeral dependencies or controlled test environments for databases, brokers, object stores and catalogs.
5. Validate idempotency and publication atomicity; inspect target state after injected failures.
6. Keep secrets and production data out of CI; use synthetic or masked fixtures.
7. Promote immutable artifacts across environments.
8. Gate production on schema compatibility, quality thresholds, SLO and rollback readiness.

## Failure modes and recovery
- Flaky integration tests: isolate dependencies and retain diagnostics.
- Test schema differs from production: validate production contract.
- Retry duplicates rows: enforce sink idempotency and inject failures.
- Backfill not covered: test historical windows and concurrent live ingestion.
- Config drift: compare rendered config and secret references.

## Validation and acceptance
- Test duplicates, replay, late data, schema drift, empty batches, source/sink outage and partial commit.
- Reconcile counts and key-level aggregates for end-to-end fixtures.
- Record engine versions, fixture version and exclusions.
- Verify rollback and rerun from durable checkpoint.

## Output contract
Return test pyramid, CI gates, fixture matrix, deployment/rollback process and coverage gaps.

## Official or primary references
- https://docs.getdbt.com/docs/build/data-tests
- https://docs.pytest.org/
- https://docs.dagster.io/guides/test
