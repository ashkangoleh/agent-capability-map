---
name: multi-engine-data-platform-interoperability
description: "Design multi-engine data platforms across compute, query, catalog and storage without assuming shared transaction or type semantics."
license: Proprietary
metadata:
  version: "1.1.0"
---

# multi-engine-data-platform-interoperability

## Activation boundary
Use when one logical data platform spans Trino, DuckDB, Spark, Flink, StarRocks and object-store/lakehouse systems. A multi-engine workflow is not automatically a distributed transaction.

## Required context
Engine/version matrix; formats; catalog; object store; reader/writer roles; concurrency; type mapping; auth; transaction and recovery requirements.

## Production procedure
1. Draw control plane, catalog, storage, compute and serving layers separately.
2. Define canonical formats/catalog and identify each engine as reader, writer or maintenance owner.
3. Build compatibility matrix for types, schema evolution, deletes, snapshots, partition transforms and statistics.
4. Assign one authoritative writer or prove concurrent commit behavior for each shared table.
5. Define transaction boundaries for each handoff; use staging/manifests when cross-engine atomicity is unavailable.
6. Map timestamps, decimals, nested types, case sensitivity, null semantics and collation explicitly.
7. Assign compaction/snapshot maintenance ownership.
8. Define credentials and object-store permissions per engine.
9. Test failure between extract, transform, publish and catalog commit.

## Failure modes and recovery
- Engine writes metadata another cannot read: inspect format/catalog feature matrix.
- Concurrent commit conflict: serialize writes or prove coordination.
- Partial publication: hide output until manifest/catalog commit is verified.
- Type mismatch: use explicit casts and boundary tests.
- Credential mismatch: separate catalog and object-store auth.

## Validation and acceptance
- Test engine A write, engine B read and engine C maintenance on exact versions.
- Test concurrent read/write, commit conflict, schema evolution, deletes and credential rotation.
- Inject failure at each handoff and prove replay is idempotent.
- Record compatibility, bytes moved, commit latency and recovery.

## Output contract
Return layered architecture, engine responsibility matrix, compatibility table, transaction boundaries and recovery plan.

## Official or primary references
- https://trino.io/docs/current/connector/iceberg.html
- https://iceberg.apache.org/docs/latest/
- https://duckdb.org/docs/stable/
