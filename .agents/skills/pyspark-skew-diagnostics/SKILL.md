---
name: pyspark-skew-diagnostics
description: Diagnose and mitigate verified Spark/PySpark join or aggregation skew using per-task metrics, key distributions, and Spark-version-aware options. Do not activate just because a user mentions Spark.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Diagnose Spark data skew

## When to use
Use when evidence suggests hot keys, disproportionate partitions, stragglers, or uneven shuffle task sizes. A generic slow query without these symptoms should start with pyspark-joins or pyspark-pipelines, depending on the deliverable.

## Workflow
1. Obtain Spark/runtime version and relevant Spark UI stages, physical plan, task-duration distribution, shuffle read/write sizes, spill, and partition statistics.
2. Establish whether the bottleneck is skew versus total data volume, bad join cardinality, slow external I/O, memory pressure, or resource contention.
3. Inspect key-frequency distribution, null/sentinel keys, partition counts, and whether one key dominates a join or aggregation.
4. Try the lowest-risk supported approach first: correct keys/filters, AQE skew handling where applicable, appropriately sized partitions, or moving avoidable work out of shuffles.
5. Consider salting or heavy-key splitting only when measured imbalance persists and correctness/cost trade-offs are understood. Require deterministic recombination and regression tests.
6. Compare before/after p50/p95/max task times, shuffle bytes, spill, job latency, output equality, and cloud/resource cost using the same representative workload.
7. Record revert criteria and operational impact.

## Evidence and output
Provide a falsifiable diagnosis, minimal remediation, observed-versus-expected metrics, correctness tests, and a rollback. Quote neither universal skew thresholds nor guaranteed gains without source and measurement.

## Stop conditions
If no stage/task evidence exists, provide a measurement plan and mark skew as a hypothesis; do not present a diagnosis as fact.

## Validation
- [ ] A competing non-skew explanation tested.
- [ ] Output semantics match before and after.
- [ ] Rollback and workload comparability established.
