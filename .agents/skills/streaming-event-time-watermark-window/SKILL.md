---
name: streaming-event-time-watermark-window
description: "Design event-time streaming windows with watermarks, allowed lateness, idle partitions, triggers, state retention and correction semantics."
license: Proprietary
metadata:
  version: "1.1.0"
---

# streaming-event-time-watermark-window

## Activation boundary
Use for event-time and window semantics in Flink, Spark Structured Streaming, Beam and streaming SQL. A watermark is not a guarantee that no later event can arrive.

## Required context
Event timestamp source; clock skew; disorder distribution; window type; allowed lateness; idleness; state backend; sink upsert/retraction support.

## Production procedure
1. Define event time from source metadata or business timestamp; document timezone and clock-skew assumptions.
2. Measure event-time skew and arrival delay by partition; choose watermark delay from observed tail latency and business tolerance.
3. Select tumbling, hopping/sliding, session or custom windows from aggregation semantics.
4. Define late-event policy: drop, side output, update/retract prior result or correction pipeline.
5. Configure idleness detection where inactive partitions stall progress; validate it does not hide delayed active sources.
6. Bound state with TTL/retention consistent with window and correction requirements.
7. Align sink semantics with updates/retractions; append-only sinks cannot represent corrected aggregates without a compensating model.

## Failure modes and recovery
- Watermark stalls: inspect slow partitions, source idleness and timestamp assignment.
- Late data dropped: quantify loss and replay from durable source when policy permits.
- State explosion: review unbounded windows and joins before changing TTL.
- Duplicate window output: use deterministic keys and sink upsert/retraction semantics.
- Clock drift: isolate source timestamp quality instead of arbitrarily increasing watermark.

## Validation and acceptance
- Test out-of-order events, idle partitions, lateness beyond threshold, restart and checkpoint recovery.
- Compare output with an offline event-time reference.
- Measure watermark delay, late-event ratio, state bytes, checkpoint time and correction count.

## Output contract
Return event-time definition, window/watermark policy, late-data contract, state budget and sink correction model.

## Official or primary references
- https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/event-time/
- https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html
