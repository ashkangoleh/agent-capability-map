# aws-data-platform-engineering — independent acceptance and recovery

## Source-specific contract
Focus: Managed cloud service API and billing boundaries. Evidence required by this specialist: Account/region; data volume; latency; sources; IAM roles; S3 layout; Glue Catalog; compute/warehouse; residency and cost.

## Falsification matrix
| Scenario | Probe | Acceptance oracle |
|---|---|---|
| Baseline | Pin deployed builds, source/target revisions, input grain, authorization scope and representative workload. Record control counts and costs. | Results agree with a trusted independent baseline; missing observations stay UNKNOWN. |
| Targeted fault | Inject regional API throttling or loss of identity permissions mid-load. | No unauthorized access or unbounded retry/cost; table outcomes remain reconcilable. |
| Replay and recovery | Crash after a durable write and before checkpoint; restart with identical inputs and verify replay/cleanup. | Stop jobs, reconcile partial cloud artifacts and redeploy pinned configuration. |
| Version/contract drift | Change a schema or connector release on a fixed test fixture and compare before/after. | No undocumented type/data loss, access regression or false compatibility claims. |

## Existing specialist risk signals
- S3 direct access bypasses table grants: restrict bucket/prefix policies. - Glue crawler schema drift: enforce contract and reviewed catalog updates. - Kinesis shard throttling: scale shards or use on-demand with quota/cost review. - EMR job retry duplicates: make sink writes idempotent. - Cross-region replication: verify residency, encryption and recovery.

## Evidence checklist
- [ ] Confirm installed runtime and connector versions with official release documentation; do not trust `latest`.
- [ ] Preserve exact fixture/data snapshot, code/config revision and evaluation commands, if executed.
- [ ] Measure reconciliation per business key and timestamp/window, including duplicates, late changes and deletes as applicable.
- [ ] Report observed fault injection and recovery separately from unexecuted test plans.
- [ ] Record SLO/cost/incident owner, security boundary, release stop and rollback/failback conditions.
- [ ] Require explicit approval for live mutations and never interpret this guide as authorization.

## Reference starting points — pin release before use
- https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/building-data-lake-aws.html
- https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html
- https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html

Not evidence of production readiness. The standalone router does not automatically execute referenced scripts.
