# parquet-file-layout-tuning — independent acceptance and recovery

## Source-specific contract
Focus: Source snapshots and resumable ingestion. Evidence required by this specialist: Dataset grain, file counts and size distribution, engines, object store/HDFS, scan filters, row-group statistics, compression, memory and access patterns.

## Falsification matrix
| Scenario | Probe | Acceptance oracle |
|---|---|---|
| Baseline | Pin deployed builds, source/target revisions, input grain, authorization scope and representative workload. Record control counts and costs. | Results agree with a trusted independent baseline; missing observations stay UNKNOWN. |
| Targeted fault | Fail between source page and durable target checkpoint; replay duplicates. | Input keys and control totals match durable output across retries. |
| Replay and recovery | Crash after a durable write and before checkpoint; restart with identical inputs and verify replay/cleanup. | Restart at committed source point, keeping raw artifacts for reconciliation. |
| Version/contract drift | Change a schema or connector release on a fixed test fixture and compare before/after. | No undocumented type/data loss, access regression or false compatibility claims. |

## Existing specialist risk signals
- Compare total rows, schema, null counts and hashes before/after rewrite. - Measure files opened, bytes scanned, read parallelism and object-store requests. - Include edge cases, timeouts and partial failures where material; do not claim tests executed without tool traces.

## Evidence checklist
- [ ] Confirm installed runtime and connector versions with official release documentation; do not trust `latest`.
- [ ] Preserve exact fixture/data snapshot, code/config revision and evaluation commands, if executed.
- [ ] Measure reconciliation per business key and timestamp/window, including duplicates, late changes and deletes as applicable.
- [ ] Report observed fault injection and recovery separately from unexecuted test plans.
- [ ] Record SLO/cost/incident owner, security boundary, release stop and rollback/failback conditions.
- [ ] Require explicit approval for live mutations and never interpret this guide as authorization.

## Reference starting points — pin release before use
- https://parquet.apache.org/docs/concepts/
- https://parquet.apache.org/docs/file-format/configurations/

Not evidence of production readiness. The standalone router does not automatically execute referenced scripts.
