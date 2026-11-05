# data-quality-contracts: specialist evaluation and negative controls

Domain `data/quality/core`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Discover the consuming decisions and dataset grain; classify each expectation as schema, uniqueness, completeness, validity, referential integrity, volume, freshness, or cross-system reconciliation.
2. Define each metric precisely: numerator, denominator, time zone, window, acceptable nulls, threshold basis and behavior for zero rows. Do not prescribe arbitrary percentages.
3. Separate upstream data contracts from pipeline validation and downstream semantic checks; assign failure ownership and response policy for each.
4. Choose checks at boundaries with minimal query cost. Use existing engine/dbt primitives when available; do not add an orchestration/observability platform without an operational need.

## Challenge / acceptance
- **Challenge:** Inject null-key, duplicate and schema mismatch. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Fail-closed publication with clean reconciliation and actionable alert owner. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
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
- https://docs.getdbt.com/docs/build/data-tests
- https://docs.getdbt.com/docs/build/sources

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
