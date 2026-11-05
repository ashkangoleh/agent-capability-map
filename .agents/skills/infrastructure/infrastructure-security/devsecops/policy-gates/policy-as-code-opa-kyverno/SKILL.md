---
name: policy-as-code-opa-kyverno
description: "Design policy-as-code controls with OPA/Gatekeeper and Kyverno for admission, validation and mutation."
metadata:
  version: "1.0.1"
---

# policy-as-code-opa-kyverno

## Activation boundary
Design policy-as-code controls with OPA/Gatekeeper and Kyverno for admission, validation and mutation.

## Required context
Cluster/API versions, policy scope, exemptions, audit mode and enforcement rollout.

## Production procedure
1. Map threats, trust boundaries, assets and required security gates before selecting scanners.
2. Integrate SAST/DAST/SCA, secrets, IaC, image, SBOM and provenance checks with severity policy.
3. Use policy-as-code in audit mode before enforce; define narrow exceptions and expiry.
4. Verify identity, signing, attestation and admission at deployment time.
5. Test bypass paths, false positives, scanner outage and emergency exception handling.

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
- https://www.openpolicyagent.org/docs/
- https://kyverno.io/docs/

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
