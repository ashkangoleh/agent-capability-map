# pipeline-backfill-recovery — independent acceptance and recovery

## Source-specific contract
Focus: Backfill windows and target idempotency. Evidence required by this specialist: Source retention and replayability, target mutation semantics, run/date windows, dataset grain, checkpoint metadata, dependency graph, throughput limit, RPO/RTO and publication visibility.

## Falsification matrix
| Scenario | Probe | Acceptance oracle |
|---|---|---|
| Baseline | Pin deployed builds, source/target revisions, input grain, authorization scope and representative workload. Record control counts and costs. | Results agree with a trusted independent baseline; missing observations stay UNKNOWN. |
| Targeted fault | Crash after target publication but before checkpoint then rerun the same date. | Backfill rerun yields identical partition/business values without duplicate effects. |
| Replay and recovery | Crash after a durable write and before checkpoint; restart with identical inputs and verify replay/cleanup. | Restore last published partition manifest and bounded replay. |
| Version/contract drift | Change a schema or connector release on a fixed test fixture and compare before/after. | No undocumented type/data loss, access regression or false compatibility claims. |

## Existing specialist risk signals
Never claim a backfill is lossless when source retention, checkpoints or sink consistency contracts are unavailable.

## Evidence checklist
- [ ] Confirm installed runtime and connector versions with official release documentation; do not trust `latest`.
- [ ] Preserve exact fixture/data snapshot, code/config revision and evaluation commands, if executed.
- [ ] Measure reconciliation per business key and timestamp/window, including duplicates, late changes and deletes as applicable.
- [ ] Report observed fault injection and recovery separately from unexecuted test plans.
- [ ] Record SLO/cost/incident owner, security boundary, release stop and rollback/failback conditions.
- [ ] Require explicit approval for live mutations and never interpret this guide as authorization.

## Reference starting points — pin release before use
- https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
- https://docs.getdbt.com/docs/build/incremental-models

Not evidence of production readiness. The standalone router does not automatically execute referenced scripts.
