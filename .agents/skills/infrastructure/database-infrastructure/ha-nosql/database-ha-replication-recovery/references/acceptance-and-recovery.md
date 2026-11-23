# database-ha-replication-recovery: specialist evaluation and negative controls

Domain `infrastructure/database-infrastructure/ha-nosql`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define failure model and RPO/RTO for process, host, AZ and region; distinguish sync from async guarantees.
2. Design election, quorum, fencing, split-brain prevention, lag thresholds and read/write endpoints.
3. Configure WAL/binlog archive, base backups, encryption, retention and immutable/offsite copies.
4. Set pooling, retry and endpoint behavior to avoid duplicate transactions and retry storms.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Async promotion may lose acknowledged writes; state the real RPO.
- No fencing can create dual primaries and corruption.
- Untested backup is unproven recovery.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.postgresql.org/docs/current/high-availability.html
- https://dev.mysql.com/doc/refman/8.4/en/replication.html
- https://www.pgbouncer.org/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
