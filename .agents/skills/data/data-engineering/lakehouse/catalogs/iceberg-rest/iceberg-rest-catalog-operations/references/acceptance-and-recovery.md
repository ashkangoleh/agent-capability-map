# iceberg-rest-catalog-operations — independent acceptance and recovery

## Capability and observed inputs
Catalog control plane and commit contention. Required context from the existing specialist: - Server/product version, REST endpoint, warehouse/prefix, deployment and client/engine versions. - Auth mechanism (OAuth2, Basic, SigV4 or provider-specific), principal and namespace/table grants; never request plaintext secrets in a report. - Object-store provider and region, FileIO/credential delegation model, read/write requirements and token lifetime. - Tables, current metadata/snapshot IDs, concurrency, commit/retry policy, target SLO and recovery RPO/RTO. - Known supported protocol endpoints: read the catalog's config/endpoint-discovery response instead of presuming all extensions exist.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Fail credential vending or catalog commit after object upload. | Published metadata pointer and object permissions remain consistent; retries do not fork authoritative history. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Re-read catalog state before retry; preserve last validated table snapshot. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- **401/403**: isolate catalog identity, namespace privileges, delegated storage permissions and refresh-token expiry; never enlarge permissions by default. - **404/not supported**: check negotiated endpoint set, namespace/prefix and protocol extension support before changing table state. - **409/conflict**: reload table state, resolve concurrent writer history and replan; avoid losing successful commits. - **429/5xx**: use bounded, jittered retry only for safe/idempotent reads; for write requests first resolve commit outcome. - **Expired temporary storage credentials**: refresh through supported catalog/client mechanisms and verify job recov

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://iceberg.apache.org/rest-catalog-spec/
- https://iceberg.apache.org/docs/latest/rest-catalog/
- https://iceberg.apache.org/docs/nightly/rest-protocol/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
