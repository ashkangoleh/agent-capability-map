# ds-robust-nonparametric-inference: specialist evaluation and negative controls

Domain `data/data-science/statistics-advanced`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define the estimand and experimental/sampling unit. Decide whether observations are independent, paired, repeated or clustered.
2. Inspect distribution, outliers, heteroskedasticity, ties, censoring and group-size imbalance. Do not use a normality-test p-value as the sole method selector.
3. Choose a statistic aligned to the estimand: mean/trimmed mean, median, quantile, rank effect, probability of superiority or another interpretable contrast.
4. Select a procedure whose null and assumptions match the design:

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not interpret Mann-Whitney as a test of medians unless additional distribution-shape assumptions hold.
- Do not permute individual rows when randomization occurred by cluster or matched pair.
- Do not bootstrap correlated observations as IID.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.scipy.org/doc/scipy/reference/stats.html
- https://www.statsmodels.org/stable/stats.html
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
