---
name: materialize-streaming-sql-engineering
description: "Engineer Materialize streaming SQL with sources, sinks, indexes, logical timestamps, arrangements and compaction."
license: Proprietary
metadata:
  version: "1.1.0"
---

# materialize-streaming-sql-engineering

## Activation boundary
Use for Materialize streaming SQL. Do not conflate logical timestamps/frontiers with Kafka offsets or Flink watermarks.

## Required inputs
Materialize version; sources/sinks; event identity; freshness; indexes; concurrency; retention; auth.

## Production workflow
1. Model source ingestion and timestamping guarantees.
2. Define views and indexes from real query patterns; justify their memory cost.
3. Understand logical timestamps, frontiers and compaction windows.
4. Configure source/sink auth and secret rotation.
5. Define sink delivery, retry and deduplication.
6. Monitor source progress, arrangements, compaction and sink state.

## Failure modes and recovery
- Frontier stalls: identify slow source/dataflow.
- Arrangement growth: review indexes and joins.
- Sink duplicates: enforce stable keys.
- Source reconnect: verify offsets and source retention.
- Latency regression: inspect index coverage and plans.

## Validation and evidence
- Compare view results with bounded batch computation.
- Test outage, reconnect, late data, schema evolution and sink retry.
- Measure frontiers, lag, arrangement bytes and query latency.

## Output contract
Return source/timestamp model, view/index design, compaction and recovery.

## Official references
- https://materialize.com/docs/
