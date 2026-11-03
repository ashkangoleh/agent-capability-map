---
name: pyspark-pipelines
description: Design or implement an end-to-end PySpark DataFrame or Spark SQL batch pipeline, including contracts, writes, testing, and recovery. Use for complete jobs; not for isolated join-plan or skew diagnosis.
license: Proprietary
metadata:
  version: "1.0.0"
---

# PySpark pipeline implementation

## When to use
Use for an end-to-end Spark job (read, transform, validate, write), not merely a join tuning question. A generic SQL pipeline without Spark stays with data-engineering-implementation.

## Workflow
1. Identify Spark/runtime version, deployment mode, input/output table formats, source guarantees, dataset sizes, grain, target latency, and deployment ownership. Unknown is not zero.
2. Define input/output schemas and null, timezone, event-time, duplicate, and schema evolution contracts.
3. Implement minimal DataFrame or Spark SQL transformations. Prefer built-in functions; justify Python UDFs or custom state.
4. Specify idempotent write/retry semantics for the *actual* sink; do not infer exactly-once from a Spark component.
5. Review logical and physical plans when joins, shuffles, wide aggregations, or window functions are important. For a join-specific issue, select pyspark-joins instead of loading this entire workflow.
6. Validate deterministic sample results, schema, key uniqueness, data reconciliation, failure/retry, and backfill. Include observability for job duration, input/output counts, failures, and cost.
7. Challenge extra layers: require evidence before adding a cache, broker, service, orchestration framework, or persistent intermediate stage.

## Evidence and output
Produce a runnable job or focused patch, configuration assumptions, correctness tests, resource/failure analysis, and a safe rerun/rollback method. Use version-matched official Spark documentation and actual execution plans for tuning claims.

## Stop conditions
If version, sink semantics, or production data contract is missing, state the assumption and avoid asserting deployment safety or guaranteed performance.

## Validation
- [ ] Schema, grain, keys, and date semantics checked.
- [ ] Retry/dedup/backfill behavior demonstrated.
- [ ] Source/sink compatibility and rollout plan verified.
