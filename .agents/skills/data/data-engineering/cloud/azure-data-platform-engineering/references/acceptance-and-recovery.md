# azure-data-platform-engineering — independent acceptance and recovery

## Source-specific contract
Focus: Managed cloud service API and billing boundaries. Evidence required by this specialist: Subscription/tenant; ADLS account; identity; Data Factory/Fabric/Synapse; Event Hubs; region; network and governance.

## Falsification matrix
| Scenario | Probe | Acceptance oracle |
|---|---|---|
| Baseline | Pin deployed builds, source/target revisions, input grain, authorization scope and representative workload. Record control counts and costs. | Results agree with a trusted independent baseline; missing observations stay UNKNOWN. |
| Targeted fault | Inject regional API throttling or loss of identity permissions mid-load. | No unauthorized access or unbounded retry/cost; table outcomes remain reconcilable. |
| Replay and recovery | Crash after a durable write and before checkpoint; restart with identical inputs and verify replay/cleanup. | Stop jobs, reconcile partial cloud artifacts and redeploy pinned configuration. |
| Version/contract drift | Change a schema or connector release on a fixed test fixture and compare before/after. | No undocumented type/data loss, access regression or false compatibility claims. |

## Existing specialist risk signals
- ADLS ACL mismatch: test both RBAC and POSIX ACL evaluation. - Managed identity failure: verify role assignment scope and token audience. - Event Hubs checkpoint loss: preserve checkpoint store and define replay. - Data Factory retry duplicates: make sink idempotent. - Fabric capacity throttling: monitor CU saturation and workload isolation.

## Evidence checklist
- [ ] Confirm installed runtime and connector versions with official release documentation; do not trust `latest`.
- [ ] Preserve exact fixture/data snapshot, code/config revision and evaluation commands, if executed.
- [ ] Measure reconciliation per business key and timestamp/window, including duplicates, late changes and deletes as applicable.
- [ ] Report observed fault injection and recovery separately from unexecuted test plans.
- [ ] Record SLO/cost/incident owner, security boundary, release stop and rollback/failback conditions.
- [ ] Require explicit approval for live mutations and never interpret this guide as authorization.

## Reference starting points — pin release before use
- https://learn.microsoft.com/azure/architecture/data-guide/
- https://learn.microsoft.com/azure/storage/blobs/data-lake-storage-introduction
- https://learn.microsoft.com/azure/event-hubs/event-hubs-about

Not evidence of production readiness. The standalone router does not automatically execute referenced scripts.
