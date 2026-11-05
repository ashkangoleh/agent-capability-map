# argo-workflows-data-orchestration — independent acceptance and recovery

## Capability and observed inputs
DAG interval/partition run semantics. Required context from the existing specialist: Controller version, cluster context, namespace/RBAC, workflow spec, retry budgets, artifact store, secrets, schedules/timezones and data source/sink.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Re-run overlapping windows during scheduler failover and DST boundary. | Each declared data interval has one durable accepted output. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Pause competing runs; reprocess impacted intervals with safe overwrite/merge. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Use version-matched lint/validation for Workflow manifests. - Reconcile data output and workflow status after failed/retried task. - Disclose unverified guarantees, tests not executed, missing evidence and any unresolved recovery risk.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://argo-workflows.readthedocs.io/en/latest/workflow-templates/
- https://argo-workflows.readthedocs.io/en/latest/cron-workflows/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
