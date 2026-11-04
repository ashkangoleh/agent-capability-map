---
name: snowflake-data-platform-engineering
description: "Engineer Snowflake file and row ingestion, Snowpipe, Snowpipe Streaming, Streams and Tasks, Dynamic Tables and cost-aware refresh."
license: Proprietary
metadata:
  version: "1.1.0"
---

# snowflake-data-platform-engineering

## Activation boundary
Use for Snowflake-native data engineering. Snowpipe, Snowpipe Streaming, Streams/Tasks and Dynamic Tables are not interchangeable.

## Required inputs
Region/edition; source pattern; latency/volume; table type; warehouse budget; schema; task graph; retention/access.

## Production workflow
1. Choose COPY, Snowpipe or Snowpipe Streaming from payload, latency and cost.
2. Validate stage notifications, load history, file format and duplicate behavior.
3. For Snowpipe Streaming, validate client version, channel/offset and commit semantics.
4. Choose Streams/Tasks for procedural CDC and Dynamic Tables for supported declarative refresh.
5. Treat TARGET_LAG as a freshness goal, not guaranteed schedule or zero lag.
6. Control warehouse sizing, auto-suspend, concurrency, refresh and storage access.

## Failure modes and recovery
- File gaps: compare event notifications with stage listing/load history.
- Stream consumption mistakes: verify staleness and transaction state.
- Task failure: inspect dependencies, privileges and warehouse availability.
- Dynamic Table lag: inspect refresh history and incremental eligibility.
- Cost spike: tune refresh cadence and compute.

## Validation and evidence
- Test duplicate/late files, schema changes, task retries and refresh.
- Compare incremental outputs with full refresh.
- Measure freshness, credits, bytes scanned and failed rows.

## Output contract
Return ingestion decision, pipeline topology, freshness/cost model and replay plan.

## Official references
- https://docs.snowflake.com/en/user-guide/data-load-overview
- https://docs.snowflake.com/en/user-guide/data-pipelines-intro
