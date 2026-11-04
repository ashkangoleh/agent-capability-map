---
name: datafusion-arrow-query-engine
description: "Build Arrow-native query and DataFrame execution with Apache DataFusion; use Ballista only when distributed execution is explicitly required."
license: Proprietary
metadata:
  version: "1.1.0"
---

# datafusion-arrow-query-engine

## Activation boundary
Use for DataFusion query execution, Arrow DataFrames and TableProvider/functions. DataFusion is an embeddable query engine, not a cluster manager.

## Required inputs
DataFusion version; client language; source formats; object store; SQL/functions; memory budget; concurrency; distributed execution need.

## Production workflow
1. Decide embedded, query-service or Ballista deployment; avoid distributed execution without need.
2. Define catalog and TableProvider statistics, projection/filter pushdown and partition pruning.
3. Validate Arrow types, nullability, decimal precision, timestamps and nested types.
4. Inspect logical/physical plans, joins, repartitioning, memory and spill.
5. Bound concurrency and object-store retries.
6. Publish with destination-appropriate commit semantics.

## Failure modes and recovery
- Missing pushdown: inspect plan/provider before scaling.
- Memory pressure: reduce batch/concurrency and test skew.
- Type drift: reject or quarantine incompatible columns.
- Executor loss: verify Ballista shuffle recovery for pinned release.

## Validation and evidence
- Compare SQL results against a trusted engine for edge types.
- Test pushdown, pruning, skew, spill and object-store interruption.
- Record plan, bytes scanned, memory, spill and latency.

## Output contract
Return deployment mode, Arrow type contract, plan evidence and recovery strategy.

## Official references
- https://datafusion.apache.org/user-guide/introduction.html
- https://datafusion.apache.org/ballista/
