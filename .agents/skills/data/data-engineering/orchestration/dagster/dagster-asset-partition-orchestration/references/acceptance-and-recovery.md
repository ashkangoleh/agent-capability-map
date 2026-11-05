# dagster-asset-partition-orchestration — independent acceptance and recovery

## Capability and observed inputs
DAG interval/partition run semantics. Required context from the existing specialist: Dagster version, asset graph, partitions, sources, materialization store, refresh cadence, IO manager and external system state.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Re-run overlapping windows during scheduler failover and DST boundary. | Each declared data interval has one durable accepted output. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Pause competing runs; reprocess impacted intervals with safe overwrite/merge. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Assert dependency order and partition IDs with test fixture runs. - Reconcile materializations with target data and asset check results. - Do not assert a test, benchmark, compatibility or rollout succeeded without actual tool evidence.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://docs.dagster.io/
- https://docs.dagster.io/guides/build/assets

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
