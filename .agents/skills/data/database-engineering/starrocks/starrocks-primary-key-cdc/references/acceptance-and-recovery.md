# starrocks-primary-key-cdc: specialist evaluation and negative controls

Domain `data/database-engineering/starrocks`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Inspect actual source changelog grain, event key and mutable fields; verify StarRocks table type and exact engine version.
2. Choose Primary Key columns and distribution/sort keys from uniqueness and query patterns; keys are non-null and updates replace matching key rows.
3. Specify UPSERT and DELETE event handling, key changes, soft deletes, null/unset fields and out-of-order delivery.
4. Evaluate full vs partial update behavior and conditional merge semantics; verify version prerequisites and new-key partial update defaults.

## Challenge / acceptance
- **Challenge:** Fail a transaction after partial client timeout and replay a CDC change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Commit outcome, isolation and data invariants reconcile without blind retry. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Compare destination latest-row state to source point-in-time state.
- Inspect PK index, query plans and load rejects with actual workload.
- Include edge cases, timeouts and partial failures where material; do not claim tests executed without tool traces.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.starrocks.io/docs/table_design/table_types/primary_key_table/
- https://docs.starrocks.io/docs/loading/Load_to_Primary_Key_tables/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
