---
name: risingwave-streaming-sql-engineering
description: "Operate RisingWave streaming SQL with sources, sinks, materialized views, checkpoints, state, backpressure and recovery."
license: Proprietary
metadata:
  version: "1.1.0"
---

# risingwave-streaming-sql-engineering

## Activation boundary
Use for RisingWave streaming database design. Materialized views have freshness lag; do not promise zero lag.

## Required inputs
RisingWave version; source/sink; event key/time; SQL; throughput; state size; retention; checkpoint and freshness SLO.

## Production workflow
1. Define offsets, key semantics, event time and schema evolution.
2. Model incremental views; validate joins, windows, state growth and retractions.
3. Verify connector delivery behavior for the exact release.
4. Size parallelism, memory, state and checkpoint intervals from load.
5. Define sink idempotency and upsert/delete mapping.
6. Monitor source lag, checkpoint progress, state, compaction and sink latency.

## Failure modes and recovery
- Source lag: separate source, compute and sink bottlenecks.
- State growth: review unbounded joins/windows and retention.
- Sink retry: deduplicate by stable event key/version.
- Checkpoint stall: inspect slow actors and storage latency.
- Schema mismatch: quarantine at the source contract.

## Validation and evidence
- Replay a bounded interval and compare with batch reference.
- Test restart, sink outage, restore, schema change, late and duplicate events.
- Measure freshness, checkpoint duration, state size and recovery time.

## Output contract
Return SQL/dataflow design, source/sink guarantee matrix, capacity and replay strategy.

## Official references
- https://docs.risingwave.com/
