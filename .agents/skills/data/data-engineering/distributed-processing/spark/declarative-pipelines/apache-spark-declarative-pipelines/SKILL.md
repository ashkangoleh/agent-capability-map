---
name: apache-spark-declarative-pipelines
description: "Design declarative batch and streaming pipelines in SQL/Python while separating upstream Spark Declarative Pipelines from Databricks Lakeflow extensions."
license: Proprietary
metadata:
  version: "1.1.1"
---

# apache-spark-declarative-pipelines

## Activation boundary
Use for Spark Declarative Pipelines concepts. Treat Databricks Lakeflow as an implementation with extensions; do not assume proprietary features are portable.

## Required inputs
Runtime/SDP version; platform; SQL/Python; sources/sinks; streaming/triggered mode; catalog; quality/freshness SLO.

## Production workflow
1. Confirm runtime support and platform-specific extensions.
2. Model datasets, dependencies, streaming tables, materialized views and sinks by incremental semantics.
3. Define source mode, checkpoint ownership, schema evolution and event time.
4. Keep transformations deterministic and isolate side effects.
5. Select triggered versus continuous execution from latency and cost.
6. Promote through environments with least-privilege identity and rollback gates.

## Failure modes and recovery
- Unsupported feature: use portable subset or isolate platform-specific code.
- State incompatibility: preserve checkpoints and use supported migration.
- Unexpected full refresh: inspect dependency invalidation.
- Continuous cost spike: switch mode only if freshness allows.
- Quality rule drops valid data: quarantine and alert.

## Validation and evidence
- Test dependency resolution, incremental append, supported updates/deletes, checkpoint recovery and schema evolution.
- Verify AUTO CDC and expectations separately per platform.
- Compare incremental output with bounded full refresh.
- Measure freshness, backlog, duration and compute.

## Output contract
Return portable/platform feature matrix, pipeline graph, state plan and deployment gates.

## Official references
- https://spark.apache.org/docs/latest/
- https://docs.databricks.com/aws/en/ldp/concepts/spark-declarative-pipelines

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
