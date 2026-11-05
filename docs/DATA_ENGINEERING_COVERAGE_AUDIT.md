# Data Engineering Coverage Audit

**Branch:** pre_release  
**Scope:** Data Engineering only; other Data subdomains are unchanged.  
**Status:** Expanded taxonomy and specialist routing; production certification is not claimed.

## Canonical first-class scopes

1. Foundations and lifecycle
2. Source ingestion and connector engineering
3. Batch ingestion, CDC and recovery
4. Messaging and event brokers
5. Streaming semantics and streaming SQL
6. Distributed processing
7. Workflow orchestration
8. SQL transformation and ELT
9. Serialization and file formats
10. Distributed storage and NoSQL integration
11. Lakehouse table formats and catalogs
12. Warehouses, federation and real-time OLAP
13. Data observability
14. Data quality
15. Governance, contracts, privacy and access
16. DataOps and schema release
17. Pipeline reliability and disaster recovery
18. Performance, capacity and cost
19. Managed cloud data platforms
20. Data serving and reverse ETL
21. Cross-platform data migration
22. Unstructured data ingestion
23. Data platform architecture

## Added specialist packages

This tranche adds 19 active specialists: Apache SeaTunnel, Dask, Apache DataFusion/Ballista, Spark Declarative Pipelines, RisingWave, Materialize, Apache Fluss, DuckLake, StarRocks OLAP, NATS JetStream, data migration/cutover, unstructured ingestion, Snowflake, BigQuery, Redshift, Databricks Lakeflow, OCI data platform, orchestrator selection/migration and OpenMetadata catalog operations.

## Routing corrections

- Generic Data Engineering intent routes to foundations, not distributed processing.
- Ingestion connectors and batch/CDC recovery are separate scopes.
- Warehouse engines are consolidated under one tree; dimensional modeling remains in Analytics Engineering.
- Lakehouse format selection and catalog interoperability are nested under Lakehouse.
- Durable/alternative workflow engines are nested under orchestration.
- Generic fallback registrations were removed from Trino, DuckDB, Parquet and Iceberg registries; underspecified engine requests now clarify.

## Production completion gates

1. Verify each specialist against exact tool/runtime versions and official references.
2. Test source/connector/sink guarantees as a combination; do not inherit exactly-once claims.
3. Expand positive, negative, ambiguous, near-miss and Persian/English routing fixtures.
4. Add executable examples and release-specific integration tests before production certification.
5. Verify actual skill loading in Codex, OpenCode, Copilot, Claude Code and Cursor.

Passing YAML and routing tests establish structural correctness, not semantic accuracy, runtime compatibility or production readiness.

## First per-skill deepening: Iceberg compaction and retention (2026-11-05)

- Existing canonical `iceberg-compaction-retention` ID, trigger registry and route are unchanged; SKILL.md advanced from version 1.0.0 to 1.1.0. Only this Data Engineering capability's package was deepened in this increment.
- Added on-demand `references/operations.md` and `references/failure-recovery.md`, read-only `examples/spark_maintenance.sql`, an illustrative offline JSON plan, and standard-library `scripts/check_plan.py`. Preflight **never executes Spark/Catalog/SQL/storage calls** and returns `can_execute: false` even when static checks pass.
- Added `tests/test_iceberg_maintenance_skill.py` covering unchanged route, retention floor, legal hold, active writer orphan safety, manifest review, JSON rejection and non-authorization. The SQL shows mutating procedures as commented examples only.
- Official reference basis: Iceberg Spark procedures, maintenance guide, metadata queries, specification. Deployed engine/catalog compatibility, real table metrics, recovery evidence, human authorization and live tests remain **UNKNOWN**; do not claim production readiness from successful static CI.
- After CI is green on the exact new SHA, review one next Data Engineering skill in the same staged, one-at-a-time fashion; do not expand taxonomy or touch main.
