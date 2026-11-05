# ds-survey-sampling-design: specialist evaluation and negative controls

Domain `data/data-science/statistics-advanced`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Document the target population, sampling frame, unit selection stages, strata, clusters and inclusion probabilities.
2. Distinguish base design weights from nonresponse-adjusted, calibrated, post-stratified or trimmed final weights. Preserve the weight construction metadata.
3. Assess frame undercoverage, nonresponse, extreme weights, positivity and the difference between the sample and target population.
4. Declare the full survey design before estimating totals, means, proportions, regression or subgroup/domain estimates.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not assume weighting removes nonresponse or coverage bias.
- Do not use unweighted sample counts as population totals.
- Do not treat weights as frequency weights unless that interpretation is correct.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://r-survey.r-forge.r-project.org/pkgdown/docs/index.html
- https://stat.ethz.ch/CRAN/web/packages/survey/index.html
- https://r-survey.r-forge.r-project.org/pkgdown/docs/reference/svydesign.html
- https://search.r-project.org/CRAN/refmans/survey/html/svydesign.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
