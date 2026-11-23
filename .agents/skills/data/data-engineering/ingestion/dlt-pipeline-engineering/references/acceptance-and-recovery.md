# dlt-pipeline-engineering — independent acceptance and recovery

## Capability and observed inputs
Connector state, pagination and external quotas. Required context from the existing specialist: dlt version; source/resource; cursor or primary key; destination; write disposition; schema; state location; run frequency and retries.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Repeat pages after timeout, expire token and rate limit midway. | Source progress advances only after target commit, and deduplication is deterministic. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Resume from last confirmed cursor; quarantine ambiguous writes. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Cursor skips late updates: use overlap or source change sequence and deduplicate. - State lost: restore matching pipeline/source identity; do not restart at latest by default. - Schema drift: quarantine incompatible changes and preserve raw payload. - Partial destination load: inspect package/job state before retry. - Replace mode deletes good data: validate scope and use staging/swap when supported.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://dlthub.com/docs/
- https://dlthub.com/docs/general-usage/incremental-loading

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
