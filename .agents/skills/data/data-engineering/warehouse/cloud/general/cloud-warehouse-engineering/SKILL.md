---
name: cloud-warehouse-engineering
description: "Select and architect cloud warehouses across Snowflake, BigQuery, Redshift, Databricks SQL and Synapse using workload semantics, governance and cost."
license: Proprietary
metadata:
  version: "1.1.1"
---

# cloud-warehouse-engineering

## Activation boundary
Use for cross-vendor warehouse selection and architecture. Use engine-specific specialist skills for Snowflake, BigQuery and Redshift implementation details.

## Required context
Workload mix; latency/freshness; concurrency; data volume; SQL dialect; storage; identity; residency; team skills; cost model.

## Production procedure
1. Classify workload: batch ELT, continuous ingestion, BI concurrency, ad hoc federation, ML feature access or operational analytics.
2. Compare Snowflake, BigQuery, Redshift, Databricks SQL and Synapse by ingestion APIs, table/storage semantics, concurrency, isolation and ecosystem.
3. Model cost drivers: compute credits/slots/nodes, storage, scans, egress, serverless refresh, idle time and data sharing.
4. Define partitioning/clustering/sort/distribution and materialized-view strategy only after workload analysis.
5. Compare transaction, MERGE, CDC, time-travel, retention and streaming buffer semantics.
6. Define catalog/governance, IAM, masking, network, audit and regional residency.
7. Run representative query and ingestion tests; compare p95/p99, freshness, cost and failure recovery.
8. Define migration, rollback, portability and exit costs before committing to vendor-specific features.

## Failure modes and recovery
- Benchmark mismatch: use representative concurrency and data distribution.
- Cost surprise: include refresh, idle, egress and serverless costs.
- Dialect lock-in: inventory proprietary SQL and stored procedures.
- Ingestion mismatch: verify API delivery/offset semantics.
- Governance gap: test direct storage and export access, not only warehouse grants.

## Validation and acceptance
- Run workload-specific benchmark and cost model with stated assumptions.
- Test schema evolution, ingestion retry, concurrent queries and restore.
- Verify identity and audit using production roles.
- Record unsupported features and migration cost.

## Output contract
Return weighted decision matrix, reference architecture, cost model, governance design and engine-specific implementation routes.

## Official or primary references
- https://docs.snowflake.com/
- https://docs.cloud.google.com/bigquery/docs
- https://docs.aws.amazon.com/redshift/latest/dg/welcome.html
- https://docs.databricks.com/aws/en/sql/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
