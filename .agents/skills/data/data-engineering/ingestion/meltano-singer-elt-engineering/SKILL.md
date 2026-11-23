---
name: meltano-singer-elt-engineering
description: "Operate Meltano and Singer taps/targets with catalog selection, state messages and incremental replication."
metadata:
  version: "1.0.1"
---

# meltano-singer-elt-engineering

## Activation boundary
Operate Meltano and Singer taps/targets with catalog selection, state messages and incremental replication.

## Required context
Plugin versions, streams, replication keys, state persistence, upsert and delete behavior.

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
- https://docs.meltano.com/
- https://www.singer.io/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
