# sqlserver-cdc-change-tracking: independent acceptance and recovery protocol

## Capability boundary
- Canonical skill: `sqlserver-cdc-change-tracking`. Do not substitute a sibling skill or invent a connector/runtime capability.
- Problem-specific focus: CDC positions, snapshots and schema evolution.
- Existing skill evidence requirements: Collect SQL Server/Azure SQL product and version, database compatibility level, recovery/replication configuration, capture or tracking mode, source table keys, capture columns, retention, SQL Agent availability, expected lag, extraction cadence, consumer checkpoint store and target idempotency.

## Falsification matrix (run only in an authorized, isolated test environment)
| Test | Injection / measurement | Acceptance oracle |
|---|---|---|
| Controlled baseline | Freeze source revision, engine/connector versions, identifiers, data slices, business grain, permissions and downstream SLO. Run a representative non-mutating probe. | Record reference counts, checksums or justified invariants, query/ingest latency and cost; report unknowns explicitly. |
| Targeted fault injection | Interrupt snapshot-to-stream transition and inject DDL, deletes and an unavailable log segment. | One logical change is reproducibly accounted for using position+key, with no silent missing deletes. |
| Recovery and replay | Interrupt after a durable handoff, restart with an unchanged input and reconcile state at source and sink. | Resume from a verified cursor/LSN/SCN or restore full snapshot with deduplicated replay. Verify no stale/duplicate business effects or lost deletes. |
| Version and boundary regression | Upgrade one dependency or mutate a relevant schema/partition contract while holding the test dataset fixed. | Reject undocumented behavioral differences, hidden privilege expansion and unsupported compatibility claims. |

## Failure signals inherited from the specialist
- Capture job stopped or behind: the source transaction log may not truncate as expected and CDC latency grows. - Cleanup retention overtakes a consumer watermark: the requested LSN interval is no longer complete. - A query requests an LSN outside the capture instance validity interval: stop rather than silently skipping data. - CT retention expires before the consumer reads changes: re-baseline; the old version cannot be replayed. - Update before/after rows are treated as independent business updates: downstream state becomes incorrect. - Source DDL changes alter capture shape or invalidate assumptions: coordinate a new capture instance and 

## Evidence required for a deployable recommendation
- [ ] Actual release/build, catalog/connector mode and privilege boundary recorded from deployment, not assumed from a `latest` guide.
- [ ] Exact test command/code reference and fixture/dataset revision preserved in a runnable artifact (if an execution is authorized).
- [ ] Source vs sink reconciliation and negative test outputs recorded with observed counts or hashes; no fabricated benchmark numbers.
- [ ] Failure injection, retry/replay, partial-commit and recovery observations distinguished from proposed test steps.
- [ ] Rollback/failback prerequisites, side-effect ownership, monitoring, on-call contact and stop conditions specified.
- [ ] Explicit reviewer sign-off before any production mutation. This document is not permission to access a live system.

## Reference starting points (verify installed release)
- https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server
- https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/administer-and-monitor-change-data-capture-sql-server
- https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/work-with-change-data-sql-server
- https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/track-data-changes-sql-server

This protocol is a task-specific evaluation plan, **not** executed evidence or production certification. The generic standard-library router and Windows/Linux standalone bundles do not automatically run a skill's scripts.
