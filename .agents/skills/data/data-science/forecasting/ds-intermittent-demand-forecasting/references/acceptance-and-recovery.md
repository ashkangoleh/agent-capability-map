# ds-intermittent-demand-forecasting: specialist evaluation and negative controls

Domain `data/data-science/forecasting`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Classify every time bucket: **observed true zero**, positive demand, **stockout-censored**, missing feed, inactive/discontinued product or unobserved prelaunch period. A zero sale during an outage is not a zero demand label. Reject contaminated periods until their observation mechanism is resolved.
2. Profile nonzero frequency, `ADI = number of eligible buckets / nonzero eligible buckets`, nonzero demand sizes, series history and lifecycle. All-zero series have undefined ADI and size, **not** automatic proof of permanent obsolescence. Document grouping threshold heuristics as descriptive, not immutable business classes.
3. Compare a credible simple baseline and Croston-family variants (Croston, bias-adjusted SBA, TSB) plus ADIDA/IMAPA when supported by the installed StatsForecast release. Croston-family outputs are not automatically probabilistic demand distributions.
4. For obsolescence, TSB-style methods separately update **demand occurrence probability every period** and demand size on positive periods; verify how changing occurrence probability and item retirement are reflected in the target version.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Unknown stockout history or missing observation state → decline a precise true-demand forecast until data provenance is reconciled.
- Very few nonzero periods or entirely zero history → mark unstable/undefined size and ADI; report cold-start or obsolescence uncertainty.
- Abrupt changes in occurrence rate or lifecycle → review model class/fallback; do not mechanically extrapolate past positive events.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://nixtla.github.io/statsforecast/
- https://github.com/Nixtla/statsforecast
- https://help.sap.com/docs/SAP_HANA_PLATFORM/319d36de4fd64ac3afbf91b1fb3ce8de/croston-tsb-method-8203847.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
