# dbt-snapshot-scd2: specialist evaluation and negative controls

Domain `data/analytics-engineering/dbt`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Clarify whether point-in-time history is required and whether source is mutable or already a changelog; compare snapshots vs incremental-only design.
2. Validate non-null uniqueness at source grain and timestamp quality; incorrect keys cause duplicate or merged histories.
3. Choose supported timestamp/check strategy and columns tracked; define how unchanged/no-op records, late updates and null changes are handled.
4. Specify valid_from/valid_to interval semantics, current-row marker, hard-delete handling and clock/timezone consistency.

## Challenge / acceptance
- **Challenge:** Rebuild after dimension key change, partial refresh or late facts. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Source-to-model uniqueness, historical grain and test-controlled business totals align. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Assert one current row per key and non-overlapping history intervals.
- Reconcile current snapshot view with source and validate historical point-in-time queries.
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
- https://docs.getdbt.com/docs/build/snapshots
- https://docs.getdbt.com/best-practices/how-we-handle-cdc/2-choosing-incremental-or-snapshots

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
