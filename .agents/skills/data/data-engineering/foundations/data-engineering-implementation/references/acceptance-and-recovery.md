# data-engineering-implementation — independent acceptance and recovery

## Capability and observed inputs
Data model grain and reproducible lifecycle. Required context from the existing specialist: Establish source and sink, engine and versions, data volume, throughput, latency/SLO, retention, security, governance, deployment model, and acceptable recovery objectives. Mark unknowns rather than inventing them.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Replay late update/delete and mutate source schema under an existing model. | Business grain, temporal validity and schema evolution remain auditable. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Version model contracts and rebuild affected partitions. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
Do not recommend a production design without understanding source/sink consistency and recovery requirements. Do not claim zero data loss, exactly-once, or performance gains without evidence.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- No primary URL found in the original skill. API/version claims are blocked pending official verification.

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
