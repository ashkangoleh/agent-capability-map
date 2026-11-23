# schema-registry-compatibility — independent acceptance and recovery

## Capability and observed inputs
Event-time, offsets and sink delivery contracts. Required context from the existing specialist: Registry/version; format; subject naming; producer/consumer versions; compatibility mode; key/value schema; references; replay horizon.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Inject late events, duplicate retries and restart with divergent state. | Event-time windows and output effects follow explicitly proven guarantee. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Rewind replayable source and perform idempotent/transactional sink recovery. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Registry accepts a change but consumers break: run semantic and replay tests; compatibility mode is not an application contract. - Wrong subject naming creates parallel subjects: inspect actual subject before registering. - Protobuf field number reuse corrupts wire compatibility: reserve removed numbers permanently. - Registry outage breaks schema lookup: define cache and producer failure behavior.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html
- https://www.apicur.io/registry/docs/apicurio-registry/3.0.x/getting-started/assembly-what-is-apicurio-registry.html

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
