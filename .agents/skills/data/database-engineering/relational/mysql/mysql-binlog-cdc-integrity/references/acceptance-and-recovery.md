# mysql-binlog-cdc-integrity: specialist evaluation and negative controls

Domain `data/database-engineering/relational/mysql`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Inspect actual binary log configuration, source replica permissions and existing consumer positions.
2. Choose consistent snapshot boundary and binlog or GTID resume semantics validated for the chosen connector.
3. Protect source disk via retention and lag monitoring, avoiding premature log purging.
4. Review row images, deletes, schema changes, key changes and timezone/decimal conversions.

## Challenge / acceptance
- **Challenge:** Fail a transaction after partial client timeout and replay a CDC change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Commit outcome, isolation and data invariants reconcile without blind retry. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://dev.mysql.com/doc/refman/8.4/en/binary-log.html
- https://dev.mysql.com/doc/refman/8.4/en/replication-gtids.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
