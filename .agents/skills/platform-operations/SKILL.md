---
name: platform-operations
description: "Review platform operational readiness, ownership, service boundaries, maintenance and recovery controls."
license: Proprietary
metadata:
  version: "1.1.0"
---

# platform-operations

## Activation boundary
Use only for cross-cutting platform operational-readiness reviews when explicitly requested. Do not use as a generic Kubernetes, Helm, cloud, network, Linux or DevOps implementation skill; select the relevant specialist instead.

## Required context
Platform/service owner, environment, dependencies, SLOs, maintenance model, on-call path, access boundaries, backup/restore evidence and lifecycle stage.

## Production procedure
1. Define platform boundary, consumers, critical journeys, dependencies and named service owner.
2. Review SLOs, dashboards, alerts, runbooks, escalation and incident communication.
3. Verify identity, secrets, access reviews, audit retention, patch cadence and security exceptions.
4. Review release, maintenance, capacity, backup/restore, DR, deprecation and support lifecycle.
5. Identify unsupported components, single-person knowledge, manual steps and cross-team handoffs.
6. Produce a readiness assessment with evidence, severity, owner, due date and explicit go/no-go criteria.

## Failure modes and recovery
- A platform without a named owner or on-call route is not operationally ready.
- Dashboard presence is not evidence of alert coverage; verify alerts against user-facing symptoms.
- Backup jobs without restore exercises do not establish recoverability.
- Do not approve production change when access, rollback, dependency ownership or escalation is ambiguous.

## Validation and evidence
- Verify one normal operation, one incident workflow, one restore workflow and one access-review workflow.
- Confirm SLOs, alert routing, runbook freshness, ownership and exception expiry.
- Separate observed controls from planned controls and unverified assumptions.

## Official references
- https://sre.google/sre-book/service-level-objectives/
- https://sre.google/workbook/incident-response/
- https://www.cncf.io/architecture/

## Output contract
Return a readiness decision, evidence-backed findings, prioritized gaps, named owners, go/no-go criteria and smallest safe next actions. Never claim a control was tested without evidence.
