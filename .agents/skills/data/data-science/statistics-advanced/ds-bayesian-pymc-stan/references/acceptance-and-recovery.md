# ds-bayesian-pymc-stan: specialist evaluation and negative controls

Domain `data/data-science/statistics-advanced`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
- Scientific question, target population, unit of analysis, estimand and decision.
- Outcome likelihood, predictors, hierarchy, missingness and dependence structure.
- Prior knowledge, plausible parameter scales, computational budget and required precision.

## Preserve skill-specific method
1. Write the generative model before writing code: data likelihood, parameter hierarchy, link functions, transformations and conditional dependencies.
2. Check identifiability and parameterization. Distinguish weak identification from sampler failure; consider centered versus non-centered parameterizations for hierarchical effects.
3. Perform prior predictive simulation. Reject priors that imply impossible scales, rates, counts, tails or group variation before fitting observed data.
4. Fit multiple independently initialized chains. Record warmup, draws, sampler, adaptation settings, random seeds and divergences.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not report estimates from chains with unresolved convergence or material divergences.
- Do not select priors solely because they make the sampler run.
- Do not use a single posterior predictive plot as complete model validation.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.pymc.io/projects/docs/en/stable/
- https://mc-stan.org/docs/stan-users-guide/
- https://python.arviz.org/en/stable/
- https://python.arviz.org/projects/stats/en/latest/api/generated/arviz_stats.diagnose.html
- https://www.pymc.io/projects/docs/en/stable/learn/usage_overview.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
