---
name: managed-elt-fivetran-estuary-operations
description: "Operate managed ELT connectors with connector limits, CDC semantics, destination cost and exit planning."
metadata:
  version: "1.0.1"
---

# managed-elt-fivetran-estuary-operations

## Activation boundary
Operate managed ELT connectors with connector limits, CDC semantics, destination cost and exit planning.

## Required context
Provider/plan, connector, sync frequency, delete support, schema drift, pricing and export options.

## Production procedure
1. Inspect source consistency, pagination/CDC semantics, quotas, auth, deletes and schema behavior for the exact connector release.
2. Choose a stable cursor/log position and persist state only after durable sink publication.
3. Use bounded concurrency, timeouts, jittered retries and explicit permanent/transient error handling.
4. Define deduplication, schema drift, late updates, deletes and reprocessing.
5. Test interruption, duplicate pages/events, cursor regression, source failover and sink outage.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://fivetran.com/docs
- https://docs.estuary.dev/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
