# polaris-iceberg-catalog-operations — independent acceptance and recovery

## Capability and observed inputs
Catalog control plane and commit contention. Required context from the existing specialist: Polaris version, Iceberg REST clients, catalog topology, object storage, identity credentials, table namespaces and availability SLO.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Fail credential vending or catalog commit after object upload. | Published metadata pointer and object permissions remain consistent; retries do not fork authoritative history. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Re-read catalog state before retry; preserve last validated table snapshot. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
Not sufficiently specified in source: requires individual expert review.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://polaris.apache.org/
- https://iceberg.apache.org/spec/#rest-catalog-api

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
