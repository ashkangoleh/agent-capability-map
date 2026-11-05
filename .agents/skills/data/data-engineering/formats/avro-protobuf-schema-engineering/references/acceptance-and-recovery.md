# avro-protobuf-schema-engineering — independent acceptance and recovery

## Capability and observed inputs
Schema encoding and cross-runtime type fidelity. Required context from the existing specialist: Format, registry, producer/consumer languages, field IDs, defaults and retention.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Round-trip nested/null/decimal/timestamp values across independent readers. | Field identity, logical types and backward compatibility remain intact. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Retain prior schema and isolate incompatible assets. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee. - Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits. - Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://avro.apache.org/docs/
- https://protobuf.dev/programming-guides/proto3/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
