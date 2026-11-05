# ds-hierarchical-forecasting: specialist evaluation and negative controls

Domain `data/data-science/forecasting`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define the **aggregation graph** for a specific version and period. Validate that every bottom series has a stable unique ID and the intended mapping to parents; detect overlaps, renamed IDs, unmatched items and changing catalog/country boundaries. Distinguish additive measurements (units/revenue) from averages/ratios that cannot simply be summed.
2. Construct the summing matrix `S` mapping bottom-level values to all requested levels and verify the **actual historical observations** satisfy `y_all = S @ y_bottom` before comparing any reconciler. Do not use naive addition for different time units, currencies or partially observed groups.
3. Generate baseline/advanced **unreconciled** predictions with identical rolling origins and horizons. Test BottomUp, TopDown or MinTrace only where supported by the installed HierarchicalForecast version and sample covariance quality.
4. For linear reconciliation, distinguish reconciled forecasts `S @ (P @ base_forecasts)` from **already coherent** bottom-up totals. Check rank/conditioning and covariance stability; small, sparse or changing hierarchies make empirical error covariance unreliable.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Non-additive measures, mismatched units/time periods or duplicate parent members → refuse naive sum; repair the business aggregation contract.
- Incoherent base predictions, unstable covariance or insufficient historical data → compare against BottomUp and freeze unsupported reconcilers.
- Hierarchy version drift or missing bottom series → quarantine affected forecasts until mapping/source completeness is restored.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://nixtla.github.io/hierarchicalforecast/
- https://github.com/Nixtla/hierarchicalforecast
- https://otexts.com/fpp3/hierarchical.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
