---
name: devops-delivery
description: Design or improve CI/CD pipelines, artifact promotion and safe deployment workflows with immutable builds, verification, rollback and failure isolation.
license: Proprietary
metadata:
  version: "1.0.0"
---

# DevOps delivery workflow

## Activate
Use for CI/CD design, build/release automation, promotion across environments, rollout strategies, deployment rollback and developer delivery workflows. Platform API self-service routes to platform-engineering-workflows; incident SLO ownership routes to sre-incident-response.

## Procedure
1. Determine repository, build/runtime, environments, deployment target, access boundaries, target lead time and recovery goals.
2. Separate compilation, unit/integration tests, artifact signing/storage, promotion and deployment approval. Build once when practical.
3. Use ephemeral credentials, scoped permissions and pinned dependencies/actions where supported. Never request secret values in plain text.
4. Define repeatable migrations, health probes, canary or staged rollout where justified, feature flags and safe rollback.
5. Verify failed build, partial deployment, network retry, rollback and artifact provenance behaviors.
6. Report observed durations and failure rates; do not promise deployment improvements without measurement.

## Outputs
Smallest working pipeline/configuration, promotion contract, validation matrix, release checklist and rollback plan.

## Reference
https://docs.github.com/en/actions
