# ds-missing-data: specialist evaluation and negative controls

Domain `data/data-science/statistics-advanced`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
- Unit of analysis, target estimand, variables with missing values and missingness indicators.
- Collection process, time ordering, data source, eligibility and reasons for absence.
- Whether the task is descriptive, inferential or predictive, and whether missing values are structural, not applicable, censored or genuinely unobserved.

## Preserve skill-specific method
1. Profile missingness by variable, row, time, source, outcome, treatment and important subgroups. Check whether missingness itself is informative.
2. Separate structural absence, not-applicable values, source outages, delayed arrival, censoring and nonresponse. Do not impute these as if they were the same mechanism.
3. State the plausible mechanism: MCAR, MAR conditional on observed variables, or MNAR depending on unobserved values. These assumptions are not generally identifiable from observed data alone.
4. Define the estimand and compare complete-case analysis, likelihood-based methods, inverse-probability weighting and imputation against that estimand.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not replace missing values with zero unless zero is the actual observed meaning.
- Do not impute across time or entity boundaries using future information.
- Do not hide high missingness behind a single overall percentage.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://scikit-learn.org/stable/modules/impute.html
- https://stefvanbuuren.name/fimd/
- https://search.r-project.org/CRAN/refmans/mice/html/pool.html
- https://www.statsmodels.org/stable/imputation.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
