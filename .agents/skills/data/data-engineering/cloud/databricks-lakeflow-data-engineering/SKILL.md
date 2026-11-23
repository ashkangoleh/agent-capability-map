---
name: databricks-lakeflow-data-engineering
description: "Engineer Databricks Lakeflow Connect, pipelines and Jobs with Unity Catalog, SDP boundaries and operational controls."
license: Proprietary
metadata:
  version: "1.1.1"
---

# databricks-lakeflow-data-engineering

## Activation boundary
Use for Databricks Lakeflow. Distinguish Lakeflow Connect, Pipelines, Jobs and upstream Spark Declarative Pipelines.

## Required inputs
Cloud/workspace; runtime; Unity Catalog; connector limits; pipeline mode; compute policy; quality/freshness SLO.

## Production workflow
1. Choose Lakeflow Connect where connector semantics meet requirements.
2. Use Lakeflow Pipelines for declarative datasets and Jobs for surrounding orchestration.
3. Separate upstream SDP features from Lakeflow extensions such as AUTO CDC and expectations.
4. Define streaming tables, materialized views, flows and sinks by incremental semantics.
5. Use Unity Catalog for ownership, privileges and lineage.
6. Promote version-controlled code with least-privilege identity; monitor event logs and cost.

## Failure modes and recovery
- Connector lag: inspect source limits and destination backpressure.
- Unexpected full refresh: inspect dependency invalidation.
- Permission failure: validate pipeline identity and catalog grants.
- Continuous-mode cost growth: use triggered mode only if freshness permits.
- Partial publication: inspect event log/table history before rerun.

## Validation and evidence
- Test incremental append, updates/deletes, AUTO CDC where supported and checkpoint recovery.
- Test environment promotion and compare with full refresh.
- Measure freshness, backlog, duration, quality failures and cost.

## Output contract
Return product boundary, pipeline design, identity model, deployment and monitoring gates.

## Official references
- https://docs.databricks.com/aws/en/data-engineering
- https://docs.databricks.com/aws/en/ldp/concepts/spark-declarative-pipelines

## Independent operational verification
For deployable changes or incidents, read [specialist acceptance and recovery evidence](references/acceptance-and-recovery.md) on demand. Its specific fault/restore oracle is a review gate, not proof of execution or permission to modify a system.
