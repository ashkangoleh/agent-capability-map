# Failure, rollback and recovery playbook

**Preconditions:** an approved change, snapshot and reference inventory, recovery proof, service-owner sign-off and bounded mutation scope. The offline validator does not establish any of these.

| Failure | What to inspect first | Safe response | Do not |
|---|---|---|---|
| Concurrent `rewrite_data_files` commit conflict | Catalog current snapshot ID and rewritten input-file references | Reconcile changed files and retry only when Iceberg's rewrite validation conditions still hold; otherwise replan canary | Blindly replay a rewrite after a timeout |
| Successful partial-progress rewrite then task failure | Snapshot history and number of committed file groups | Inventory already-committed groups, verify query invariants and scope retries to remaining groups | Treat job failure as all-or-nothing |
| Manifest rewrite with unchanged planning time | Before/after plans, manifest sizes, partition layout and reader cache | Check stats and plan cache; stop if savings cannot justify write load | Repeat large rewrite by default |
| Snapshot expiration exceeded required history | Active refs, surviving snapshots and backup/PITR points | Freeze cleanup and recover from separately validated backup if possible; declare inability to rollback when files are gone | Claim metadata pointer rollback restores deleted data |
| Orphan candidates include active writer files | Writer duration, outstanding checkpoints, object modification times, path equivalence | Stop deletion; increase safety interval and re-run read-only listing | Use short default retention or force mismatched prefix deletion |
| Catalog timeout or unknown commit result | Latest catalog metadata pointer, reference snapshot, writer logs | Determine whether the commit landed before attempting an idempotent recovery | Treat a client timeout as proof the transaction aborted |
| Schema/partition spec changed mid-maintenance | Current spec, staged manifests and writer compatibility | Stop and replan for current spec after checking reader compatibility | Carry forward a stale predicate or spec ID |

## Staged rollout
- Staging: isolated test table created with separately owned files, concurrent writer exercises and failure injection.
- Canary: limit affected partition group(s); compare live row/business invariants and file counts; observe a bounded window.
- Promotion: widen only after measured benefit, explicit service ownership and capacity estimates.
- Abort: unexpected deletes, unexpected snapshot movement, unresolved commit status, legal hold conflict, authorisation gap or broken business invariant.

## Evidence to retain
Change ticket, catalog/engine versions, snapshot ID and protected refs before and after, operation and arguments, file/delete-file metrics, dry-run candidate list, observed error messages, business invariant checks, cost/latency comparison, reviewer and restore drill evidence.

No provided script performs Spark, REST, S3 or filesystem mutations.
