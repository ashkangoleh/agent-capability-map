# multi-engine-data-platform-interoperability: independent acceptance and recovery protocol

## Capability boundary
- Canonical skill: `multi-engine-data-platform-interoperability`. Do not substitute a sibling skill or invent a connector/runtime capability.
- Problem-specific focus: Cross-engine consistency and service ownership.
- Existing skill evidence requirements: Engine/version matrix; formats; catalog; object store; reader/writer roles; concurrency; type mapping; auth; transaction and recovery requirements.

## Falsification matrix (run only in an authorized, isolated test environment)
| Test | Injection / measurement | Acceptance oracle |
|---|---|---|
| Controlled baseline | Freeze source revision, engine/connector versions, identifiers, data slices, business grain, permissions and downstream SLO. Run a representative non-mutating probe. | Record reference counts, checksums or justified invariants, query/ingest latency and cost; report unknowns explicitly. |
| Targeted fault injection | Kill the authoritative writer between persist, metadata handoff and downstream publication. | Row/business invariants remain consistent across replays and mutually incompatible readers. |
| Recovery and replay | Interrupt after a durable handoff, restart with an unchanged input and reconcile state at source and sink. | Revert traffic to last verified publication manifest or snapshot. Verify no stale/duplicate business effects or lost deletes. |
| Version and boundary regression | Upgrade one dependency or mutate a relevant schema/partition contract while holding the test dataset fixed. | Reject undocumented behavioral differences, hidden privilege expansion and unsupported compatibility claims. |

## Failure signals inherited from the specialist
- Engine writes metadata another cannot read: inspect format/catalog feature matrix. - Concurrent commit conflict: serialize writes or prove coordination. - Partial publication: hide output until manifest/catalog commit is verified. - Type mismatch: use explicit casts and boundary tests. - Credential mismatch: separate catalog and object-store auth.

## Evidence required for a deployable recommendation
- [ ] Actual release/build, catalog/connector mode and privilege boundary recorded from deployment, not assumed from a `latest` guide.
- [ ] Exact test command/code reference and fixture/dataset revision preserved in a runnable artifact (if an execution is authorized).
- [ ] Source vs sink reconciliation and negative test outputs recorded with observed counts or hashes; no fabricated benchmark numbers.
- [ ] Failure injection, retry/replay, partial-commit and recovery observations distinguished from proposed test steps.
- [ ] Rollback/failback prerequisites, side-effect ownership, monitoring, on-call contact and stop conditions specified.
- [ ] Explicit reviewer sign-off before any production mutation. This document is not permission to access a live system.

## Reference starting points (verify installed release)
- https://trino.io/docs/current/connector/iceberg.html
- https://iceberg.apache.org/docs/latest/
- https://duckdb.org/docs/stable/

This protocol is a task-specific evaluation plan, **not** executed evidence or production certification. The generic standard-library router and Windows/Linux standalone bundles do not automatically run a skill's scripts.
