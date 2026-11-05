---
name: dask-distributed-data-engineering
description: "Engineer Dask DataFrame and task-graph workloads with partition sizing, shuffle, scheduler, worker memory and recovery controls."
license: Proprietary
metadata:
  version: "1.1.1"
---

# dask-distributed-data-engineering

## Activation boundary
Use for Dask parallel/distributed workloads. Do not recommend it automatically as a Spark replacement; validate task graph and shuffle profile.

## Required inputs
Data volume/shape; partition size; worker CPU/RAM; scheduler topology; filesystem; shuffle; recovery requirements.

## Production workflow
1. Choose Dask DataFrame, Array, Bag or delayed APIs from workload shape.
2. Size partitions from worker memory and task concurrency; avoid tiny and oversized partitions.
3. Inspect task graph for repeated work, unnecessary materialization and expensive shuffles.
4. Pin Dask/distributed/Python dependencies across scheduler and workers.
5. Configure memory thresholds, spill capacity, retries and worker resources.
6. Publish through an idempotent sink.

## Failure modes and recovery
- Worker OOM: inspect per-task memory and partition size.
- Scheduler overload: reduce task granularity.
- Shuffle bottleneck: profile skew and bytes before repartitioning.
- Spill exhaustion: monitor spill storage independently.

## Validation and evidence
- Compare output with a single-node reference on bounded data.
- Test worker loss, scheduler restart, spill pressure, skew and retries.
- Record task count, shuffle bytes, spill, peak memory and duration.

## Output contract
Return suitability decision, partition/shuffle plan, worker sizing and failure-test evidence.

## Official references
- https://docs.dask.org/en/stable/
- https://distributed.dask.org/en/stable/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
