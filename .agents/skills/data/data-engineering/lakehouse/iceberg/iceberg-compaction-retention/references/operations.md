# Iceberg maintenance operation contracts

Applies to Iceberg Spark procedures, **only after verifying the deployed Iceberg + Spark release and catalog wiring**. This document is a decision reference, not an executable job.

## Operation selection

| Operation | Trigger / measured baseline | Mutation and correctness gates | Acceptance / recovery |
|---|---|---|---|
| `rewrite_data_files` | Measured small-file distribution and inflated file-open overhead | Use limited partitions/filter canary, validate delete-file application and concurrent-commit behavior; no indiscriminate rewrite-all | Compare snapshot lineage, business row invariants, file distribution and query latency. Revert only if relevant snapshots and data files remain available |
| `rewrite_manifests` | Excess manifest count or measurable planning latency | Confirm current partition spec; rewriting manifests is not data-file compaction. Observe cache invalidation | Compare planning latency, manifests and readable snapshots; re-run a scoped rewrite if needed |
| `expire_snapshots` | Snapshot history costs after approved retention window | Compare time-travel, rollback, delayed consumers, legal holds and branch/tag references. Set explicit `older_than` and `retain_last` | Review current and protected refs; expiration deletes old data not referenced by remaining snapshots and is potentially irreversible |
| `remove_orphan_files` | Files left by abandoned/uncommitted write attempts | **Always inspect `dry_run => true` first**. Set conservative `older_than` greater than in-flight writer duration plus margin; compare path scheme/authority; never override mismatch to DELETE blindly | Review each candidate class before separately authorized deletion; restore from independent backup if data is lost |

## Ordering and scope

1. Capture `<catalog>.<namespace>.<table>.snapshots`, `.history`, `.refs`, `.files`, `.manifests` and `.partitions` as supported in the installed engine.
2. Inventory live data and equality/position delete files; raw metadata `record_count` can overstate currently visible rows where deletes apply. Check business invariants with reads, not only metadata sums.
3. Prefer **one** operation at a time. Rewriting files does not by itself remove snapshots. Snapshot expiration does not make orphan cleanup universally safe.
4. Hold the table writer/concurrency policy constant during each canary; re-check the current snapshot after a commit conflict or timeout. An unknown commit outcome must be resolved by reading catalog state before retry.
5. Treat Spark procedure arguments and output schemas as release-specific, including Spark 3.x extensions versus Spark 4.x procedure behavior; verify syntax and provider capabilities before using SQL.

## Sources
- https://iceberg.apache.org/docs/latest/spark-procedures/
- https://iceberg.apache.org/docs/latest/maintenance/
- https://iceberg.apache.org/docs/latest/spark-queries/
- https://iceberg.apache.org/spec/

The sources describe features, not the capabilities or operational guarantees of an uninspected deployment.
