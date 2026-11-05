# ray-data-pipeline-engineering — independent acceptance and recovery

## Capability and observed inputs
Distributed engine data contracts. Required context from the existing specialist: Ray release, cluster/memory and object store, source/sink, data schema, blocks, concurrency, acceleration needs, deployment and failure limits.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Force worker loss, network partition and memory pressure during shuffle. | No data loss/duplication beyond explicitly stated sink guarantees. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Resume from durable partitions/checkpoints or discard uncommitted output. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Test output schema and row cardinality across a controlled rerun. - Record Ray dashboard metrics and resource usage on representative data. - Disclose unverified guarantees, tests not executed, missing evidence and any unresolved recovery risk.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://docs.ray.io/en/latest/data/key-concepts.html
- https://docs.ray.io/en/latest/data/loading-data.html

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
