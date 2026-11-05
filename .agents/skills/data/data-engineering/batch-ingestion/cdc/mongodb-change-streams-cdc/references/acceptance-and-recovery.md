# mongodb-change-streams-cdc: independent acceptance and recovery protocol

## Capability boundary
- Canonical skill: `mongodb-change-streams-cdc`. Do not substitute a sibling skill or invent a connector/runtime capability.
- Problem-specific focus: CDC positions, snapshots and schema evolution.
- Existing skill evidence requirements: Collect MongoDB server and driver versions, replica-set or sharded-cluster topology, watch scope, read preference, event filters, oplog window, pre/post-image configuration and retention, source throughput, sink commit model, consumer checkpoint store and recovery objective.

## Falsification matrix (run only in an authorized, isolated test environment)
| Test | Injection / measurement | Acceptance oracle |
|---|---|---|
| Controlled baseline | Freeze source revision, engine/connector versions, identifiers, data slices, business grain, permissions and downstream SLO. Run a representative non-mutating probe. | Record reference counts, checksums or justified invariants, query/ingest latency and cost; report unknowns explicitly. |
| Targeted fault injection | Interrupt snapshot-to-stream transition and inject DDL, deletes and an unavailable log segment. | One logical change is reproducibly accounted for using position+key, with no silent missing deletes. |
| Recovery and replay | Interrupt after a durable handoff, restart with an unchanged input and reconcile state at source and sink. | Resume from a verified cursor/LSN/SCN or restore full snapshot with deduplicated replay. Verify no stale/duplicate business effects or lost deletes. |
| Version and boundary regression | Upgrade one dependency or mutate a relevant schema/partition contract while holding the test dataset fixed. | Reject undocumented behavioral differences, hidden privilege expansion and unsupported compatibility claims. |

## Failure signals inherited from the specialist
- Oplog history no longer contains the resume point: stop incremental replay and perform a documented resnapshot/reconciliation. - Resume pipeline or options changed: do not reuse the old token with a different stream definition. - Collection drop/rename emits invalidate: use the appropriate new stream start procedure; resumeAfter is not interchangeable with startAfter. - updateLookup returns a later document version or null: use event deltas or configured pre/post images when event-time state is required. A pipeline that filters on fullDocument can also make resume-token lookup fail when updateLookup returns null after a delete; validate thi

## Evidence required for a deployable recommendation
- [ ] Actual release/build, catalog/connector mode and privilege boundary recorded from deployment, not assumed from a `latest` guide.
- [ ] Exact test command/code reference and fixture/dataset revision preserved in a runnable artifact (if an execution is authorized).
- [ ] Source vs sink reconciliation and negative test outputs recorded with observed counts or hashes; no fabricated benchmark numbers.
- [ ] Failure injection, retry/replay, partial-commit and recovery observations distinguished from proposed test steps.
- [ ] Rollback/failback prerequisites, side-effect ownership, monitoring, on-call contact and stop conditions specified.
- [ ] Explicit reviewer sign-off before any production mutation. This document is not permission to access a live system.

## Reference starting points (verify installed release)
- https://www.mongodb.com/docs/manual/changestreams/
- https://www.mongodb.com/docs/manual/reference/operator/aggregation/changestream/
- https://www.mongodb.com/docs/manual/reference/change-events/update/

This protocol is a task-specific evaluation plan, **not** executed evidence or production certification. The generic standard-library router and Windows/Linux standalone bundles do not automatically run a skill's scripts.
