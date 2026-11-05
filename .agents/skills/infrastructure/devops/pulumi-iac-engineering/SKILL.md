---
name: pulumi-iac-engineering
description: "Engineer Pulumi infrastructure programs with typed components, stack configuration, secrets and preview-driven deployment."
metadata:
  version: "1.0.1"
---

# pulumi-iac-engineering

## Activation boundary
Engineer Pulumi infrastructure programs with typed components, stack configuration, secrets and preview-driven deployment.

## Required context
Pulumi runtime/language, provider versions, stack state, secrets backend and cloud account.

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
- https://www.pulumi.com/docs/

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
