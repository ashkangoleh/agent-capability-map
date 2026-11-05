---
name: data-orchestration-platform-selection
description: "Select or migrate data workflow orchestrators using execution semantics, scheduling, durability, deployment and operational fit."
license: Proprietary
metadata:
  version: "1.1.1"
---

# data-orchestration-platform-selection

## Activation boundary
Use to compare Mage, DolphinScheduler, Luigi, Oozie, Kestra, Airflow, Dagster, Prefect, Argo, Flyte, Kubeflow and Temporal. An orchestrator does not replace compute.

## Required inputs
Workflow topology; triggers; task duration; retries/backfills; state durability; deployment; language; Kubernetes; multi-tenancy; SLO.

## Production workflow
1. Separate scheduling/orchestration from Spark, Flink, dbt or warehouse execution.
2. Compare DAG, asset-aware, event-driven and durable workflow models.
3. Compare HA, metadata DB, executor isolation, queueing and backpressure.
4. Compare retries, idempotency, backfills, catchup, concurrency and dependency semantics.
5. Compare sensors, approvals, timers, Kubernetes, secrets, RBAC and audit.
6. Model control-plane footprint, on-call load, migration and upgrade cost.

## Failure modes and recovery
- Dual-run duplicate execution: use single-writer gates or idempotent tasks.
- Schedule drift: compare timezone and data interval semantics.
- Backfill overload: cap concurrency.
- Lost state: preserve metadata DB and external task state.
- Plugin incompatibility: pin versions.

## Validation and evidence
- Test schedule parity, retries, backfills, cancellation, worker loss and control-plane restart.
- Shadow-run representative workflows without duplicate side effects.
- Measure scheduler latency, queue wait and recovery.

## Output contract
Return weighted decision matrix, compatibility gaps, migration plan and rollback criteria.

## Official references
- https://dolphinscheduler.apache.org/en-us/docs/latest/
- https://docs.mage.ai/
- https://luigi.readthedocs.io/en/stable/
- https://oozie.apache.org/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
