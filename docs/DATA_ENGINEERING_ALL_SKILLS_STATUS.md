# Data Engineering — all 123 canonical specialist packages

Snapshot commit before this report: `cbd033f33fb7b2f15369c8a4257edb6651978a36`. Branch: `pre_release`. Source of truth remains the live graph and `scripts/audit_data_engineering_skills.py`. The table below is **not** a production-certification report.

## Inventory interpretation

- **123 / 123** have an independent linked on-demand acceptance/recovery reference, confirmed by Git tree path matching.
- **35 family-specific verification profiles**; one profile can apply to several skills. This is structured fault-injection planning, not 123 independently witnessed recovery experiments.
- **3** packages contain at least one local Python script and **2** have an `examples/` directory. File presence says nothing about successful real-engine execution. Existing repository-wide examples outside the skill package are not included in this count.
- Every skill is at **L1_REFERENCE_PRESENT** but L2 engine-version compatibility and real L3/L4 acceptance **remain unverified**.
- The 41-domain router, 438 total canonical skills, 408 total roles, root ID/trigger paths and max-five scope policy were not changed in this tranche.

## Per-skill matrix

| Skill | Family path | Profile | Script in package | Example in package | Evidence state |
|---|---|---|---|---|---|
| [`data-mesh-data-product-architecture`](../.agents/skills/data/data-engineering/architecture/data-mesh-data-product-architecture/SKILL.md) | `architecture` | `architecture` | No | No | L1 only |
| [`medallion-lambda-kappa-architecture`](../.agents/skills/data/data-engineering/architecture/medallion-lambda-kappa-architecture/SKILL.md) | `architecture` | `architecture` | No | No | L1 only |
| [`multi-engine-data-platform-interoperability`](../.agents/skills/data/data-engineering/architecture/multi-engine-data-platform-interoperability/SKILL.md) | `architecture` | `architecture` | No | No | L1 only |
| [`debezium-cdc-bootstrap`](../.agents/skills/data/data-engineering/batch-ingestion/cdc/debezium-cdc-bootstrap/SKILL.md) | `batch-ingestion/cdc` | `batch-ingestion/cdc` | No | No | L1 only |
| [`kafka-connect-cdc-design`](../.agents/skills/data/data-engineering/batch-ingestion/cdc/kafka-connect-cdc-design/SKILL.md) | `batch-ingestion/cdc` | `batch-ingestion/cdc` | No | No | L1 only |
| [`mongodb-change-streams-cdc`](../.agents/skills/data/data-engineering/batch-ingestion/cdc/mongodb-change-streams-cdc/SKILL.md) | `batch-ingestion/cdc` | `batch-ingestion/cdc` | No | No | L1 only |
| [`oracle-goldengate-cdc-operations`](../.agents/skills/data/data-engineering/batch-ingestion/cdc/oracle-goldengate-cdc-operations/SKILL.md) | `batch-ingestion/cdc` | `batch-ingestion/cdc` | No | No | L1 only |
| [`sqlserver-cdc-change-tracking`](../.agents/skills/data/data-engineering/batch-ingestion/cdc/sqlserver-cdc-change-tracking/SKILL.md) | `batch-ingestion/cdc` | `batch-ingestion/cdc` | No | No | L1 only |
| [`elasticsearch-pit-bulk-extraction`](../.agents/skills/data/data-engineering/batch-ingestion/elasticsearch/elasticsearch-pit-bulk-extraction/SKILL.md) | `batch-ingestion/elasticsearch` | `batch-ingestion/elasticsearch` | No | No | L1 only |
| [`nifi-flowfile-backpressure-operations`](../.agents/skills/data/data-engineering/batch-ingestion/nifi/nifi-flowfile-backpressure-operations/SKILL.md) | `batch-ingestion/nifi` | `batch-ingestion` | No | No | L1 only |
| [`parquet-file-layout-tuning`](../.agents/skills/data/data-engineering/batch-ingestion/parquet/parquet-file-layout-tuning/SKILL.md) | `batch-ingestion/parquet` | `batch-ingestion` | No | No | L1 only |
| [`pipeline-backfill-recovery`](../.agents/skills/data/data-engineering/batch-ingestion/recovery/pipeline-backfill-recovery/SKILL.md) | `batch-ingestion/recovery` | `batch-ingestion/recovery` | No | No | L1 only |
| [`aws-data-platform-engineering`](../.agents/skills/data/data-engineering/cloud/aws-data-platform-engineering/SKILL.md) | `cloud` | `cloud` | No | No | L1 only |
| [`azure-data-platform-engineering`](../.agents/skills/data/data-engineering/cloud/azure-data-platform-engineering/SKILL.md) | `cloud` | `cloud` | No | No | L1 only |
| [`databricks-lakeflow-data-engineering`](../.agents/skills/data/data-engineering/cloud/databricks-lakeflow-data-engineering/SKILL.md) | `cloud` | `cloud` | No | No | L1 only |
| [`gcp-data-platform-engineering`](../.agents/skills/data/data-engineering/cloud/gcp-data-platform-engineering/SKILL.md) | `cloud` | `cloud` | No | No | L1 only |
| [`oci-data-platform-engineering`](../.agents/skills/data/data-engineering/cloud/oci-data-platform-engineering/SKILL.md) | `cloud` | `cloud` | No | No | L1 only |
| [`data-migration-cutover-reconciliation`](../.agents/skills/data/data-engineering/data-migration/data-migration-cutover-reconciliation/SKILL.md) | `data-migration` | `data-migration` | No | No | L1 only |
| [`data-pipeline-testing-ci-cd`](../.agents/skills/data/data-engineering/dataops/data-pipeline-testing-ci-cd/SKILL.md) | `dataops` | `dataops` | No | No | L1 only |
| [`data-schema-migration-release-management`](../.agents/skills/data/data-engineering/dataops/data-schema-migration-release-management/SKILL.md) | `dataops` | `dataops` | No | No | L1 only |
| [`beam-runner-portability`](../.agents/skills/data/data-engineering/distributed-processing/beam/beam-runner-portability/SKILL.md) | `distributed-processing/beam` | `distributed-processing` | No | No | L1 only |
| [`dask-distributed-data-engineering`](../.agents/skills/data/data-engineering/distributed-processing/dask/dask-distributed-data-engineering/SKILL.md) | `distributed-processing/dask` | `distributed-processing` | No | No | L1 only |
| [`datafusion-arrow-query-engine`](../.agents/skills/data/data-engineering/distributed-processing/datafusion/datafusion-arrow-query-engine/SKILL.md) | `distributed-processing/datafusion` | `distributed-processing` | No | No | L1 only |
| [`flink-checkpoint-savepoint-recovery`](../.agents/skills/data/data-engineering/distributed-processing/flink/flink-checkpoint-savepoint-recovery/SKILL.md) | `distributed-processing/flink` | `distributed-processing/flink` | No | No | L1 only |
| [`flink-sql-event-time-modeling`](../.agents/skills/data/data-engineering/distributed-processing/flink/flink-sql-event-time-modeling/SKILL.md) | `distributed-processing/flink` | `distributed-processing/flink` | No | No | L1 only |
| [`ray-data-pipeline-engineering`](../.agents/skills/data/data-engineering/distributed-processing/ray/ray-data-pipeline-engineering/SKILL.md) | `distributed-processing/ray` | `distributed-processing` | No | No | L1 only |
| [`apache-spark-declarative-pipelines`](../.agents/skills/data/data-engineering/distributed-processing/spark/declarative-pipelines/apache-spark-declarative-pipelines/SKILL.md) | `distributed-processing/spark/declarative-pipelines` | `distributed-processing/spark` | No | No | L1 only |
| [`pyspark-project-bootstrap`](../.agents/skills/data/data-engineering/distributed-processing/spark/pyspark/pyspark-project-bootstrap/SKILL.md) | `distributed-processing/spark/pyspark` | `distributed-processing/spark` | No | No | L1 only |
| [`pyspark-transformations`](../.agents/skills/data/data-engineering/distributed-processing/spark/pyspark/pyspark-transformations/SKILL.md) | `distributed-processing/spark/pyspark` | `distributed-processing/spark` | No | No | L1 only |
| [`spark-structured-streaming`](../.agents/skills/data/data-engineering/distributed-processing/spark/pyspark/spark-structured-streaming/SKILL.md) | `distributed-processing/spark/pyspark` | `distributed-processing/spark` | No | No | L1 only |
| [`spark-performance-diagnostics`](../.agents/skills/data/data-engineering/distributed-processing/spark/runtime/spark-performance-diagnostics/SKILL.md) | `distributed-processing/spark/runtime` | `distributed-processing/spark` | No | No | L1 only |
| [`spark-scala-job-engineering`](../.agents/skills/data/data-engineering/distributed-processing/spark/scala/spark-scala-job-engineering/SKILL.md) | `distributed-processing/spark/scala` | `distributed-processing/spark` | No | No | L1 only |
| [`spark-sql-engineering`](../.agents/skills/data/data-engineering/distributed-processing/spark/sql/spark-sql-engineering/SKILL.md) | `distributed-processing/spark/sql` | `distributed-processing/spark` | No | No | L1 only |
| [`arrow-flight-substrait-interoperability`](../.agents/skills/data/data-engineering/formats/arrow-flight-substrait-interoperability/SKILL.md) | `formats` | `formats` | No | No | L1 only |
| [`avro-protobuf-schema-engineering`](../.agents/skills/data/data-engineering/formats/avro-protobuf-schema-engineering/SKILL.md) | `formats` | `formats` | No | No | L1 only |
| [`parquet-orc-columnar-storage`](../.agents/skills/data/data-engineering/formats/parquet-orc-columnar-storage/SKILL.md) | `formats` | `formats` | No | No | L1 only |
| [`bitemporal-event-data-modeling`](../.agents/skills/data/data-engineering/foundations/bitemporal-event-data-modeling/SKILL.md) | `foundations` | `foundations` | No | No | L1 only |
| [`data-engineering-foundations-lifecycle`](../.agents/skills/data/data-engineering/foundations/data-engineering-foundations-lifecycle/SKILL.md) | `foundations` | `foundations` | No | No | L1 only |
| [`data-engineering-implementation`](../.agents/skills/data/data-engineering/foundations/data-engineering-implementation/SKILL.md) | `foundations` | `foundations` | No | No | L1 only |
| [`data-vault-2-modeling`](../.agents/skills/data/data-engineering/foundations/data-vault-2-modeling/SKILL.md) | `foundations` | `foundations` | No | No | L1 only |
| [`enterprise-data-modeling-pattern-selection`](../.agents/skills/data/data-engineering/foundations/enterprise-data-modeling-pattern-selection/SKILL.md) | `foundations` | `foundations` | No | No | L1 only |
| [`python-data-engineering-runtime-performance`](../.agents/skills/data/data-engineering/foundations/python-data-engineering-runtime-performance/SKILL.md) | `foundations` | `foundations` | No | No | L1 only |
| [`data-access-control-masking`](../.agents/skills/data/data-engineering/governance/data-access-control-masking/SKILL.md) | `governance` | `governance` | No | No | L1 only |
| [`data-contract-odcs-engineering`](../.agents/skills/data/data-engineering/governance/data-contract-odcs-engineering/SKILL.md) | `governance` | `governance` | No | No | L1 only |
| [`data-retention-lifecycle-governance`](../.agents/skills/data/data-engineering/governance/data-retention-lifecycle-governance/SKILL.md) | `governance` | `governance` | No | No | L1 only |
| [`openmetadata-catalog-operations`](../.agents/skills/data/data-engineering/governance/openmetadata-catalog-operations/SKILL.md) | `governance` | `governance` | No | No | L1 only |
| [`privacy-preserving-data-engineering`](../.agents/skills/data/data-engineering/governance/privacy-preserving-data-engineering/SKILL.md) | `governance` | `governance` | No | No | L1 only |
| [`airbyte-connector-operations`](../.agents/skills/data/data-engineering/ingestion/airbyte-connector-operations/SKILL.md) | `ingestion` | `ingestion` | No | No | L1 only |
| [`apache-seatunnel-data-integration`](../.agents/skills/data/data-engineering/ingestion/apache-seatunnel-data-integration/SKILL.md) | `ingestion` | `ingestion` | No | No | L1 only |
| [`api-ingestion-pagination-rate-limits`](../.agents/skills/data/data-engineering/ingestion/api-ingestion-pagination-rate-limits/SKILL.md) | `ingestion` | `ingestion` | No | No | L1 only |
| [`dlt-pipeline-engineering`](../.agents/skills/data/data-engineering/ingestion/dlt-pipeline-engineering/SKILL.md) | `ingestion` | `ingestion` | No | No | L1 only |
| [`file-ingestion-landing-zone`](../.agents/skills/data/data-engineering/ingestion/file-ingestion-landing-zone/SKILL.md) | `ingestion` | `ingestion` | No | No | L1 only |
| [`flink-cdc-source-sink-engineering`](../.agents/skills/data/data-engineering/ingestion/flink-cdc-source-sink-engineering/SKILL.md) | `ingestion` | `ingestion` | No | No | L1 only |
| [`managed-elt-fivetran-estuary-operations`](../.agents/skills/data/data-engineering/ingestion/managed-elt-fivetran-estuary-operations/SKILL.md) | `ingestion` | `ingestion` | No | No | L1 only |
| [`meltano-singer-elt-engineering`](../.agents/skills/data/data-engineering/ingestion/meltano-singer-elt-engineering/SKILL.md) | `ingestion` | `ingestion` | No | No | L1 only |
| [`apache-paimon-streaming-lakehouse`](../.agents/skills/data/data-engineering/lakehouse/apache-paimon-streaming-lakehouse/SKILL.md) | `lakehouse` | `lakehouse` | No | No | L1 only |
| [`gravitino-federated-catalog-operations`](../.agents/skills/data/data-engineering/lakehouse/catalogs/gravitino/gravitino-federated-catalog-operations/SKILL.md) | `lakehouse/catalogs/gravitino` | `lakehouse/catalogs` | No | No | L1 only |
| [`iceberg-rest-catalog-operations`](../.agents/skills/data/data-engineering/lakehouse/catalogs/iceberg-rest/iceberg-rest-catalog-operations/SKILL.md) | `lakehouse/catalogs/iceberg-rest` | `lakehouse/catalogs` | No | No | L1 only |
| [`lakekeeper-iceberg-catalog-operations`](../.agents/skills/data/data-engineering/lakehouse/catalogs/lakekeeper/lakekeeper-iceberg-catalog-operations/SKILL.md) | `lakehouse/catalogs/lakekeeper` | `lakehouse/catalogs` | No | No | L1 only |
| [`nessie-versioned-catalog-operations`](../.agents/skills/data/data-engineering/lakehouse/catalogs/nessie/nessie-versioned-catalog-operations/SKILL.md) | `lakehouse/catalogs/nessie` | `lakehouse/catalogs` | No | No | L1 only |
| [`polaris-iceberg-catalog-operations`](../.agents/skills/data/data-engineering/lakehouse/catalogs/polaris/polaris-iceberg-catalog-operations/SKILL.md) | `lakehouse/catalogs/polaris` | `lakehouse/catalogs` | No | No | L1 only |
| [`delta-lake-merge-change-feed`](../.agents/skills/data/data-engineering/lakehouse/delta/delta-lake-merge-change-feed/SKILL.md) | `lakehouse/delta` | `lakehouse` | No | No | L1 only |
| [`ducklake-lakehouse-format-engineering`](../.agents/skills/data/data-engineering/lakehouse/ducklake/ducklake-lakehouse-format-engineering/SKILL.md) | `lakehouse/ducklake` | `lakehouse` | No | No | L1 only |
| [`hudi-cow-mor-table-design`](../.agents/skills/data/data-engineering/lakehouse/hudi/hudi-cow-mor-table-design/SKILL.md) | `lakehouse/hudi` | `lakehouse` | No | No | L1 only |
| [`iceberg-compaction-retention`](../.agents/skills/data/data-engineering/lakehouse/iceberg/iceberg-compaction-retention/SKILL.md) | `lakehouse/iceberg` | `lakehouse/iceberg` | Present, not engine-verified | Present, not engine-verified | L1 only |
| [`iceberg-table-schema-partition-evolution`](../.agents/skills/data/data-engineering/lakehouse/iceberg/iceberg-table-schema-partition-evolution/SKILL.md) | `lakehouse/iceberg` | `lakehouse/iceberg` | Present, not engine-verified | Present, not engine-verified | L1 only |
| [`lakehouse-catalog-ecosystem-interoperability`](../.agents/skills/data/data-engineering/lakehouse/lakehouse-catalog-ecosystem-interoperability/SKILL.md) | `lakehouse` | `lakehouse` | No | No | L1 only |
| [`minio-s3-object-storage-reliability`](../.agents/skills/data/data-engineering/lakehouse/object-storage/minio-s3-object-storage-reliability/SKILL.md) | `lakehouse/object-storage` | `lakehouse` | No | No | L1 only |
| [`open-table-format-selection`](../.agents/skills/data/data-engineering/lakehouse/open-table-format-selection/SKILL.md) | `lakehouse` | `lakehouse` | No | No | L1 only |
| [`apache-fluss-streaming-storage`](../.agents/skills/data/data-engineering/lakehouse/streaming-storage/apache-fluss-streaming-storage/SKILL.md) | `lakehouse/streaming-storage` | `lakehouse` | No | No | L1 only |
| [`kafka-consumer-rebalance-replay`](../.agents/skills/data/data-engineering/messaging/kafka/kafka-consumer-rebalance-replay/SKILL.md) | `messaging/kafka` | `messaging/kafka` | No | No | L1 only |
| [`kafka-streaming-reliability`](../.agents/skills/data/data-engineering/messaging/kafka/kafka-streaming-reliability/SKILL.md) | `messaging/kafka` | `messaging/kafka` | No | No | L1 only |
| [`kinesis-stream-consumer-recovery`](../.agents/skills/data/data-engineering/messaging/kinesis/kinesis-stream-consumer-recovery/SKILL.md) | `messaging/kinesis` | `messaging` | No | No | L1 only |
| [`nats-jetstream-data-streaming`](../.agents/skills/data/data-engineering/messaging/nats/nats-jetstream-data-streaming/SKILL.md) | `messaging/nats` | `messaging` | No | No | L1 only |
| [`pulsar-subscription-replay`](../.agents/skills/data/data-engineering/messaging/pulsar/pulsar-subscription-replay/SKILL.md) | `messaging/pulsar` | `messaging` | No | No | L1 only |
| [`rabbitmq-consumer-delivery-safety`](../.agents/skills/data/data-engineering/messaging/rabbitmq/rabbitmq-consumer-delivery-safety/SKILL.md) | `messaging/rabbitmq` | `messaging` | No | No | L1 only |
| [`data-observability-freshness-slo`](../.agents/skills/data/data-engineering/observability/slo/data-observability-freshness-slo/SKILL.md) | `observability/slo` | `observability` | No | No | L1 only |
| [`airflow-backfill-scheduling`](../.agents/skills/data/data-engineering/orchestration/airflow/airflow-backfill-scheduling/SKILL.md) | `orchestration/airflow` | `orchestration` | No | No | L1 only |
| [`airflow-dag-engineering`](../.agents/skills/data/data-engineering/orchestration/airflow/airflow-dag-engineering/SKILL.md) | `orchestration/airflow` | `orchestration` | No | No | L1 only |
| [`argo-workflows-data-orchestration`](../.agents/skills/data/data-engineering/orchestration/argo-workflows/argo-workflows-data-orchestration/SKILL.md) | `orchestration/argo-workflows` | `orchestration` | No | No | L1 only |
| [`dagster-asset-partition-orchestration`](../.agents/skills/data/data-engineering/orchestration/dagster/dagster-asset-partition-orchestration/SKILL.md) | `orchestration/dagster` | `orchestration` | No | No | L1 only |
| [`data-orchestration-platform-selection`](../.agents/skills/data/data-engineering/orchestration/data-orchestration-platform-selection/SKILL.md) | `orchestration` | `orchestration` | No | No | L1 only |
| [`flyte-kubeflow-pipeline-orchestration`](../.agents/skills/data/data-engineering/orchestration/flyte-kubeflow-pipeline-orchestration/SKILL.md) | `orchestration` | `orchestration` | No | No | L1 only |
| [`kestra-data-orchestration`](../.agents/skills/data/data-engineering/orchestration/kestra-data-orchestration/SKILL.md) | `orchestration` | `orchestration` | No | No | L1 only |
| [`prefect-flow-reliability`](../.agents/skills/data/data-engineering/orchestration/prefect/prefect-flow-reliability/SKILL.md) | `orchestration/prefect` | `orchestration` | No | No | L1 only |
| [`temporal-durable-workflows`](../.agents/skills/data/data-engineering/orchestration/temporal-durable-workflows/SKILL.md) | `orchestration` | `orchestration` | No | No | L1 only |
| [`data-platform-cost-capacity-engineering`](../.agents/skills/data/data-engineering/performance/data-platform-cost-capacity-engineering/SKILL.md) | `performance` | `performance` | No | No | L1 only |
| [`distributed-query-engine-performance`](../.agents/skills/data/data-engineering/performance/distributed-query-engine-performance/SKILL.md) | `performance` | `performance` | No | No | L1 only |
| [`deequ-data-quality-at-scale`](../.agents/skills/data/data-engineering/quality/deequ-data-quality-at-scale/SKILL.md) | `quality` | `quality` | No | No | L1 only |
| [`pandera-dataframe-validation`](../.agents/skills/data/data-engineering/quality/pandera-dataframe-validation/SKILL.md) | `quality` | `quality` | No | No | L1 only |
| [`soda-data-quality-engineering`](../.agents/skills/data/data-engineering/quality/soda-data-quality-engineering/SKILL.md) | `quality` | `quality` | No | No | L1 only |
| [`data-platform-backup-disaster-recovery`](../.agents/skills/data/data-engineering/reliability/data-platform-backup-disaster-recovery/SKILL.md) | `reliability` | `reliability` | No | No | L1 only |
| [`end-to-end-pipeline-reliability`](../.agents/skills/data/data-engineering/reliability/end-to-end-pipeline-reliability/SKILL.md) | `reliability` | `reliability` | No | No | L1 only |
| [`transactional-outbox-dlq-replay`](../.agents/skills/data/data-engineering/reliability/transactional-outbox-dlq-replay/SKILL.md) | `reliability` | `reliability` | No | No | L1 only |
| [`data-serving-api-design`](../.agents/skills/data/data-engineering/serving/data-serving-api-design/SKILL.md) | `serving` | `serving` | No | No | L1 only |
| [`reverse-etl-data-activation`](../.agents/skills/data/data-engineering/serving/reverse-etl-data-activation/SKILL.md) | `serving` | `serving` | No | No | L1 only |
| [`cloud-object-storage-data-lake-operations`](../.agents/skills/data/data-engineering/storage/cloud-object-storage-data-lake-operations/SKILL.md) | `storage` | `storage` | No | No | L1 only |
| [`hadoop-hdfs-hive-yarn-operations`](../.agents/skills/data/data-engineering/storage/hadoop-hdfs-hive-yarn-operations/SKILL.md) | `storage` | `storage` | No | No | L1 only |
| [`hbase-distributed-storage`](../.agents/skills/data/data-engineering/storage/hbase-distributed-storage/SKILL.md) | `storage` | `storage` | No | No | L1 only |
| [`nosql-data-platform-integration`](../.agents/skills/data/data-engineering/storage/nosql-data-platform-integration/SKILL.md) | `storage` | `storage` | No | No | L1 only |
| [`end-to-end-delivery-semantics`](../.agents/skills/data/data-engineering/streaming/end-to-end-delivery-semantics/SKILL.md) | `streaming` | `streaming` | Present, not engine-verified | No | L1 only |
| [`kafka-streams-ksqldb-engineering`](../.agents/skills/data/data-engineering/streaming/kafka-streams-ksqldb-engineering/SKILL.md) | `streaming` | `streaming` | No | No | L1 only |
| [`redpanda-event-streaming`](../.agents/skills/data/data-engineering/streaming/redpanda-event-streaming/SKILL.md) | `streaming` | `streaming` | No | No | L1 only |
| [`schema-registry-compatibility`](../.agents/skills/data/data-engineering/streaming/schema-registry-compatibility/SKILL.md) | `streaming` | `streaming` | No | No | L1 only |
| [`materialize-streaming-sql-engineering`](../.agents/skills/data/data-engineering/streaming/sql-engines/materialize/materialize-streaming-sql-engineering/SKILL.md) | `streaming/sql-engines/materialize` | `streaming/sql-engines` | No | No | L1 only |
| [`risingwave-streaming-sql-engineering`](../.agents/skills/data/data-engineering/streaming/sql-engines/risingwave/risingwave-streaming-sql-engineering/SKILL.md) | `streaming/sql-engines/risingwave` | `streaming/sql-engines` | No | No | L1 only |
| [`streaming-event-time-watermark-window`](../.agents/skills/data/data-engineering/streaming/streaming-event-time-watermark-window/SKILL.md) | `streaming` | `streaming` | No | No | L1 only |
| [`apache-hop-etl-operations`](../.agents/skills/data/data-engineering/transformation/apache-hop-etl-operations/SKILL.md) | `transformation` | `transformation` | No | No | L1 only |
| [`dataform-warehouse-transformations`](../.agents/skills/data/data-engineering/transformation/dataform-warehouse-transformations/SKILL.md) | `transformation` | `transformation` | No | No | L1 only |
| [`sqlmesh-stateful-transformations`](../.agents/skills/data/data-engineering/transformation/sqlmesh-stateful-transformations/SKILL.md) | `transformation` | `transformation` | No | No | L1 only |
| [`unstructured-data-ingestion-engineering`](../.agents/skills/data/data-engineering/unstructured/unstructured-data-ingestion-engineering/SKILL.md) | `unstructured` | `unstructured` | No | No | L1 only |
| [`apache-doris-olap-engineering`](../.agents/skills/data/data-engineering/warehouse/apache-doris-olap-engineering/SKILL.md) | `warehouse` | `warehouse` | No | No | L1 only |
| [`apache-pinot-druid-realtime-olap`](../.agents/skills/data/data-engineering/warehouse/apache-pinot-druid-realtime-olap/SKILL.md) | `warehouse` | `warehouse` | No | No | L1 only |
| [`clickhouse-mergetree-operability`](../.agents/skills/data/data-engineering/warehouse/clickhouse/clickhouse-mergetree-operability/SKILL.md) | `warehouse/clickhouse` | `warehouse` | No | No | L1 only |
| [`bigquery-data-platform-engineering`](../.agents/skills/data/data-engineering/warehouse/cloud/bigquery/bigquery-data-platform-engineering/SKILL.md) | `warehouse/cloud/bigquery` | `warehouse/cloud` | No | No | L1 only |
| [`cloud-warehouse-engineering`](../.agents/skills/data/data-engineering/warehouse/cloud/general/cloud-warehouse-engineering/SKILL.md) | `warehouse/cloud/general` | `warehouse/cloud` | No | No | L1 only |
| [`redshift-data-platform-engineering`](../.agents/skills/data/data-engineering/warehouse/cloud/redshift/redshift-data-platform-engineering/SKILL.md) | `warehouse/cloud/redshift` | `warehouse/cloud` | No | No | L1 only |
| [`snowflake-data-platform-engineering`](../.agents/skills/data/data-engineering/warehouse/cloud/snowflake/snowflake-data-platform-engineering/SKILL.md) | `warehouse/cloud/snowflake` | `warehouse/cloud` | No | No | L1 only |
| [`dremio-presto-query-federation`](../.agents/skills/data/data-engineering/warehouse/dremio-presto-query-federation/SKILL.md) | `warehouse` | `warehouse` | No | No | L1 only |
| [`duckdb-parquet-transformation`](../.agents/skills/data/data-engineering/warehouse/duckdb/duckdb-parquet-transformation/SKILL.md) | `warehouse/duckdb` | `warehouse` | No | No | L1 only |
| [`opensearch-analytics-index-engineering`](../.agents/skills/data/data-engineering/warehouse/opensearch-analytics-index-engineering/SKILL.md) | `warehouse` | `warehouse` | No | No | L1 only |
| [`starrocks-olap-warehouse-engineering`](../.agents/skills/data/data-engineering/warehouse/starrocks/starrocks-olap-warehouse-engineering/SKILL.md) | `warehouse/starrocks` | `warehouse/starrocks` | No | No | L1 only |
| [`trino-federated-query-optimization`](../.agents/skills/data/data-engineering/warehouse/trino/trino-federated-query-optimization/SKILL.md) | `warehouse/trino` | `warehouse/trino` | No | No | L1 only |

