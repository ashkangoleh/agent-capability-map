# apache-doris-olap-engineering — independent acceptance and recovery

## Capability and observed inputs
OLAP schema design and cross-engine query behavior. Required context from the existing specialist: Doris version; deployment mode; table model; source/sink; data rate; partitioning; materialized views; concurrency and retention.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Load duplicate and late update keys under partition skew and stale materialized view. | Query result, primary/aggregate semantics and refresh lag meet recorded SLO. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Revert schema/MV or rebuild affected partitions from replayable staging. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Tablet skew: revise distribution key and bucket count. - Compaction backlog: inspect ingestion bursts and storage headroom. - Load retry duplicates: reconcile labels/transactions before replay. - MV not used: inspect rewrite eligibility and freshness. - FE/BE failure: verify quorum/replicas before increasing load.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://doris.apache.org/docs/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
