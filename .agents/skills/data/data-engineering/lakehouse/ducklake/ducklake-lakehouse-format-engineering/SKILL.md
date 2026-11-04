---
name: ducklake-lakehouse-format-engineering
description: "Design DuckLake catalogs, snapshots, schema evolution, file lifecycle and multi-client compatibility with explicit DuckDB version gates."
license: Proprietary
metadata:
  version: "1.1.0"
---

# ducklake-lakehouse-format-engineering

## Activation boundary
Use for DuckLake table-format and catalog engineering. Do not treat it as interchangeable with Iceberg, Delta or DuckDB native storage.

## Required inputs
DuckLake/DuckDB versions; catalog backend; object store; writer concurrency; partitioning; snapshot retention; client matrix.

## Production workflow
1. Identify DuckLake format and compatible DuckDB extension versions.
2. Select catalog backend and verify transaction/locking behavior.
3. Define schema and partitioning from workload; avoid excessive partition cardinality.
4. Plan snapshot history, compaction and catalog-aware orphan cleanup.
5. Test reader/writer compatibility across intended clients.
6. Back up catalog metadata and object data at coordinated recovery points.

## Failure modes and recovery
- Catalog loss: restore a consistent backup and verify referenced files.
- Orphan files: never use blind prefix deletion.
- Concurrent conflict: serialize or use documented coordination.
- Extension mismatch: pin compatible versions and stop mixed writers.

## Validation and evidence
- Test append, supported updates/deletes, schema evolution, rollback and concurrent access.
- DuckLake 1.1 documentation specifies DuckDB 2.0.0 or later; verify deployed versions.
- Test cross-client reads/writes and restore.

## Output contract
Return version matrix, catalog/storage topology, concurrency and lifecycle policy.

## Official references
- https://ducklake.select/docs/stable/