## Production acceptance checklist for each skill

1. Identify an exact deployed engine/connector version, query/API compatibility and maintained official documentation; no generic `latest` assumption.
2. Supply a true runnable example for that skill when implementation is involved. Include a fixed input, expected output and negative cases, not a copy of the same generic script.
3. Execute a bounded fault experiment and reconcile full source-to-sink data and external side effects in an isolated environment.
4. Verify safe rollback or recovery with actual retained data, permissions and recorded limits. Unknown or unsafe results block signoff.
5. Compare agent output against a base agent through blinded independent scoring; quantify correctness, unsafe claims, p95 latency and cost.
6. Mark each unrun or irrelevant test `UNKNOWN` or `N/A with reason`, never `PASS`.

## Priority for executable second-pass work

- CDC and ingestion: snapshot/stream handoff, retention-window loss, cursor expiration, deletes and schema evolution.
- Kafka/Flink/Spark streaming: checkpoint/ack, rebalances, broker retention, state migration and sink idempotency.
- Lakehouse/catalogs: snapshot preservation, field-ID history, concurrent commit, catalog vending and object-store recovery.
- Trino/StarRocks/DuckDB and cloud warehouses: transaction reconciliation, type fidelity, unknown load outcome and p99 query behavior.
- Orchestration/quality/governance: time intervals and DST, idempotent historical backfills, access revocation and evidence quality.

**Engineering conclusion:** this effort closes an important structural gap but is not sufficient to call the entire Data Engineering portfolio best-in-class. Per-engine, release-pinned integration evidence remains the next quality gate.
