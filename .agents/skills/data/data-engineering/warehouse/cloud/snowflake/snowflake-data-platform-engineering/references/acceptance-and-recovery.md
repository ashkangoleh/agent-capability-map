# snowflake-data-platform-engineering — independent acceptance and recovery

## Capability and observed inputs
Managed warehouse cost/transaction contracts. Required context from the existing specialist: Region/edition; source pattern; latency/volume; table type; warehouse budget; schema; task graph; retention/access.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Interrupt COPY/MERGE after API timeout with warehouse resource throttling. | Statement and ingestion outcomes reconcile with billing and snapshot state. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Resolve transaction status and resume from verified staged files. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- File gaps: compare event notifications with stage listing/load history. - Stream consumption mistakes: verify staleness and transaction state. - Task failure: inspect dependencies, privileges and warehouse availability. - Dynamic Table lag: inspect refresh history and incremental eligibility. - Cost spike: tune refresh cadence and compute.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://docs.snowflake.com/en/user-guide/data-load-overview
- https://docs.snowflake.com/en/user-guide/data-pipelines-intro

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
