# data-schema-migration-release-management — independent acceptance and recovery

## Source-specific contract
Focus: Release and data contract promotion. Evidence required by this specialist: Current/target schema; producers/consumers; format/catalog; volume; update/delete behavior; deployment order; compatibility window; rollback.

## Falsification matrix
| Scenario | Probe | Acceptance oracle |
|---|---|---|
| Baseline | Pin deployed builds, source/target revisions, input grain, authorization scope and representative workload. Record control counts and costs. | Results agree with a trusted independent baseline; missing observations stay UNKNOWN. |
| Targeted fault | Deploy incompatible schema or partial pipeline artifact under concurrent run. | Old and new consumers maintain verified contract and lineage. |
| Replay and recovery | Crash after a durable write and before checkpoint; restart with identical inputs and verify replay/cleanup. | Roll back immutable artifact and compensate or quarantine incompatible publication. |
| Version/contract drift | Change a schema or connector release on a fixed test fixture and compare before/after. | No undocumented type/data loss, access regression or false compatibility claims. |

## Existing specialist risk signals
- Consumer deployed too late: roll back producer or keep dual representation. - Type narrowing: reject/quarantine values that cannot be represented. - Rename treated as additive: preserve old field until consumers migrate. - Backfill overlap: deduplicate by stable key/version. - Physical rewrite rollback: verify snapshot/time-travel retention before promising reversibility.

## Evidence checklist
- [ ] Confirm installed runtime and connector versions with official release documentation; do not trust `latest`.
- [ ] Preserve exact fixture/data snapshot, code/config revision and evaluation commands, if executed.
- [ ] Measure reconciliation per business key and timestamp/window, including duplicates, late changes and deletes as applicable.
- [ ] Report observed fault injection and recovery separately from unexecuted test plans.
- [ ] Record SLO/cost/incident owner, security boundary, release stop and rollback/failback conditions.
- [ ] Require explicit approval for live mutations and never interpret this guide as authorization.

## Reference starting points — pin release before use
- https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html
- https://iceberg.apache.org/docs/latest/evolution/

Not evidence of production readiness. The standalone router does not automatically execute referenced scripts.
