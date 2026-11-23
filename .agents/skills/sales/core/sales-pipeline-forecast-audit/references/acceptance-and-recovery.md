# sales-pipeline-forecast-audit: specialist evaluation and negative controls

Domain `sales/core`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define opportunity grain, stage entry/exit rules, booking recognition and forecast period.
2. Validate duplicates, missing amounts, stale stages, contradictory close dates and reopen cycles.
3. Calculate stage conversion and cycle time from timestamped history; distinguish observed win rates from guessed probabilities.
4. Develop deterministic, weighted and scenario forecasts with explicit assumptions and cohort limits.

## Challenge / acceptance
- **Challenge:** Change opportunity stage, forecast probability or consent status. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Forecast calibration and contact permission evidence match CRM records. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No guaranteed quota or unauthorized customer outreach. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://trailhead.salesforce.com/content/learn/trails/salesforce_sales_cloud

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
