# oci-data-platform-engineering — independent acceptance and recovery

## Source-specific contract
Focus: Managed cloud service API and billing boundaries. Evidence required by this specialist: Region/tenancy; compartments; IAM; sources; Data Flow/Spark version; GoldenGate; Streaming retention; Object Storage; database workload.

## Falsification matrix
| Scenario | Probe | Acceptance oracle |
|---|---|---|
| Baseline | Pin deployed builds, source/target revisions, input grain, authorization scope and representative workload. Record control counts and costs. | Results agree with a trusted independent baseline; missing observations stay UNKNOWN. |
| Targeted fault | Inject regional API throttling or loss of identity permissions mid-load. | No unauthorized access or unbounded retry/cost; table outcomes remain reconcilable. |
| Replay and recovery | Crash after a durable write and before checkpoint; restart with identical inputs and verify replay/cleanup. | Stop jobs, reconcile partial cloud artifacts and redeploy pinned configuration. |
| Version/contract drift | Change a schema or connector release on a fixed test fixture and compare before/after. | No undocumented type/data loss, access regression or false compatibility claims. |

## Existing specialist risk signals
- IAM denial: inspect principal and compartment scope. - GoldenGate lag: separate extract, transport and apply. - Data Flow failure: preserve logs and immutable inputs. - Streaming retention expiry: define checkpoint and replay SLA. - Region mismatch: validate availability and residency.

## Evidence checklist
- [ ] Confirm installed runtime and connector versions with official release documentation; do not trust `latest`.
- [ ] Preserve exact fixture/data snapshot, code/config revision and evaluation commands, if executed.
- [ ] Measure reconciliation per business key and timestamp/window, including duplicates, late changes and deletes as applicable.
- [ ] Report observed fault injection and recovery separately from unexecuted test plans.
- [ ] Record SLO/cost/incident owner, security boundary, release stop and rollback/failback conditions.
- [ ] Require explicit approval for live mutations and never interpret this guide as authorization.

## Reference starting points — pin release before use
- https://docs.oracle.com/en-us/iaas/data-flow/using/home.htm
- https://docs.oracle.com/en-us/iaas/goldengate/

Not evidence of production readiness. The standalone router does not automatically execute referenced scripts.
