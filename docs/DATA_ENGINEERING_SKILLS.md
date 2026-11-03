# Deep Data Engineering Capability Map

## Scope

29 new narrowly scoped Agent Skills have been added on top of the previous 59 active skills. All are linked through the authoritative YAML graph. For maintained counts run:

    python scripts/report_coverage.py --summary
    python -m capability_map validate
    python scripts/evaluate_graph.py

## Technology routes

| Technology / capability | Specialist skills |
|---|---|
| Flink | `flink-checkpoint-savepoint-recovery`, `flink-sql-event-time-modeling` |
| Beam | `beam-runner-portability` |
| Ray Data | `ray-data-pipeline-engineering` |
| Scala Spark | `spark-scala-job-engineering` |
| Kafka | `kafka-consumer-rebalance-replay`, `kafka-connect-cdc-design` |
| Pulsar | `pulsar-subscription-replay` |
| RabbitMQ | `rabbitmq-consumer-delivery-safety` |
| Kinesis | `kinesis-stream-consumer-recovery` |
| Debezium | `debezium-cdc-bootstrap` |
| Airflow | `airflow-backfill-scheduling` |
| Argo Workflows | `argo-workflows-data-orchestration` |
| Dagster | `dagster-asset-partition-orchestration` |
| Prefect | `prefect-flow-reliability` |
| OpenLineage | `openlineage-metadata-instrumentation` |
| Iceberg | `iceberg-table-schema-partition-evolution`, `iceberg-compaction-retention` |
| Delta Lake | `delta-lake-merge-change-feed` |
| Hudi | `hudi-cow-mor-table-design` |
| Trino | `trino-federated-query-optimization` |
| DuckDB | `duckdb-parquet-transformation` |
| StarRocks | `starrocks-stream-load-transaction`, `starrocks-primary-key-cdc` |
| dbt | `dbt-snapshot-scd2` |
| Dimensional modeling | `dimensional-modeling-grain` |
| Data reliability | `data-observability-freshness-slo` |
| Parquet | `parquet-file-layout-tuning` |
| Architecture | `data-platform-architecture-review` |

## Routing architecture

The root routes to Data. Data routes to the appropriate subdomain. Technology routers distinguish between engines and operations, and local skills.yaml registries choose specific specialist procedures. This avoids putting all instructions into AGENTS.md or reading unrelated engines.

Example:

    catalog/root.yaml
      domains/data/map.yaml
        domains/data/data-engineering/map.yaml
          domains/data/data-engineering/lakehouse/map.yaml
            iceberg
              .../lakehouse/iceberg/skills.yaml
                iceberg-compaction-retention/SKILL.md

StarRocks is additionally available through the database-engineering technology route. Generic ETL and SQL pipelines retain an intentionally narrow fallback when no specialized task matches.

## Engineering quality gates

- Source and sink schema, grain, version and replay contract must be explicit.
- Retryable does not imply idempotent; Kafka/Flink exactly-once guarantees must be evaluated across external sinks.
- Iceberg/Delta/Hudi schema and retention behavior must be verified by actual format/engine releases.
- SQL federation, connector pushdown and multi-table transactions are not universally supported.
- For object storage, never infer atomic file rename from a staging directory.
- Every active skill includes task-specific test scenarios, failure recovery, resource cost and official documentation entry points.
- Do not claim a benchmark, source audit or integration test succeeded without tool evidence.

## Evaluation limitations

Structural validation checks SKILL.md frontmatter, path safety and YAML references. New regression fixtures check 29 specialized matches and near-miss cases, in addition to prior fixtures. They do **not** measure LLM semantic correctness, hallucination rate or token usage across hosts.

## Out of scope / next additions

Business Intelligence, Data Science, the Semantic Layer and selected relational database tools are now mapped to active skills. Other subdomains remain unmapped or mapped-only; consult the live coverage report. A mapped-only status must produce an explicit unavailable/clarification response instead of fabricating a Skill. Add dedicated skills only after reviewing current official interfaces and designing negative, near-miss, multilingual and workload validation cases.

## Typed graph links

Eight additional typed links connect Flink–Kafka, Trino–Iceberg, DuckDB–Parquet, dbt–Airflow, StarRocks–CDC, lineage–Airflow, Iceberg–Spark and data-quality–observability. These edges are read on demand using `capability-map related --route ...`; they do not automatically activate multiple skills or claim cross-engine transactions.

## Additional tooling in unified reference branch

Eleven further Data Engineering skills cover PostgreSQL logical CDC, MySQL binlog CDC, MinIO object storage, Polaris and Lakekeeper Iceberg REST catalogs, DataHub metadata governance, Great Expectations validation, NiFi backpressure, Elasticsearch PIT extraction, ClickHouse MergeTree and SQL physical-plan optimization. These routes are part of `feat/master-reference-platform-data-ai`; see [MASTER_REFERENCE_EXPANSION.md](MASTER_REFERENCE_EXPANSION.md).
