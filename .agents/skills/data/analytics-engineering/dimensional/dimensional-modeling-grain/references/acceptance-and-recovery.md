# dimensional-modeling-grain: specialist evaluation and negative controls

Domain `data/analytics-engineering/dimensional`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. State each business process and fact grain in a single unambiguous sentence; disallow a fact table with mixed grains without an explicit bridge.
2. Choose transaction, periodic snapshot or accumulating snapshot fact as supported by the source events.
3. Define conformed dimensions, natural/surrogate keys and SCD types; handle unknown/late arriving dimension references explicitly.
4. Specify additive/semi-additive/non-additive metrics with time and category aggregation behavior; do not blindly sum ratios.

## Challenge / acceptance
- **Challenge:** Rebuild after dimension key change, partial refresh or late facts. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Source-to-model uniqueness, historical grain and test-controlled business totals align. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Validate fact grain uniqueness and business reconciliation against source orders/transactions.
- Run representative BI queries and inspect aggregation correctness.
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
- https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview
- https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
