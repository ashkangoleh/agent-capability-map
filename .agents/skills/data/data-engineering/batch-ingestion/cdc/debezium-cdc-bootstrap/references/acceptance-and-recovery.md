# debezium-cdc-bootstrap: independent acceptance and recovery protocol

## Capability boundary
- Canonical skill: `debezium-cdc-bootstrap`. Do not substitute a sibling skill or invent a connector/runtime capability.
- Problem-specific focus: CDC positions, snapshots and schema evolution.
- Existing skill evidence requirements: Source database engine/version, Debezium connector/version, snapshot mode, replication permissions, transaction log retention, tables and primary keys, downstream consumers.

## Falsification matrix (run only in an authorized, isolated test environment)
| Test | Injection / measurement | Acceptance oracle |
|---|---|---|
| Controlled baseline | Freeze source revision, engine/connector versions, identifiers, data slices, business grain, permissions and downstream SLO. Run a representative non-mutating probe. | Record reference counts, checksums or justified invariants, query/ingest latency and cost; report unknowns explicitly. |
| Targeted fault injection | Interrupt snapshot-to-stream transition and inject DDL, deletes and an unavailable log segment. | One logical change is reproducibly accounted for using position+key, with no silent missing deletes. |
| Recovery and replay | Interrupt after a durable handoff, restart with an unchanged input and reconcile state at source and sink. | Resume from a verified cursor/LSN/SCN or restore full snapshot with deduplicated replay. Verify no stale/duplicate business effects or lost deletes. |
| Version and boundary regression | Upgrade one dependency or mutate a relevant schema/partition contract while holding the test dataset fixed. | Reject undocumented behavioral differences, hidden privilege expansion and unsupported compatibility claims. |

## Failure signals inherited from the specialist
- Reconcile source primary keys and CDC changes after the snapshot boundary. - Record LSN/binlog offsets, schema-history topic status, connector lag and snapshot progress. - Do not assert a test, benchmark, compatibility or rollout succeeded without actual tool evidence.

## Evidence required for a deployable recommendation
- [ ] Actual release/build, catalog/connector mode and privilege boundary recorded from deployment, not assumed from a `latest` guide.
- [ ] Exact test command/code reference and fixture/dataset revision preserved in a runnable artifact (if an execution is authorized).
- [ ] Source vs sink reconciliation and negative test outputs recorded with observed counts or hashes; no fabricated benchmark numbers.
- [ ] Failure injection, retry/replay, partial-commit and recovery observations distinguished from proposed test steps.
- [ ] Rollback/failback prerequisites, side-effect ownership, monitoring, on-call contact and stop conditions specified.
- [ ] Explicit reviewer sign-off before any production mutation. This document is not permission to access a live system.

## Reference starting points (verify installed release)
- https://debezium.io/documentation/
- https://debezium.io/blog/2025/10/06/add-new-table-to-capture-list/

This protocol is a task-specific evaluation plan, **not** executed evidence or production certification. The generic standard-library router and Windows/Linux standalone bundles do not automatically run a skill's scripts.
