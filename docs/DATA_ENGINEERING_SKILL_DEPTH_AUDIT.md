# Data Engineering — specialist evidence and depth audit

Scope: `data/data-engineering` on `pre_release`. Baseline: 123 existing canonical skill packages. This tranche creates **no new skill IDs or routes**. The corpus is intentionally the existing specialist inventory rather than a new taxonomy.

## Structural increment

- 123 skill packages now link to a dedicated, on-demand `references/acceptance-and-recovery.md` resource. The original procedures and official starting links remain intact.
- 35 scoped verification profiles define failure injection, acceptance oracle, recovery and impact boundary by engine/family. Each skill resource also includes the existing skill-specific operating inputs, failure signals and source URLs. Profiles are intentionally reusable; **they do not establish 123 independently authored, production-tested runbooks**.
- The router and user five-domain selection policy remain unchanged. The added resources are lazy-loaded and do not execute automatically. The first Iceberg compaction skill retains its independently implemented offline preflight script.
- Automated integrity guard: `python scripts/audit_data_engineering_skills.py --strict --summary` plus `tests/test_data_engineering_skill_depth.py`. The tool checks resource presence, profile-specific requirements, canonical naming, size and procedure/link contracts. It deliberately reports all real engine and agent-host tests as NOT_VERIFIED.

## Explicit quality levels

| Level | Evidence | Status |
|---|---|---|
| L0 | Canonical routes, owners, frontmatter, links | Existing graph / CI |
| L1 | Distinct fault/recovery plan and safe evidence boundary | Added for 123 packages, pending exact-commit CI |
| L2 | Pinned engine/connector version, executable representative example and independently verified API/config | **NOT COMPLETE** for inventory |
| L3 | Executed end-to-end fault/replay/integration tests with checksums, SLO, rollback and observed recovery | **NOT VERIFIED** repo-wide |
| L4 | Native agent-host A/B showing better correctness, safety, cost and latency against base agent | **NOT VERIFIED** |

Do not call a skill best-in-class or production ready merely because L1 passes. In particular, an automatically generated, profile-based acceptance reference cannot substitute for manually validated, engine-specific runbooks.

## Highest-risk second-pass queue

1. CDC and ingestion: Debezium, SQL Server CDC, Mongo Change Streams, GoldenGate, Elasticsearch PIT, API cursors. Prove snapshot/stream handoff, deletes and cursor boundaries.
2. Stateful streaming: Kafka, Flink, Spark Structured Streaming, broker integrations, streaming SQL. Prove source-to-sink replay and sink effects on failover; source + sink guarantees must be inspected jointly.
3. Shared lakehouse: Iceberg evolution, Delta/Hudi, Polaris/Lakekeeper/Nessie/Gravitino, MinIO object store. Pin cross-engine compatibility and unsafe retention/delete operations.
4. Query and warehouse: Trino, DuckDB, StarRocks, ClickHouse, Snowflake/BigQuery/Redshift. Execute representative transaction, concurrency, load-retry and query correctness cases.
5. Orchestration, quality and governance: Airflow/Dagster/Prefect; quality contracts, access revocations and DR drills. Check operational ownership, negative scenarios, release/rollback.

## Sources (starting points, not claim of deployment compatibility)

- https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- https://kafka.apache.org/design/
- https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/fault_tolerance/
- https://iceberg.apache.org/docs/latest/spark-procedures/

Repository skill references remain separately owned. A future L2 pass must pin and verify each engine version, not just link to a latest page.
