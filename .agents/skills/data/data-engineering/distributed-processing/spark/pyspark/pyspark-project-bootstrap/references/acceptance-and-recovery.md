# pyspark-project-bootstrap — independent acceptance and recovery

## Capability and observed inputs
Spark distributed query correctness and state. Required context from the existing specialist: Identify task and deliverable, Spark and Python runtimes, cluster manager or Spark Connect mode, input/output storage and format, schema, grain, partition policy, transformation requirements, availability/recovery expectations, deployment model and security constraints. Treat unknown values as unknown; a version-neutral structure can be proposed with open decisions rather than blocking on a questionnaire.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Inject executor loss, skew/hot key, stale cached plan or stateful restart. | Result counts and business keys remain correct across retry and adaptive plans. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Return to previous artifact/streaming checkpoint with sink idempotence. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
1. Inspect the actual project directory and provided specifications first. State what exists and what is missing. For a structure-only request, propose the structure now with labeled decision points; ask at most the material clarification that prevents the requested output. 2. Verify the runtime: distinguish the **currently available official Spark release**, the **deployed cluster release**, the **Python compatibility matrix**, and the **recommended version for this project**. They are different facts. Do not label Spark 3.5 or any hardcoded line "latest stable" without checking the current official release list and dates. Do not assume a le

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://spark.apache.org/downloads
- https://spark.apache.org/news/
- https://spark.apache.org/documentation
- https://spark.apache.org/docs/latest/api/python/
- https://hadoop.apache.org/docs/current3/hadoop-aws/tools/hadoop-aws/troubleshooting_s3a.html

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
