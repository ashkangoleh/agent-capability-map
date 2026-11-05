# data-pipeline-testing-ci-cd — independent acceptance and recovery

## Source-specific contract
Focus: Release and data contract promotion. Evidence required by this specialist: Pipeline DAG/assets; transformations; sources/sinks; schemas/contracts; environments; volumes; replay/backfill; secrets and identity.

## Falsification matrix
| Scenario | Probe | Acceptance oracle |
|---|---|---|
| Baseline | Pin deployed builds, source/target revisions, input grain, authorization scope and representative workload. Record control counts and costs. | Results agree with a trusted independent baseline; missing observations stay UNKNOWN. |
| Targeted fault | Deploy incompatible schema or partial pipeline artifact under concurrent run. | Old and new consumers maintain verified contract and lineage. |
| Replay and recovery | Crash after a durable write and before checkpoint; restart with identical inputs and verify replay/cleanup. | Roll back immutable artifact and compensate or quarantine incompatible publication. |
| Version/contract drift | Change a schema or connector release on a fixed test fixture and compare before/after. | No undocumented type/data loss, access regression or false compatibility claims. |

## Existing specialist risk signals
- Flaky integration tests: isolate dependencies and retain diagnostics. - Test schema differs from production: validate production contract. - Retry duplicates rows: enforce sink idempotency and inject failures. - Backfill not covered: test historical windows and concurrent live ingestion. - Config drift: compare rendered config and secret references.

## Evidence checklist
- [ ] Confirm installed runtime and connector versions with official release documentation; do not trust `latest`.
- [ ] Preserve exact fixture/data snapshot, code/config revision and evaluation commands, if executed.
- [ ] Measure reconciliation per business key and timestamp/window, including duplicates, late changes and deletes as applicable.
- [ ] Report observed fault injection and recovery separately from unexecuted test plans.
- [ ] Record SLO/cost/incident owner, security boundary, release stop and rollback/failback conditions.
- [ ] Require explicit approval for live mutations and never interpret this guide as authorization.

## Reference starting points — pin release before use
- https://docs.getdbt.com/docs/build/data-tests
- https://docs.pytest.org/
- https://docs.dagster.io/guides/test

Not evidence of production readiness. The standalone router does not automatically execute referenced scripts.
