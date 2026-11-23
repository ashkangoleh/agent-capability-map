# redshift-data-platform-engineering — independent acceptance and recovery

## Capability and observed inputs
Managed warehouse cost/transaction contracts. Required context from the existing specialist: Deployment mode; compute; source format; COPY/streaming path; concurrency; table size; sort/distribution; freshness/cost.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Interrupt COPY/MERGE after API timeout with warehouse resource throttling. | Statement and ingestion outcomes reconcile with billing and snapshot state. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Resolve transaction status and resume from verified staged files. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- COPY duplicates: use manifests and validate replay. - Distribution skew: inspect slice-level distribution. - MV full refresh: inspect eligibility. - Queue buildup: separate workload classes. - Maintenance overload: avoid redundant manual jobs.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-sort-key.html
- https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
