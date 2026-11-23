---
name: flyte-kubeflow-pipeline-orchestration
description: "Design Flyte and Kubeflow Pipelines for reproducible containerized workflows, artifacts and Kubernetes isolation."
metadata:
  version: "1.0.1"
---

# flyte-kubeflow-pipeline-orchestration

## Activation boundary
Design Flyte and Kubeflow Pipelines for reproducible containerized workflows, artifacts and Kubernetes isolation.

## Required context
Platform release, Kubernetes, task images, artifact store, metadata DB and cache policy.

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
- https://docs.flyte.org/
- https://www.kubeflow.org/docs/components/pipelines/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
