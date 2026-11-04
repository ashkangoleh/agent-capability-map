---
name: ci-cd-release-engineering
description: "Design CI/CD release pipelines with immutable artifacts, promotion gates, rollback and environment isolation."
metadata:
  version: "1.0.0"
---

# ci-cd-release-engineering

## Activation boundary
Design CI/CD release pipelines with immutable artifacts, promotion gates, rollback and environment isolation.

## Required context
Source control, runners, artifact registry, deployment targets, approvals and release SLO.

## Production procedure
1. Inspect repository, provider/runtime versions, remote state, identity and deployment target before changes.
2. Design immutable artifacts, reusable modules, pinned providers and explicit environment boundaries.
3. Preview plans/manifests and validate drift, destructive replacements, secrets and provenance.
4. Use progressive promotion with approvals, rollback conditions and owner-visible audit trails.
5. Test concurrent runs, partial apply, expired credentials, drift and recovery.

## Failure modes and recovery
- Start with read-only evidence collection and confirm the exact environment/cluster/account before mutation.
- Treat credentials, production data, network reachability and state backends as security boundaries.
- Define blast radius, abort criteria, rollback limits and post-change verification before execution.
- Do not claim availability, security or recovery guarantees without evidence from the deployed version and tested path.

## Validation
- Verify product/version compatibility against official documentation.
- Test failure, partial rollout, identity expiry, capacity exhaustion and recovery where applicable.
- Record ownership, monitoring, approval and rollback evidence.

## Official references
- https://docs.github.com/en/actions

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.
