---
name: devsecops-review
description: Review and harden software supply chains, CI/CD permissions, dependency exposure, secret handling and deployment security using evidence-based risk prioritization.
license: Proprietary
metadata:
  version: "1.0.0"
---

# DevSecOps hardening

## Activate
Use for CI/CD and build security, credential exposure, dependency provenance, container image hardening, security gates, or least-privilege delivery controls. General functional CI/CD work routes to devops-delivery.

## Procedure
1. Model assets, attackers, trust boundaries, privileged identities, third-party code and release pathways.
2. Inspect actual pipeline definitions, lockfiles, images, permissions, secret injection and artifact distribution. Never print secrets.
3. Prioritize risks by exploitability, exposure, severity and blast radius instead of adding tools by default.
4. Specify minimal controls: least privilege, ephemeral credentials, pinning, signed/provenance-aware artifacts where supported, secret scans and patch workflow.
5. Distinguish code findings, policy decisions and confirmed vulnerabilities. Validate against authoritative advisories before stating affected versions.
6. Include false-positive handling, exception ownership, staged rollout, rollback and audit evidence.

## Outputs
Threat/asset table, ranked findings backed by evidence, minimal patches, verification steps and residual risk. No unsupported compliance claims.

## Reference
https://slsa.dev/spec/v1.1/
