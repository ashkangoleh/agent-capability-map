# data-orchestration-platform-selection — independent acceptance and recovery

## Capability and observed inputs
DAG interval/partition run semantics. Required context from the existing specialist: Workflow topology; triggers; task duration; retries/backfills; state durability; deployment; language; Kubernetes; multi-tenancy; SLO.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Re-run overlapping windows during scheduler failover and DST boundary. | Each declared data interval has one durable accepted output. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Pause competing runs; reprocess impacted intervals with safe overwrite/merge. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Dual-run duplicate execution: use single-writer gates or idempotent tasks. - Schedule drift: compare timezone and data interval semantics. - Backfill overload: cap concurrency. - Lost state: preserve metadata DB and external task state. - Plugin incompatibility: pin versions.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://dolphinscheduler.apache.org/en-us/docs/latest/
- https://docs.mage.ai/
- https://luigi.readthedocs.io/en/stable/
- https://oozie.apache.org/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
