---
name: bitemporal-event-data-modeling
description: "Model valid-time and system-time history for reproducible as-of queries and retroactive corrections."
metadata:
  version: "1.0.0"
---

# bitemporal-event-data-modeling

## Activation boundary
Model valid-time and system-time history for reproducible as-of queries and retroactive corrections.

## Required context
Event/valid/system time, interval semantics, timezone, clock quality and correction policy.

## Production procedure
1. Declare business grain, keys, ownership and event-time semantics before selecting tools.
2. Choose modeling/runtime patterns from audit, history, scale and consumer query requirements.
3. Define canonical types, timezone/decimal rules and schema contracts.
4. Specify corrections, late data, historical reconstruction and migration behavior.
5. Validate grain, uniqueness, referential integrity and reproducibility.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://www.postgresql.org/docs/current/functions-datetime.html

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
