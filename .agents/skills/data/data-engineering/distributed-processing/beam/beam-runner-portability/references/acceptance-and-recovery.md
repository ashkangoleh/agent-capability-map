# beam-runner-portability — independent acceptance and recovery

## Capability and observed inputs
Distributed engine data contracts. Required context from the existing specialist: Beam SDK version and language, target runners, source/sink IOs, boundedness, event-time/trigger strategy, portable feature set and deployment constraints.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Force worker loss, network partition and memory pressure during shuffle. | No data loss/duplication beyond explicitly stated sink guarantees. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Resume from durable partitions/checkpoints or discard uncommitted output. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Compare reference output across supported runner targets. - Fail closed on unverified SDK/runner feature combinations. - Do not assert a test, benchmark, compatibility or rollout succeeded without actual tool evidence.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://beam.apache.org/documentation/programming-guide/
- https://beam.apache.org/documentation/runners/capability-matrix/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
