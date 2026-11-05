# cloud-warehouse-engineering — independent acceptance and recovery

## Capability and observed inputs
Managed warehouse cost/transaction contracts. Required context from the existing specialist: Workload mix; latency/freshness; concurrency; data volume; SQL dialect; storage; identity; residency; team skills; cost model.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Interrupt COPY/MERGE after API timeout with warehouse resource throttling. | Statement and ingestion outcomes reconcile with billing and snapshot state. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Resolve transaction status and resume from verified staged files. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Benchmark mismatch: use representative concurrency and data distribution. - Cost surprise: include refresh, idle, egress and serverless costs. - Dialect lock-in: inventory proprietary SQL and stored procedures. - Ingestion mismatch: verify API delivery/offset semantics. - Governance gap: test direct storage and export access, not only warehouse grants.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://docs.snowflake.com/
- https://docs.cloud.google.com/bigquery/docs
- https://docs.aws.amazon.com/redshift/latest/dg/welcome.html
- https://docs.databricks.com/aws/en/sql/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
