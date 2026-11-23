---
name: starrocks-olap-warehouse-engineering
description: "Design StarRocks OLAP tables, distribution and partitioning, materialized views, compaction, workload groups and query performance."
license: Proprietary
metadata:
  version: "1.1.1"
---

# starrocks-olap-warehouse-engineering

## Activation boundary
Use for StarRocks analytical warehouse design. Use separate CDC and Stream Load skills for source-change and load transaction APIs.

## Required inputs
StarRocks version; workload; table model; update rate; keys; partition lifecycle; query patterns; concurrency; compaction budget.

## Production workflow
1. Select Duplicate, Primary, Aggregate or Unique Key from mutation semantics.
2. Define partition/bucket strategy; estimate skew, tablet count and growth.
3. Design sort keys, indexes and types from predicates and joins.
4. Select Stream Load, Broker Load, Routine Load or connector path with explicit replay rules.
5. Design materialized views and validate rewrite eligibility.
6. Set workload groups and monitor compaction, tablet balance, query profiles and load errors.

## Failure modes and recovery
- Update amplification: inspect key design and compaction.
- Tablet skew: correct distribution key.
- Compaction backlog: inspect write amplification and headroom.
- MV not rewritten: inspect query shape and eligibility.
- Load timeout: reconcile label/transaction state before retry.

## Validation and evidence
- Test concurrent loads, updates/deletes, compaction and node loss.
- Validate pruning, skew, p95/p99 latency, spill and throughput.
- Keep CDC and Stream Load guarantees separate.

## Output contract
Return table model, physical design, MV strategy, workload isolation and benchmark evidence.

## Official references
- https://docs.starrocks.io/
- https://docs.starrocks.io/docs/table_design/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
