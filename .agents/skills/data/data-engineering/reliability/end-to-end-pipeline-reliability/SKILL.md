---
name: end-to-end-pipeline-reliability
description: "Engineer reliable pipelines with idempotency, deduplication, retries, checkpoints, replay and partial-publication recovery."
metadata:
  version: "1.0.1"
---

# end-to-end-pipeline-reliability

## Activation boundary
Engineer reliable pipelines with idempotency, deduplication, retries, checkpoints, replay and partial-publication recovery.

## Required context
Source guarantees, business keys, target write model, checkpoints, retry budget and late-data policy.

## Production procedure
1. Define a durable unit of work and stable event key before retries or checkpoints.
2. Choose append/merge/replace/transactional publication from sink guarantees.
3. Persist source progress only after target commit or recoverable manifest handoff.
4. Bound retry budgets and provide controlled replay, DLQ redrive, reconciliation and RPO/RTO.
5. Test crashes before/after commit, duplicate delivery, stale checkpoints and restore.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://kafka.apache.org/documentation/#semantics
- https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/fault_tolerance/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
