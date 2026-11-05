# supply-chain-demand-planning: specialist evaluation and negative controls

Domain `logistics/core`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Distinguish observed sales from latent demand and lost sales, promotions, seasonality and censored stockout periods.
2. Validate SKU/location identity, units, substitutions, returns and calendar alignment.
3. Choose simple baselines before complex forecasting; quantify forecast error using time-ordered holdouts.
4. Model inventory position, reorder timing, minimum order constraints, capacity and safety stock from stated assumptions.

## Challenge / acceptance
- **Challenge:** Introduce delayed delivery, duplicate shipment scan or lost transport handoff. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Physical and system-of-record state reconcile within a measured exception budget. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No real-world dispatch or unsafe routing action without approval. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.ascm.org/learning-development/
- https://www.oecd.org/en/topics/supply-chains.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
