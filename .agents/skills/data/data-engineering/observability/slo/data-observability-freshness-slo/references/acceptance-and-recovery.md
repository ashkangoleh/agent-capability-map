# data-observability-freshness-slo — independent acceptance and recovery

## Capability and observed inputs
Freshness and quality SLO signal fidelity. Required context from the existing specialist: Dataset producer and consumers, event/ingest/publish timestamps, data cadence, business criticality, source arrival variance, alert ownership and available telemetry.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Delay source arrival while metrics pipeline appears healthy. | SLO measures source-to-consumer availability, not just DAG status. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Declare breach and execute runbook with bounded catch-up. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Check that each alert maps to an owner and runbook and fires on measured failures. - Evaluate false-positive rates and time-to-detection on historical traces. - Include edge cases, timeouts and partial failures where material; do not claim tests executed without tool traces.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://openlineage.io/
- https://docs.getdbt.com/docs/deploy/source-freshness

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
