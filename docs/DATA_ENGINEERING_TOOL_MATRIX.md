# Data Engineering Tool and Concept Matrix

| Capability | Open-source / self-managed | Managed / commercial | Concepts to route |
|---|---|---|---|
| Languages and data frames | Python, SQL, Scala, Java, R, pandas, Polars, PyArrow, DuckDB, Dask, Ray | Managed notebooks and serverless runtimes | typing, memory bounds, vectorization, serialization, native dependencies |
| Ingestion / ELT | Airbyte, dlt, Meltano/Singer, NiFi, Apache Hop | Fivetran, Estuary, cloud-native ingestion | full refresh, cursor incrementals, state, pagination, retries, schema drift |
| CDC | Debezium, Kafka Connect, Flink CDC, WAL/binlog readers | Managed database migration/CDC | snapshot/log handoff, WAL/binlog, GTID/LSN, deletes, ordering, sink semantics |
| Event streaming | Kafka, Pulsar, Redpanda, RabbitMQ | MSK, Confluent Cloud, Kinesis, Pub/Sub, Event Hubs | partitions, ordering, retention, consumer groups, offsets, DLQ, replay |
| Stream processing | Flink, Spark Structured Streaming, Beam, Kafka Streams | Dataflow and managed runtimes | event time, watermarks, windows, late events, state, checkpoints, backpressure |
| Distributed compute | Spark, Flink, Beam, Hadoop, Ray | EMR, Dataproc, managed Spark | shuffle, skew, spill, adaptive execution, broadcast joins, isolation |
| Orchestration | Airflow, Dagster, Prefect, Argo, Kestra, Temporal, Flyte, Kubeflow | Managed workflow services | DAG/assets, triggers, retries, backfills, durable execution |
| Transformation | dbt, SQLMesh, Dataform, Spark/Flink SQL, Hop | dbt Cloud, warehouse-native | ETL/ELT, incremental models, SCD, contracts, snapshots, restatement |
| File / interchange | Parquet, ORC, Avro, Protobuf, JSON Schema, Arrow IPC/Flight, Substrait | Vendor-optimized formats | row groups, codecs, logical types, compatibility, query-plan exchange |
| Lakehouse | Iceberg, Delta Lake, Hudi, Paimon, DuckLake | Managed lakehouse implementations | snapshots, manifests, commits, deletes, schema evolution, compaction |
| Catalogs | Hive Metastore, Polaris, Nessie, Lakekeeper, Gravitino, DataHub, OpenMetadata | Glue Catalog, Unity Catalog | REST catalog, namespaces, credential vending, lineage, ownership |
| Storage / NoSQL | MinIO, HDFS, HBase, Ceph, Cassandra, MongoDB, Redis | S3, GCS, ADLS and managed NoSQL | durability, replication, TTL, tombstones, lifecycle, recovery |
| Warehouses / federation | Trino, Presto, Dremio, StarRocks, Doris, ClickHouse | Snowflake, BigQuery, Redshift, Databricks SQL, Synapse/Fabric | MPP, pushdown, plans, sort/distribution keys, concurrency, cost |
| Real-time OLAP / search | Pinot, Druid, Elasticsearch, OpenSearch | Managed search/OLAP | segments, shards, indexes, refresh, upsert, retention |
| Quality / observability | GX, Soda, Deequ, Pandera, dbt tests, Elementary, OpenLineage | Commercial data observability | contracts, profiling, reconciliation, freshness, volume, schema, lineage |
| Governance / security | Ranger, ODCS, OpenMetadata, DataHub | Lake Formation, Unity Catalog | RBAC/ABAC, masking, PII, purpose limitation, retention, audit |
| Serving / activation | REST, GraphQL, Arrow Flight, materialized read models | Hightouch, Census | reverse ETL, rate limits, cache freshness, API contracts, tenant isolation |

## Production invariants

Grain and keys; event versus processing time; idempotency and replay; schema compatibility; skew and hot keys; small files and compaction; catalog versus object-store security; lineage and ownership; freshness SLOs; RPO/RTO; unit cost; source/sink transaction boundaries. A scheduler is not a compute engine, a CDC connector is not a universal guarantee, a catalog is not object storage, and exactly-once is an end-to-end claim.

No finite list can include every proprietary connector and vendor product. This matrix covers major current ecosystems and is designed for extension. Verify deployed versions and contracts before implementation.
