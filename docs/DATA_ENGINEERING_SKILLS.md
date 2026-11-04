# Deep Data Engineering Capability Map

## Scope

The Data Engineering subtree is maintained through nested YAML maps and local skill registries. The current inventory includes engine-specific procedures and cross-cutting reliability, governance, quality and architecture skills. Treat this document as a capability guide, not a claim that every vendor product is production-certified. For live counts and structural validation run:

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
| CDC sources | `debezium-cdc-bootstrap`, `oracle-goldengate-cdc-operations`, `sqlserver-cdc-change-tracking`, `mongodb-change-streams-cdc` |
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

Business Intelligence, Data Science, the Semantic Layer and selected relational database tools are now mapped to active skills. Some vendor-specific engines and connector families remain mapped-only or are represented by broader interoperability skills. The current high-priority CDC source expansion adds Oracle GoldenGate, SQL Server CDC/Change Tracking and MongoDB Change Streams. Remaining gaps are tracked as separate work items; mapped-only nodes must return explicit unavailable/clarification rather than fabricated expertise.

## Typed graph links

Eight additional typed links connect Flink–Kafka, Trino–Iceberg, DuckDB–Parquet, dbt–Airflow, StarRocks–CDC, lineage–Airflow, Iceberg–Spark and data-quality–observability. These edges are read on demand using `capability-map related --route ...`; they do not automatically activate multiple skills or claim cross-engine transactions.

## Additional tooling in unified reference branch

The reference branch also covers PostgreSQL logical CDC, MySQL binlog CDC, Oracle GoldenGate, SQL Server CDC/Change Tracking, MongoDB Change Streams, MinIO object storage, Polaris and Lakekeeper Iceberg REST catalogs, DataHub metadata governance, Great Expectations validation, NiFi backpressure, Elasticsearch PIT extraction, ClickHouse MergeTree and SQL physical-plan optimization. The canonical integration branch is `pre_release`.
