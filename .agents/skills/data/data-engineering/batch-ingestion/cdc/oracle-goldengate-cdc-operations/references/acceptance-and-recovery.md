# oracle-goldengate-cdc-operations: independent acceptance and recovery protocol

## Capability boundary
- Canonical skill: `oracle-goldengate-cdc-operations`. Do not substitute a sibling skill or invent a connector/runtime capability.
- Problem-specific focus: CDC positions, snapshots and schema evolution.
- Existing skill evidence requirements: Collect source and target database products and versions, GoldenGate release and deployment model, Extract and Replicat modes, source logging configuration, table keys, DDL scope, transaction volume, latency objective, trail storage, network topology, security model, retention and RPO/RTO.

## Falsification matrix (run only in an authorized, isolated test environment)
| Test | Injection / measurement | Acceptance oracle |
|---|---|---|
| Controlled baseline | Freeze source revision, engine/connector versions, identifiers, data slices, business grain, permissions and downstream SLO. Run a representative non-mutating probe. | Record reference counts, checksums or justified invariants, query/ingest latency and cost; report unknowns explicitly. |
| Targeted fault injection | Interrupt snapshot-to-stream transition and inject DDL, deletes and an unavailable log segment. | One logical change is reproducibly accounted for using position+key, with no silent missing deletes. |
| Recovery and replay | Interrupt after a durable handoff, restart with an unchanged input and reconcile state at source and sink. | Resume from a verified cursor/LSN/SCN or restore full snapshot with deduplicated replay. Verify no stale/duplicate business effects or lost deletes. |
| Version and boundary regression | Upgrade one dependency or mutate a relevant schema/partition contract while holding the test dataset fixed. | Reject undocumented behavioral differences, hidden privilege expansion and unsupported compatibility claims. |

## Failure signals inherited from the specialist
- Source log retention expires before Extract catches up: the capture gap may require a controlled re-instantiation, not a blind restart. - Trail storage fills or distribution paths stall: preserve trail files, restore capacity and verify checkpoints before purging. - Replicat repeatedly abends on a row or DDL operation: isolate the failing transaction and determine whether the issue is mapping, unsupported data, target constraint or ordering. - Missing supplemental logging or stable keys can make updates/deletes incomplete or ambiguous. - For GoldenGate for SQL Server CDC capture, the SQL Server CDC cleanup job can purge staging rows before 

## Evidence required for a deployable recommendation
- [ ] Actual release/build, catalog/connector mode and privilege boundary recorded from deployment, not assumed from a `latest` guide.
- [ ] Exact test command/code reference and fixture/dataset revision preserved in a runnable artifact (if an execution is authorized).
- [ ] Source vs sink reconciliation and negative test outputs recorded with observed counts or hashes; no fabricated benchmark numbers.
- [ ] Failure injection, retry/replay, partial-commit and recovery observations distinguished from proposed test steps.
- [ ] Rollback/failback prerequisites, side-effect ownership, monitoring, on-call contact and stop conditions specified.
- [ ] Explicit reviewer sign-off before any production mutation. This document is not permission to access a live system.

## Reference starting points (verify installed release)
- https://docs.oracle.com/en/database/goldengate/core/26/coredoc/index.html
- https://docs.oracle.com/en/database/goldengate/core/26/coredoc/overview-components-data-replication-oracle-goldengate.html
- https://docs.oracle.com/en/database/goldengate/core/26/coredoc/prepare-preparing-database-oracle-goldengate-cdc-capture.html
- https://docs.oracle.com/en/database/goldengate/core/26/coredoc/configure-ogg-adding-extract-and-replicat.html

This protocol is a task-specific evaluation plan, **not** executed evidence or production certification. The generic standard-library router and Windows/Linux standalone bundles do not automatically run a skill's scripts.
