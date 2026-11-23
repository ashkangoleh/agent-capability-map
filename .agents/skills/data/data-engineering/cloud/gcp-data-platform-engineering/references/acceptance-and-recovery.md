# gcp-data-platform-engineering — independent acceptance and recovery

## Source-specific contract
Focus: Managed cloud service API and billing boundaries. Evidence required by this specialist: Organization/project/region; Pub/Sub event rate; BigQuery workload; Dataflow/Dataproc runtime; GCS; IAM; quotas and cost.

## Falsification matrix
| Scenario | Probe | Acceptance oracle |
|---|---|---|
| Baseline | Pin deployed builds, source/target revisions, input grain, authorization scope and representative workload. Record control counts and costs. | Results agree with a trusted independent baseline; missing observations stay UNKNOWN. |
| Targeted fault | Inject regional API throttling or loss of identity permissions mid-load. | No unauthorized access or unbounded retry/cost; table outcomes remain reconcilable. |
| Replay and recovery | Crash after a durable write and before checkpoint; restart with identical inputs and verify replay/cleanup. | Stop jobs, reconcile partial cloud artifacts and redeploy pinned configuration. |
| Version/contract drift | Change a schema or connector release on a fixed test fixture and compare before/after. | No undocumented type/data loss, access regression or false compatibility claims. |

## Existing specialist risk signals
- Pub/Sub redelivery: use idempotent consumers and ack after durable sink commit. - Dataflow watermark stalls: inspect source partitions and slow transforms. - BigQuery append timeout: determine Storage Write API commit/offset state before retry. - GCS IAM bypass: restrict direct bucket access. - Regional mismatch: align source, processing and warehouse locations.

## Evidence checklist
- [ ] Confirm installed runtime and connector versions with official release documentation; do not trust `latest`.
- [ ] Preserve exact fixture/data snapshot, code/config revision and evaluation commands, if executed.
- [ ] Measure reconciliation per business key and timestamp/window, including duplicates, late changes and deletes as applicable.
- [ ] Report observed fault injection and recovery separately from unexecuted test plans.
- [ ] Record SLO/cost/incident owner, security boundary, release stop and rollback/failback conditions.
- [ ] Require explicit approval for live mutations and never interpret this guide as authorization.

## Reference starting points — pin release before use
- https://cloud.google.com/architecture/data-lakes
- https://cloud.google.com/dataflow/docs
- https://cloud.google.com/bigquery/docs

Not evidence of production readiness. The standalone router does not automatically execute referenced scripts.
