# starrocks-olap-warehouse-engineering — independent acceptance and recovery

## Capability and observed inputs
Primary keys, tablet distribution and load lifecycle. Required context from the existing specialist: StarRocks version; workload; table model; update rate; keys; partition lifecycle; query patterns; concurrency; compaction budget.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Retry Stream Load after unknown response and trigger compaction while reads run. | No duplicate primary-key effects; load labels and partition counts reconcile. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Check load transaction/label state before resubmission; restore prior published slice. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Update amplification: inspect key design and compaction. - Tablet skew: correct distribution key. - Compaction backlog: inspect write amplification and headroom. - MV not rewritten: inspect query shape and eligibility. - Load timeout: reconcile label/transaction state before retry.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://docs.starrocks.io/
- https://docs.starrocks.io/docs/table_design/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
