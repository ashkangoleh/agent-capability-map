---
name: kafka-streams-ksqldb-engineering
description: "Build Kafka Streams and ksqlDB applications with partition-aware joins, state stores, changelog topics and operational recovery."
license: Proprietary
metadata:
  version: "1.1.1"
---

# kafka-streams-ksqldb-engineering

## Activation boundary
Use for Kafka Streams and ksqlDB topology design and operations. Do not treat stateful joins or persistent queries as stateless SQL.

## Required context
Kafka/client versions; topic keys/partitions; topology; state-store size; processing guarantee; changelog retention; standby replicas; deployment model.

## Production procedure
1. Design topic keys and partition counts before joins; co-partitioned joins require compatible partitioning and serialization.
2. Choose stream-table, table-table or windowed stream-stream join from update and event-time semantics.
3. Define state-store and changelog retention, replication and restore expectations.
4. Select processing guarantee and configure producer/consumer transaction settings consistently; document external sink separately.
5. Set commit interval, cache, standby replicas, task assignment and state directory for the deployment model.
6. For ksqlDB define persistent query lifecycle, output topic naming, key/value formats and registry integration.
7. Plan rolling deployment and application reset/reprocessing; resets can re-emit side effects.

## Failure modes and recovery
- Join partition mismatch: repartition upstream with a stable key and validate serialization.
- Rebalance loop: inspect poll interval, processing time, task migration and deployment churn.
- Slow state restore: review changelog retention, standby replicas and local disk.
- Reset duplicates: require idempotent sinks or reconcile output topics.
- Schema evolution break: validate key and value compatibility.

## Validation and acceptance
- Test repartitioned joins, out-of-order events, task migration, broker restart, state restore and reset.
- Validate output key correctness and changelog replay.
- Measure rebalance time, lag, state restore duration and output latency.

## Output contract
Return topology/key design, state/changelog plan, processing guarantee, deployment and recovery evidence.

## Official or primary references
- https://kafka.apache.org/documentation/streams/
- https://docs.ksqldb.io/en/latest/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
