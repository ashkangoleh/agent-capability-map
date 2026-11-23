# dbt-incremental-modeling: specialist evaluation and negative controls

Domain `data/analytics-engineering/dbt`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Inspect the actual dbt model, adapter version, source schema and table contract. Verify supported materializations and incremental strategies against that adapter, not merely against generic dbt docs.
2. State a non-null, unique model grain and verify source and target duplicates. A configured unique_key alone does not make upstream records unique or guarantee idempotency.
3. Specify a bounded incremental filter and a deliberate late-arriving/updated-record window. Explain how initial full builds, schema drift and historical corrections differ from a normal incremental run.
4. Choose append, merge, delete+insert or insert_overwrite only when supported by the target adapter and appropriate to the grain. Make concurrent writers, retries, partial failures and downstream readers explicit.

## Challenge / acceptance
- **Challenge:** Rebuild after dimension key change, partial refresh or late facts. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Source-to-model uniqueness, historical grain and test-controlled business totals align. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
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
- https://docs.getdbt.com/docs/build/incremental-models
- https://docs.getdbt.com/docs/build/data-tests
- https://docs.getdbt.com/docs/build/incremental-strategy

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
