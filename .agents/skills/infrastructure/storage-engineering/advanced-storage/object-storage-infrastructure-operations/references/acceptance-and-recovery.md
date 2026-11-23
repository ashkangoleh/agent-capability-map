# object-storage-infrastructure-operations: specialist evaluation and negative controls

Domain `infrastructure/storage-engineering/advanced-storage`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define bucket/tenant boundaries, ownership, encryption, versioning, retention and access policies.
2. Choose durability and failure-domain layout; model replication, erasure coding, repair bandwidth and capacity.
3. Set lifecycle, multipart cleanup, object lock/legal hold and deletion protections with owners.
4. Validate API compatibility, signing, TLS, retry behavior and client SDK versions.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - S3-compatible does not mean identical semantics; test conditional and multipart behavior.
- Lifecycle expiration can permanently delete data; require restore proof.
- Replication lag can leave failover stale; expose RPO.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
- https://docs.ceph.com/en/latest/radosgw/
- https://min.io/docs/minio/linux/index.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
