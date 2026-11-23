---
name: soda-data-quality-engineering
description: "Implement SodaCL scans with metrics, thresholds, CI integration and accountable data-quality ownership."
metadata:
  version: "1.0.1"
---

# soda-data-quality-engineering

## Activation boundary
Implement SodaCL scans with metrics, thresholds, CI integration and accountable data-quality ownership.

## Required context
Soda version, source, grain, checks, schedule, thresholds, owner and sensitive columns.

## Production procedure
1. Define grain, critical fields, invariants and quality dimensions before checks.
2. Set thresholds from observed baseline and impact; distinguish hard failures from warnings.
3. Run checks in CI and production with bounded query cost and safe diagnostics.
4. Attach owner, incident route, lineage and remediation expectations.
5. Test empty partitions, null spikes, duplicates, late data and schema drift.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://docs.soda.io/soda-documentation/soda-v3/sodacl-reference/metrics-and-checks

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
