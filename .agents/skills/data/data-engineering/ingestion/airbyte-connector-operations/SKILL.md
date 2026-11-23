---
name: airbyte-connector-operations
description: "Operate Airbyte connectors with correct sync modes, incremental state, schema discovery and recovery."
metadata:
  version: "1.0.1"
---

# airbyte-connector-operations

## Activation boundary
Operate Airbyte connectors with correct sync modes, incremental state, schema discovery and recovery.

## Required context
Connector version, streams, cursor/key, state persistence, destination semantics and deletes.

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
- https://docs.airbyte.com/platform/connector-development/best-practices

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
