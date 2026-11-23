# data-migration-cutover-reconciliation — independent acceptance and recovery

## Source-specific contract
Focus: Dual-read parity, cutover and fallback. Evidence required by this specialist: Source/target versions; dataset inventory; volume/change rate; downtime; consistency; CDC; type differences; RPO/RTO; rollback constraints.

## Falsification matrix
| Scenario | Probe | Acceptance oracle |
|---|---|---|
| Baseline | Pin deployed builds, source/target revisions, input grain, authorization scope and representative workload. Record control counts and costs. | Results agree with a trusted independent baseline; missing observations stay UNKNOWN. |
| Targeted fault | Switch consumers during target catch-up then fail a writer. | Source and target compare on business keys, late updates and deletes at an agreed cutover watermark. |
| Replay and recovery | Crash after a durable write and before checkpoint; restart with identical inputs and verify replay/cleanup. | Return traffic to verified old source while keeping dual-write effects fenced. |
| Version/contract drift | Change a schema or connector release on a fixed test fixture and compare before/after. | No undocumented type/data loss, access regression or false compatibility claims. |

## Existing specialist risk signals
- Snapshot/CDC gap: stop and re-establish a consistent boundary. - Out-of-order changes: deduplicate by source identity/version. - Type truncation: quarantine; never silently narrow. - Target drift: reconcile by key/version. - Rollback after target writes: define reverse replication or no-return point.

## Evidence checklist
- [ ] Confirm installed runtime and connector versions with official release documentation; do not trust `latest`.
- [ ] Preserve exact fixture/data snapshot, code/config revision and evaluation commands, if executed.
- [ ] Measure reconciliation per business key and timestamp/window, including duplicates, late changes and deletes as applicable.
- [ ] Report observed fault injection and recovery separately from unexecuted test plans.
- [ ] Record SLO/cost/incident owner, security boundary, release stop and rollback/failback conditions.
- [ ] Require explicit approval for live mutations and never interpret this guide as authorization.

## Reference starting points — pin release before use
- https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html
- https://debezium.io/documentation/reference/stable/

Not evidence of production readiness. The standalone router does not automatically execute referenced scripts.
