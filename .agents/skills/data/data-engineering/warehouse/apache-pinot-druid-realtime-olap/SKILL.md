---
name: apache-pinot-druid-realtime-olap
description: "Design Apache Pinot and Apache Druid real-time OLAP ingestion, segments, indexes, retention and low-latency aggregation."
license: Proprietary
metadata:
  version: "1.1.1"
---

# apache-pinot-druid-realtime-olap

## Activation boundary
Use for high-concurrency, low-latency event analytics. Do not treat Pinot/Druid as general lakehouse warehouses without workload fit.

## Required context
Ingestion rate; event dimensions; query patterns; freshness; segment size; retention; replication; broker/stream source; availability target.

## Production procedure
1. Model query dimensions, metrics, filters, group-bys and cardinality before schema/index design.
2. Choose real-time ingestion and offline/batch segment paths; define handoff and deduplication.
3. Set partitioning, replicas, segment size and retention from throughput and query parallelism.
4. Select inverted, range, text, star-tree or other indexes only where measured query patterns justify them.
5. Define upsert/dedup semantics and primary-key requirements; confirm supported behavior for exact release.
6. Plan segment compaction, reload, deep storage and retention cleanup.
7. Protect broker/source systems with bounded ingestion and monitor consumer lag.

## Failure modes and recovery
- Segment explosion: tune flush/segment sizing and compaction.
- High-cardinality index blowup: choose indexes selectively.
- Realtime/offline duplication: validate segment handoff and time boundary.
- Broker lag: separate ingestion backpressure from query saturation.
- Upsert memory growth: review primary-key and retention design.

## Validation and acceptance
- Test realtime-to-offline handoff, late events, duplicate keys, broker outage and segment reload.
- Measure ingestion lag, segment count, query p95/p99, index size and deep-storage cost.

## Output contract
Return schema/index plan, ingestion topology, segment lifecycle, retention and benchmark evidence.

## Official or primary references
- https://docs.pinot.apache.org/
- https://druid.apache.org/docs/latest/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
