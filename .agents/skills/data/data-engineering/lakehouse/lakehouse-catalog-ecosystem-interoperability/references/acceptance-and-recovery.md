# lakehouse-catalog-ecosystem-interoperability — independent acceptance and recovery

## Capability and observed inputs
Table-format and object-store commit contracts. Required context from the existing specialist: Format/version; catalog/version; engines/versions; REST/native protocol; auth/credential vending; object store; writer concurrency; tenancy.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Fail object upload or metadata commit during simultaneous writers. | Reader-visible snapshot atomicity and delete semantics are proven for installed engine versions. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Quarantine uncommitted files; restore last readable catalog head. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Catalog accepts metadata but engine cannot read: inspect unsupported extensions and auth flow. - Concurrent commit conflict: retry only after refresh and idempotency proof. - Credential vending failure: separate catalog auth from object-store IAM. - Catalog backup without files: restore metadata and storage from coordinated points. - Governance catalog mistaken for table catalog: keep lineage separate from commit path.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://iceberg.apache.org/docs/latest/rest-catalog/
- https://polaris.apache.org/
- https://docs.lakekeeper.io/
- https://projectnessie.org/
- https://gravitino.apache.org/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
