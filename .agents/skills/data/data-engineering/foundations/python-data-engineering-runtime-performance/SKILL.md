---
name: python-data-engineering-runtime-performance
description: "Build maintainable Python data pipelines with bounded memory, typed interfaces, async I/O and reproducible packaging."
metadata:
  version: "1.0.1"
---

# python-data-engineering-runtime-performance

## Activation boundary
Build maintainable Python data pipelines with bounded memory, typed interfaces, async I/O and reproducible packaging.

## Required context
Python/runtime, native libraries, data volume, memory ceiling, I/O and concurrency.

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
- https://docs.python.org/3/
- https://arrow.apache.org/docs/python/
- https://docs.pola.rs/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
