# Deep Data Engineering Capability Map

## Scope

24 new narrowly scoped Agent Skills have been added on top of the previous 59 active skills. All are linked through the authoritative YAML graph. For maintained counts run:

    python scripts/report_coverage.py --summary
    python -m capability_map validate
    python scripts/evaluate_graph.py

## Technology routes

| Technology / capability | Specialist skills |
|---|---|
| Flink | `flink-checkpoint-savepoint-recovery`, `flink-sql-event-time-modeling` |
| Beam | `beam-runner-portability` |
| Scala Spark | `spark-scala-job-engineering` |
| Kafka | `kafka-consumer-rebalance-replay`, `kafka-connect-cdc-design` |
| Debezium | `debezium-cdc-bootstrap` |
| Airflow | `airflow-backfill-scheduling` |
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

Structural validation checks SKILL.md frontmatter, path safety and YAML references. New regression fixtures check 24 specialized matches and near-miss cases, in addition to prior fixtures. They do **not** measure LLM semantic correctness, hallucination rate or token usage across hosts.

## Out of scope / next additions

Remaining mapped-only nodes include Ray Data, Argo Workflows, other messaging systems and BI/Data Science. A mapped-only status must produce an explicit unavailable/clarification response instead of fabricating a Skill. Add dedicated skills only after reviewing current official interfaces and designing negative, near-miss, multilingual and workload validation cases.
