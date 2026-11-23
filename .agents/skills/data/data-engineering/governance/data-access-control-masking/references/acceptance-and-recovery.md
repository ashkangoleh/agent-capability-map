# data-access-control-masking — independent acceptance and recovery

## Capability and observed inputs
Authorization, classification and policy lineage. Required context from the existing specialist: Classification; identities/workload principals; systems; groups; row/column policy; encryption/KMS; object storage; audit and emergency access.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Revoke permissions and rotate credentials while cached reader remains active. | Deny-by-default access, correct masking and durable audit provenance. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Block affected consumers and restore reviewed least-privilege policy. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Direct object-store bypass: restrict bucket/prefix access or use credential vending. - Overbroad service account: scope roles and rotate credentials. - Masking inconsistency: test every query engine/export path. - Revocation lag: measure token/session lifetime and terminate sessions where required. - Sensitive values in logs: redact payloads.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://ranger.apache.org/
- https://trino.io/docs/current/security/file-system-access-control.html

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
