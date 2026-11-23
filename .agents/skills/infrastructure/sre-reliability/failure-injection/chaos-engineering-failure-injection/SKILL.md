---
name: chaos-engineering-failure-injection
description: "Run controlled failure-injection experiments with blast-radius limits, hypotheses and recovery verification."
metadata:
  version: "1.0.1"
---

# chaos-engineering-failure-injection

## Activation boundary
Run controlled failure-injection experiments with blast-radius limits, hypotheses and recovery verification.

## Required context
Hypothesis, steady-state signals, scope, abort criteria, permissions and rollback.

## Production procedure
1. Define user-visible SLIs, SLOs, error budgets and actionable burn-rate windows.
2. Model dependencies, saturation, capacity, failure domains and recovery objectives.
3. Instrument correlated metrics/logs/traces with controlled cardinality, sampling and retention.
4. Run controlled failure or restore exercises with blast-radius and abort criteria.
5. Verify alert quality, on-call ownership, rollback and measured RPO/RTO.

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
- https://principlesofchaos.org/

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
