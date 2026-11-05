# materialize-streaming-sql-engineering — independent acceptance and recovery

## Capability and observed inputs
Incremental materialized-view freshness and retractions. Required context from the existing specialist: Materialize version; sources/sinks; event identity; freshness; indexes; concurrency; retention; auth.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Insert out-of-order updates/retractions under high watermark lag. | Materialized view equals reference batch computation after convergence. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Rebuild from source log or restore verified snapshot. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Frontier stalls: identify slow source/dataflow. - Arrangement growth: review indexes and joins. - Sink duplicates: enforce stable keys. - Source reconnect: verify offsets and source retention. - Latency regression: inspect index coverage and plans.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://materialize.com/docs/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
