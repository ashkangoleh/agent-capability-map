# ds-ab-experimentation: specialist evaluation and negative controls

Domain `data/data-science/experimentation`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
- Hypothesis, primary estimand, primary metric and guardrail metrics.
- Randomization unit, eligibility, assignment and exposure timestamps.
- Baseline rate/variance, expected effect, alpha, power, allocation ratio and planned duration.
- Clustering, repeated users, network interference, seasonality and experiment overlap.

## Preserve skill-specific method
1. Pre-register the hypothesis, primary outcome, guardrails, eligibility, randomization unit, analysis population and stopping rule.
2. Verify randomization before reading outcome effects. Check sample-ratio mismatch overall and by key strata, assignment/exposure parity, duplicate assignments, contamination and attrition.
3. Estimate power and minimum detectable effect using the actual randomization unit. Inflate for clustering, repeated measures, attrition and multiplicity when appropriate.
4. Use intent-to-treat as the primary estimate. Report treatment-on-treated or per-protocol estimates only as secondary analyses with explicit assumptions.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Pause interpretation when assignment integrity or exposure logging is broken.
- Do not stop early because a nominal p-value crossed 0.05 unless the stopping rule supports it.
- Do not use user-level standard errors for cluster-randomized assignment without accounting for clusters.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.statsig.com/perspectives/ab-testing-statistics
- https://www.statsmodels.org/stable/stats.html
- https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
