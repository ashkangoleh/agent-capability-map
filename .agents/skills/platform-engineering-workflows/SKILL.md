---
name: platform-engineering-workflows
description: Design internal developer platforms, reusable golden paths and self-service workflows with clear platform product boundaries, support ownership and measurable adoption.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Platform engineering and developer self-service

## Activate
Use for platform APIs, standardized deployment templates, developer portals, environment provisioning, tenancy, policy boundaries and self-service delivery. Single CI/CD pipeline changes route to devops-delivery.

## Procedure
1. Identify internal developer personas, repeated friction, platform scope, team ownership and explicit non-goals.
2. Compare extending an existing platform with creating a new abstraction. Prefer a documented template over a control plane when sufficient.
3. Define golden-path inputs/outputs, idempotent provisioning, tenancy/isolation, security defaults, contract versions and upgrade strategy.
4. Account for drift, day-two operations, platform outages, onboarding and support escalation.
5. Add observability and success metrics such as time-to-first-deploy, failure rate, adoption and maintenance cost; treat unmeasured gains as hypotheses.
6. Validate a real developer journey, failure injection and rollback before scaling platform scope.

## Outputs
Platform product contract, minimal reference implementation, failure modes, operating model, rollout and measurable adoption plan.

## Reference
https://tag-app-delivery.cncf.io/whitepapers/platforms/
