# cloud-object-storage-data-lake-operations — independent acceptance and recovery

## Capability and observed inputs
Storage durability and metadata/listing consistency. Required context from the existing specialist: Provider, region, bucket policy, versioning, encryption, lifecycle, client and table format.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Remove/deny object access while writer upload completes or metadata is cached. | Data content and metadata are reconstructible from verified copies. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Restore immutable backups and reconcile storage inventory. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee. - Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits. - Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/
- https://cloud.google.com/storage/docs
- https://learn.microsoft.com/en-us/azure/storage/blobs/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
