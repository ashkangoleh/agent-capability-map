---
name: apache-doris-olap-engineering
description: "Operate Apache Doris table models, ingestion, materialized views, replication and workload management."
license: Proprietary
metadata:
  version: "1.1.0"
---

# apache-doris-olap-engineering

## Activation boundary
Use for Apache Doris analytical warehouse engineering. Verify behavior against deployed Doris release and storage-compute mode.

## Required context
Doris version; deployment mode; table model; source/sink; data rate; partitioning; materialized views; concurrency and retention.

## Production procedure
1. Choose Duplicate, Aggregate or Unique Key model from update and aggregation semantics.
2. Define partition/bucket distribution and estimate tablet count, skew and growth.
3. Select Stream Load, Routine Load, Broker Load or connector path with explicit labels and retry behavior.
4. Design materialized views and verify rewrite/refresh semantics.
5. Set workload groups and isolate ingestion from BI workloads.
6. Monitor compaction, rowsets, tablet balance, BE/FE health and query profiles.
7. Plan schema changes, rollouts and backup/restore with replica health gates.

## Failure modes and recovery
- Tablet skew: revise distribution key and bucket count.
- Compaction backlog: inspect ingestion bursts and storage headroom.
- Load retry duplicates: reconcile labels/transactions before replay.
- MV not used: inspect rewrite eligibility and freshness.
- FE/BE failure: verify quorum/replicas before increasing load.

## Validation and acceptance
- Test concurrent load, update/delete, compaction, node loss and restore.
- Measure query latency, load throughput, skew, compaction lag and resource use.

## Output contract
Return table model, physical layout, ingestion, MV, workload and recovery plan.

## Official or primary references
- https://doris.apache.org/docs/
