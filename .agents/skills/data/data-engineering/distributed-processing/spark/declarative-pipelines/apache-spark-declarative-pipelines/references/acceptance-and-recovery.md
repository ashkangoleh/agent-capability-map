# apache-spark-declarative-pipelines — independent acceptance and recovery

## Capability and observed inputs
Spark distributed query correctness and state. Required context from the existing specialist: Runtime/SDP version; platform; SQL/Python; sources/sinks; streaming/triggered mode; catalog; quality/freshness SLO.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Inject executor loss, skew/hot key, stale cached plan or stateful restart. | Result counts and business keys remain correct across retry and adaptive plans. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Return to previous artifact/streaming checkpoint with sink idempotence. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Unsupported feature: use portable subset or isolate platform-specific code. - State incompatibility: preserve checkpoints and use supported migration. - Unexpected full refresh: inspect dependency invalidation. - Continuous cost spike: switch mode only if freshness allows. - Quality rule drops valid data: quarantine and alert.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://spark.apache.org/docs/latest/
- https://docs.databricks.com/aws/en/ldp/concepts/spark-declarative-pipelines

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
