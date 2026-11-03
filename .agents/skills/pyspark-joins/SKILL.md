---
name: pyspark-joins
description: Design, debug, or optimize a PySpark or Spark SQL join using correct join semantics and a verified physical plan. Use for an isolated join question, not a whole ETL job or a proven skew incident.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Spark join semantics and physical plans

## When to use
Use when the deliverable centers on join correctness, strategy, cardinality, explain plans, join hints, null-handling, or AQE. If the primary symptom is uneven task durations or hot keys, prefer pyspark-skew-diagnostics.

## Workflow
1. Identify Spark version, join type, keys, null behavior, uniqueness/cardinality, and estimated input sizes; measure instead of assuming.
2. Verify semantics first: missing rows, accidental many-to-many multiplication, non-equi predicates, duplicate keys, and null-safe equality.
3. Capture the physical plan using explain; compare to actual stages and task metrics. Separate planner estimates from observed bytes/rows.
4. Consider broadcast, sort-merge, shuffle-hash and adaptive strategies only where supported by the deployed Spark version and measured sizes.
5. Check data layout, partitioning, predicate pushdown, and avoid unnecessary repartitions and caching.
6. If skew is evidenced, follow pyspark-skew-diagnostics for that specific problem; do not immediately add salting.
7. Validate equivalence against a small deterministic dataset and compare representative before/after execution plans and workload metrics.

## Evidence and output
Supply SQL/DataFrame code or a minimal change, expected join cardinality, relevant plan fragments, version/setting assumptions, observed metrics, and rollback/test steps. Prefer Spark's version-specific SQL performance tuning and join documentation.

## Failure modes
Hints can be ignored or harm performance; broadcast may cause memory failures; null and duplicate behavior can silently corrupt output. Do not promise a speedup without workload measurements.

## Validation
- [ ] Correctness established before optimization.
- [ ] Physical plan and observed metrics distinguished.
- [ ] Memory, skew, and retry risks addressed.
