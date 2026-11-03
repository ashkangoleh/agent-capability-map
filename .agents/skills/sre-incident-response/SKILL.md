---
name: sre-incident-response
description: Define service SLI/SLOs, incident triage and reliability improvements with observable evidence, runbooks, error budgets and recovery verification.
license: Proprietary
metadata:
  version: "1.0.0"
---

# SRE reliability and incident response

## Activate
Use for outages, symptoms, alerting and SLO design, operational runbooks, postmortems and reliability risk prioritization. Delivery automation routes to devops-delivery; network-only fault isolation routes to network-diagnostics.

## Procedure
1. Clarify customer impact, critical user journeys, incident severity, blast radius, start time and available metrics/logs/traces.
2. Establish SLIs with precise numerator/denominator, reporting windows, exclusions, and data-quality assumptions.
3. Prioritize containment and customer recovery before speculative root-cause explanations; document safe escalation and communication.
4. Investigate deployment, capacity, dependencies, network, data consistency and cascading failure hypotheses with discriminating evidence.
5. Define rollback, failover, retries/timeouts, protection against retry storms and recovery validation; never change production without authorization.
6. After recovery, record timeline, contributing factors, detection gaps, owners and preventive work. Assign evidence-based error budgets, not arbitrary SLO percentages.

## Outputs
Incident timeline/runbook, observed impact, testable hypotheses, recovery checklist, SLI/SLO definitions and follow-up work.

## Reference
https://sre.google/sre-book/service-level-objectives/
