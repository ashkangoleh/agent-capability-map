---
name: temporal-durable-workflows
description: "Use Temporal durable workflows for resumable long-running data operations, signals, timers and human intervention."
metadata:
  version: "1.0.1"
---

# temporal-durable-workflows

## Activation boundary
Use Temporal durable workflows for resumable long-running data operations, signals, timers and human intervention.

## Required context
Temporal server/SDK, workflow duration, activity boundaries, idempotency and retention.

## Production procedure
1. Model dependencies, trigger semantics, task boundaries and external side effects.
2. Pin runtime/plugin/container versions and keep heavy compute outside scheduler processes.
3. Set concurrency, retries, timeouts, cancellation and backfill windows from measured limits.
4. Make tasks idempotent or compensatable; isolate secrets and execution environments.
5. Test duplicate triggers, worker loss, partial runs and upgrades.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://docs.temporal.io/workflows
- https://docs.temporal.io/design-patterns/resumable-activity

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
