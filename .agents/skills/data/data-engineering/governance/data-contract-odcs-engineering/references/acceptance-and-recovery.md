# data-contract-odcs-engineering — independent acceptance and recovery

## Capability and observed inputs
Authorization, classification and policy lineage. Required context from the existing specialist: Producer/consumer owners; dataset/event identity; schema; semantics; quality; freshness SLO; classification; access; compatibility/deprecation policy.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Revoke permissions and rotate credentials while cached reader remains active. | Deny-by-default access, correct masking and durable audit provenance. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Block affected consumers and restore reviewed least-privilege policy. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Contract exists but is unenforced: do not report compliance; add executable gates. - Semantic ambiguity: require business definitions and examples, not only SQL types. - Breaking change: publish a new version and use expand-contract. - SLO not measurable: define timestamp source and missing-data behavior. - No accountable owner: block production activation.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://bitol-io.github.io/open-data-contract-standard/
- https://docs.getdbt.com/docs/mesh/govern/model-contracts

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
