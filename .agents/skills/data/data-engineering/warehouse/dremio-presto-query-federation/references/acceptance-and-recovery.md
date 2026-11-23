# dremio-presto-query-federation — independent acceptance and recovery

## Capability and observed inputs
OLAP schema design and cross-engine query behavior. Required context from the existing specialist: Engine/version; connector versions; source query limits; identity propagation; schemas; network; workload and latency SLO.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Load duplicate and late update keys under partition skew and stale materialized view. | Query result, primary/aggregate semantics and refresh lag meet recorded SLO. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Revert schema/MV or rebuild affected partitions from replayable staging. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- No pushdown: reduce remote scans or materialize a governed intermediate. - Source overload: isolate workloads and cap concurrency. - Inconsistent results: define snapshot/isolation limitations across sources. - Credential leakage: use scoped source credentials and audit identity mapping. - Schema drift: refresh metadata and contract-test dependent queries.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://trino.io/docs/current/
- https://docs.dremio.com/current/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
