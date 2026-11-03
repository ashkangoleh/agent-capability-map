---
name: platform-operations
description: Use when operating or designing Kubernetes, Docker, Helm, cloud infrastructure, CI/CD, networking, observability, reliability, or production incident workflows.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Purpose

Make infrastructure and production operations safe, observable, reversible, and aligned with the actual environment.

## Inputs and prerequisites

Identify environment, cluster/context, namespace, versions, deployment mechanism, access level, SLO, blast radius, maintenance window, and change authorization.

## Procedure

1. Start with read-only inspection. Confirm active account, context, cluster, namespace, release, and target resources.
2. Inspect manifests, Helm values, chart versions, image tags, policies, and current state.
3. Distinguish desired state from observed state.
4. Identify blast radius, dependencies, capacity, security boundaries, and failure domains.
5. Prefer declarative and repeatable changes. Avoid imperative mutations when a reviewed manifest or release process is available.
6. For changes, define prechecks, rollout strategy, health gates, rollback, and recovery.
7. Never run destructive commands or production mutations without explicit authorization.
8. Verify post-change state using independent signals: resource status, events, logs, metrics, and application-level checks.
9. Record exact commands and actual outputs. Redact secrets.

## Evidence requirements

Use actual cluster output, manifests, chart metadata, release notes, and official version-specific documentation. Do not assume a context or namespace from a prior task.

## Output contract

Provide diagnosis, evidence, safe commands, expected observations, stop conditions, rollback, and residual risk.

## Failure modes and abstention

Stop if target identity is ambiguous, access is insufficient, the change is irreversible, or rollback cannot be established for a high-impact operation. Do not state that a deployment succeeded until observed.

## Validation checklist

- [ ] Target environment and context are verified.
- [ ] Read-only inspection preceded mutation.
- [ ] Blast radius and dependencies are known.
- [ ] Authorization and rollback are explicit.
- [ ] Post-change health is verified.

## Official starting references

Verify the applicable version and publication date before using these sources:
- https://kubernetes.io/docs/home/
- https://helm.sh/docs/
