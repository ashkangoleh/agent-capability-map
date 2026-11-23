# elasticsearch-pit-bulk-extraction: independent acceptance and recovery protocol

## Capability boundary
- Canonical skill: `elasticsearch-pit-bulk-extraction`. Do not substitute a sibling skill or invent a connector/runtime capability.
- Problem-specific focus: PIT/search-after and extraction replay.
- Existing skill evidence requirements: Elasticsearch version, index/data stream, query filter, expected hits, PIT keep_alive, sort fields, API permissions, sink and day/window boundaries.

## Falsification matrix (run only in an authorized, isolated test environment)
| Test | Injection / measurement | Acceptance oracle |
|---|---|---|
| Controlled baseline | Freeze source revision, engine/connector versions, identifiers, data slices, business grain, permissions and downstream SLO. Run a representative non-mutating probe. | Record reference counts, checksums or justified invariants, query/ingest latency and cost; report unknowns explicitly. |
| Targeted fault injection | Expire a PIT and fail a shard/page after a successful partial batch. | A unique document-version or stable primary key set reconciles with target counts. |
| Recovery and replay | Interrupt after a durable handoff, restart with an unchanged input and reconcile state at source and sink. | Reuse persisted day/page cache or restart a fresh consistent extraction window. Verify no stale/duplicate business effects or lost deletes. |
| Version and boundary regression | Upgrade one dependency or mutate a relevant schema/partition contract while holding the test dataset fixed. | Reject undocumented behavioral differences, hidden privilege expansion and unsupported compatibility claims. |

## Failure signals inherited from the specialist
No sufficiently specific failure section found; escalate for human domain review before release.

## Evidence required for a deployable recommendation
- [ ] Actual release/build, catalog/connector mode and privilege boundary recorded from deployment, not assumed from a `latest` guide.
- [ ] Exact test command/code reference and fixture/dataset revision preserved in a runnable artifact (if an execution is authorized).
- [ ] Source vs sink reconciliation and negative test outputs recorded with observed counts or hashes; no fabricated benchmark numbers.
- [ ] Failure injection, retry/replay, partial-commit and recovery observations distinguished from proposed test steps.
- [ ] Rollback/failback prerequisites, side-effect ownership, monitoring, on-call contact and stop conditions specified.
- [ ] Explicit reviewer sign-off before any production mutation. This document is not permission to access a live system.

## Reference starting points (verify installed release)
- https://www.elastic.co/guide/en/elasticsearch/reference/current/point-in-time-api.html
- https://www.elastic.co/guide/en/elasticsearch/reference/current/paginate-search-results.html

This protocol is a task-specific evaluation plan, **not** executed evidence or production certification. The generic standard-library router and Windows/Linux standalone bundles do not automatically run a skill's scripts.
