# backup-dr-restore-exercises: specialist evaluation and negative controls

Domain `infrastructure/sre-reliability/disaster-recovery`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. **Define recovery acceptance before tooling.** Establish service ownership, downstream dependencies, legal data retention, impact tier and failure scenarios. Define `RPO` as the maximum acceptable data-loss time window and `RTO` as the maximum acceptable time to restore the agreed service function. A backup schedule is not a measured RPO, and a completed restore job is not necessarily an achieved RTO.
2. **Build an explicit recovery-point inventory.** Record backup job completion, recovery point timestamps, retention/deletion policies, replication and cross-account/region copy lag, restore coverage of app data, metadata, manifests, databases, object versions, configuration, credentials, certificates, DNS, infrastructure-as-code state and bootstrap dependencies. Distinguish snapshots, logical exports, logs/PITR and asynchronous replicas; snapshot atomicity does not imply multi-system consistency.
3. **Protect against correlated failure.** Assess deletion/ransomware blast radius, write-once retention or vault locking where supported, separate recovery credentials/roles, key availability, audited break-glass access, regional/account independence and replication permissions. Check the actual product/resource support for immutable or logically air-gapped copies and cross-account/re

## Challenge / acceptance
- **Challenge:** Inject node failure, overload and restore from checkpoint. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Error budget, recovery and customer impact measured with on-call escalation. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - **Backup is present but unusable:** missing incremental/log chain, wrong restore engine/version, corrupted object, unavailable keys or expired credentials. Abort unsafe cutover and select a verified alternative point; disclose the increased potential data-loss window.
- **RPO breach:** gaps between eligible/validated points or replication lag. Measure the actual last consistent point; do not substitute the most recent successful backup timestamp without integrity proof.
- **RTO breach:** slow restore throughput, unavailable compute or network, third-party auth/DNS/KMS dependencies and insufficient rehearsal. Report phase-by-phase timings and bottlenecks rather than promising a faster untested run.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html
- https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-validation.html
- https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/test.html
- https://docs.aws.amazon.com/aws-backup/latest/devguide/logicallyairgappedvault.html
- https://cloud.google.com/architecture/dr-scenarios-planning-guide

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
