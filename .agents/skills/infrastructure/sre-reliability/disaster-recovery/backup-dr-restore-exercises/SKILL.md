---
name: backup-dr-restore-exercises
description: "Design and test infrastructure backup, failover and restoration against explicit RPO/RTO."
metadata:
  version: "1.1.1"
---

# backup-dr-restore-exercises

## Activation boundary
Use for infrastructure backup/restore planning, recoverability audits, disaster-recovery exercises, regional/account failover and recovery validation. Distinguish routine backup restore from service-level DR orchestration. For on-call incident timelines use the incident skill; for data-model-level replay/backfills use a Data Engineering skill. Never claim a successful backup job proves a recoverable service.

## Required context
Business service and dependency graph, data ownership, protected data types (block/object/database/config/identity), protection tools and pinned provider/runtime versions, recovery objectives (service-specific RPO and RTO), maximum tolerable outage, data residency, failure domain (disk/host/AZ/region/account/credentials), backup frequency/retention, immutable/offline/air-gapped copies and threat model, replication mode and lag, consistency mechanism, encryption/KMS keys and recovery IAM, restore target capacity and network/DNS/secrets dependencies, recovery runbook owner, approval, test scope, cost and rollback/failback constraints. Mark unprovided values as unknown.

## Production procedure
1. **Define recovery acceptance before tooling.** Establish service ownership, downstream dependencies, legal data retention, impact tier and failure scenarios. Define `RPO` as the maximum acceptable data-loss time window and `RTO` as the maximum acceptable time to restore the agreed service function. A backup schedule is not a measured RPO, and a completed restore job is not necessarily an achieved RTO.
2. **Build an explicit recovery-point inventory.** Record backup job completion, recovery point timestamps, retention/deletion policies, replication and cross-account/region copy lag, restore coverage of app data, metadata, manifests, databases, object versions, configuration, credentials, certificates, DNS, infrastructure-as-code state and bootstrap dependencies. Distinguish snapshots, logical exports, logs/PITR and asynchronous replicas; snapshot atomicity does not imply multi-system consistency.
3. **Protect against correlated failure.** Assess deletion/ransomware blast radius, write-once retention or vault locking where supported, separate recovery credentials/roles, key availability, audited break-glass access, regional/account independence and replication permissions. Check the actual product/resource support for immutable or logically air-gapped copies and cross-account/region restores. Do not assume a replicated but writable backup is isolated.
4. **Choose a verifiable test point.** Select a dated recovery point at or before the desired recovery timestamp and document all incremental/log dependencies. Verify media integrity, encryption/key usability, transport availability and restoration permissions before scheduling. Build isolated target accounts/namespaces/VPCs with quota, compute/storage capacity and matching critical versions; block accidental writes to production and prevent restores from emitting real emails, payments or notifications.
5. **Plan dependency-ordered restore.** Restore and verify network/IAM/DNS/KMS/secret prerequisites, then storage and databases with transaction-consistent sequencing, then stateful infrastructure, applications, controllers and ingress. Where distributed services are involved, reconcile checkpoint/LSN/binlog positions and inter-system references; decide whether to replay logs/transactions, rehydrate indexes or quarantine inconsistent state. Treat PITR and replay as source-specific and test idempotency before enabling writers.
6. **Execute a bounded drill.** Obtain approval and capture start time for the defined outage scenario. Restore into an isolated environment, record restore job IDs, source point timestamps, infrastructure readiness, application-level serving times and every blocked dependency. Keep recovery traffic isolated until verified, with explicit abort gates for corrupt data, unexpected KMS access, excess cost, identity failures or lost isolation. In AWS, automated restore-testing plans and optional post-restore validation can help schedule and capture job evidence, but availability depends on resource type and provider; restoring a resource is not the same as validating the service.
7. **Validate end to end.** Check data integrity (checksums/sample queries/record counts and relational consistency as appropriate), authorized reads/writes, service and business transactions, auth/certificates, downstream queue offsets, replicas and alerts. Verify that jobs, integration callbacks and externally visible side effects do not double-execute. Perform a controlled failover/failback rehearsal only when it is safe and explicitly approved; avoid silent split-brain or dual writers.
8. **Measure against objectives.** For the simulated disaster time `T_failure`, recover the latest **validated application-consistent** point `T_recovery_point`. Report observed data-loss window `T_failure - T_recovery_point` with assumptions about replication/app commit semantics; calculate service-level recovery duration from the chosen trigger until the defined user-visible function passes. Compare actual observed values with the agreed RPO/RTO. Distinguish restore-job elapsed time, warm-up, network failover and final business readiness.
9. **Exit with evidence.** Record PASS/FAIL/UNKNOWN for each service dependency, data-integrity control and recovery objective; document missing backup scope, KMS/cross-region restrictions, point-in-time gaps, overrun, failback readiness, cleanup owner, cost and next exercise cadence. Keep tested recovery runbooks and immutable evidence; clean up isolated test resources intentionally and verify deletion/cost termination.

## Failure modes and recovery
- **Backup is present but unusable:** missing incremental/log chain, wrong restore engine/version, corrupted object, unavailable keys or expired credentials. Abort unsafe cutover and select a verified alternative point; disclose the increased potential data-loss window.
- **RPO breach:** gaps between eligible/validated points or replication lag. Measure the actual last consistent point; do not substitute the most recent successful backup timestamp without integrity proof.
- **RTO breach:** slow restore throughput, unavailable compute or network, third-party auth/DNS/KMS dependencies and insufficient rehearsal. Report phase-by-phase timings and bottlenecks rather than promising a faster untested run.
- **Security boundary or ransomware compromise:** compromised admin accounts, shared credentials or mutable replicas invalidate the presumed isolated copy. Quarantine restore targets and validate provenance and key/access boundaries before recovering.
- **Inconsistent distributed state / split brain:** partial database commits, unaligned snapshot boundaries, two writers during failover or duplicate downstream effects. Preserve evidence; halt writers, reconcile checkpoints and transaction boundaries, then use an approved recovery/failback decision.
- **Test environment leakage:** live customer access, production callbacks, uncontrolled cleanup and unexpected charges. Block egress/production credentials, contain the test, preserve test evidence and perform audited cleanup.

## Validation and evidence
Deliver an auditable recovery table per service: `failure_scenario`, `backup_coverage`, `source_point_time`, `validated_point_time`, `restore_start`, `service_ready_time`, `measured_rpo`, `measured_rto`, `target_rpo`, `target_rto`, `integrity_status`, `dependency_checks`, `pass_fail_unknown`, `owner`, `next_action`. Include job IDs, logs, verification queries/results and costs if observed. Mark dry-run planning versus executed exercises explicitly. No provider-specific feature or recovery claim without version/resource-specific evidence.

## Official references
- https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html
- https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-validation.html
- https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/test.html
- https://docs.aws.amazon.com/aws-backup/latest/devguide/logicallyairgappedvault.html
- https://cloud.google.com/architecture/dr-scenarios-planning-guide

## Output contract
Return a service-scoped recovery/restore plan and evidence record with explicit assumptions, RPO/RTO calculations, recovery-point and dependency checks, security/consistency gates, measured validation results, abort and failback procedure, residual risks, cost and named approver. Do not fabricate restoration or operational outcomes.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
