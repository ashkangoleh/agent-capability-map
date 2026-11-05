# trino-federated-query-optimization — independent acceptance and recovery

## Capability and observed inputs
Federated joins and connector pushdown. Required context from the existing specialist: Trino version, catalog and connector versions, predicates, query plan, scan volumes, source indexes/stats, worker limits and network policy.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Fail one source or change cardinality while a cross-catalog join spills. | Results match a materialized/control query, with bounded source impact. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Cancel/fence faulty query and revert pushed-down plan/settings. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Compare EXPLAIN output and destination result under both plans. - Check source permissions, query cancellation, retries and inconsistent source snapshots. - Include edge cases, timeouts and partial failures where material; do not claim tests executed without tool traces.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://trino.io/docs/current/optimizer/pushdown.html
- https://trino.io/docs/current/sql/explain.html

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
