---
name: backup-dr-restore-exercises
description: "Design and test infrastructure backup, failover and restoration against explicit RPO/RTO."
metadata:
  version: "1.0.0"
---

# backup-dr-restore-exercises

## Activation boundary
Design and test infrastructure backup, failover and restoration against explicit RPO/RTO.

## Required context
Assets, dependencies, RPO/RTO, backup immutability, restore order, credentials and DR region.

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
- https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.
