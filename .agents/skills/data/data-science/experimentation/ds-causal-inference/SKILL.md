---
name: ds-causal-inference
description: Use when selecting and defending a causal identification design for an intervention, policy, product change, or observational treatment.
metadata:
  version: "1.2.1"
---

# ds-causal-inference

## Activation boundary

Use to choose between randomized and quasi-experimental or observational causal designs. For a narrowly observational question with an existing causal graph, use causal-inference-observational; for a standard fixed-horizon product experiment, use ds-ab-experimentation.

## Required context

Treatment/intervention, outcome, population, assignment mechanism, treatment timing, unit, interference, covariates, outcome horizon and decision.

## Workflow

1. Define the estimand before choosing an estimator: ATE, ATT, LATE, CATE, policy effect or another explicit contrast. Specify population, treatment versions and time horizon.
2. Identify the assignment mechanism. Prefer randomized assignment when feasible and ethical; otherwise explain why an observational or quasi-experimental design is credible.
3. Draw a causal DAG and distinguish pre-treatment confounders from mediators, colliders and post-treatment variables. Do not adjust mechanically for every available covariate.
4. Check consistency, exchangeability, positivity/overlap, interference and measurement assumptions relevant to the design.
5. Select a design only when its identification assumptions are defensible:
   - randomized trial: assignment integrity, compliance, attrition and interference;
   - matching/IPW or outcome regression: measured confounding and overlap;
   - doubly robust estimation: correct specification of at least one required nuisance component plus identification assumptions;
   - difference-in-differences: credible parallel trends, no anticipation and appropriate treatment-timing estimand;
   - instrumental variables: relevance, exclusion, independence and monotonicity for the stated LATE;
   - regression discontinuity: continuity around the cutoff, no precise manipulation and valid bandwidth diagnostics;
   - synthetic control: donor-pool suitability, pre-treatment fit and placebo inference.
6. Use design-specific diagnostics, placebo outcomes/treatments, pre-trend checks, overlap plots, balance and sensitivity analysis.
7. Report uncertainty at the assignment or dependence unit. Use cluster-robust or randomization-based inference where the design requires it.
8. Separate the identification argument from the estimation algorithm. Flexible ML can estimate nuisance functions; it cannot create identification from unmeasured confounding.

## Identification gate and adversarial review

1. Separate **causal identification** from **statistical estimation**. Before invoking DoWhy, DoubleML or regression, state treatment and intervention versions, population, time horizon, assignment mechanism, estimand and plausible causal graph. A good predictive model does not identify a causal effect.
2. For randomized interventions, confirm the unit of randomization, missingness, noncompliance, treatment interference and assignment integrity. If treated users self-select into logging or exposure, randomized assignment does not by itself identify the desired exposure-on-treated effect; analyze the intention-to-treat estimand first.
3. For observational designs, identify a proposed adjustment set and label assumptions as **observed**, **plausibly testable**, or **unverifiable from available data**. Explicitly review unmeasured confounding, selection/collider bias, mediator adjustment, time-varying confounders and positivity.
4. For staggered policy adoption, specify the cohort/time ATT and comparison group; a single naive two-way-fixed-effects coefficient need not equal the desired ATT with heterogeneous effects. Pre-trend non-significance is not proof of parallel trends; check anticipation and composition drift.
5. For instruments, distinguish relevance from exclusion and independence; a strong first-stage statistic alone cannot verify exclusion. For regression discontinuity, audit manipulation/density and local continuity around the cutoff. For synthetic controls, assess pre-period fit and sensitivity to donor composition.
6. For double/debiased ML, require justified identifying assumptions **in addition to** out-of-fold nuisance estimation. Review split consistency with clusters/time and overlap; cross-fitting reduces nuisance overfitting bias but cannot remove latent confounding.
7. Apply refutations and falsifications (negative controls, placebo intervention/outcomes, sensitivity bounds, alternate windows), but do not interpret a refutation test passing as proof of a true graph. If assumptions are unsupportable, output association, sensitivity ranges or `unidentified` instead of a causal point estimate.

## Evidence and output contract

Provide an auditable *identification table*: `estimand | intervention | target population | assignment | identifying assumptions | data diagnostics | refutations | inference unit | limitations`. Label unsupported assumptions explicitly. Do not construct confidence intervals or p-values from invented data, and do not convert non-significant placebo tests into positive causal proof. Cross-domain treatment assignment, sequential stopping and model deployment require the relevant dedicated skill.

## Failure modes and abstention

- Do not call predictive feature importance or an adjusted regression coefficient a causal effect without an identification argument.
- Do not select a method by package availability.
- Do not interpret a non-significant pre-trend test as proof of parallel trends.
- If positivity, exclusion, parallel trends or exchangeability is not credible, report bounds, sensitivity or descriptive association instead of a point causal claim.

## Validation checklist

- [ ] Estimand, treatment, outcome, population and time horizon are explicit.
- [ ] DAG and design assumptions are documented.
- [ ] Design-specific diagnostics and falsification checks are run.
- [ ] Standard errors respect assignment and dependence structure.
- [ ] Sensitivity and limitations are reported.

## Authoritative references

- https://mixtape.scunning.com/
- https://docs.doubleml.org/stable/guide/guide.html
- https://www.pywhy.org/dowhy/
- https://www.pywhy.org/dowhy/v0.11/user_guide/causal_tasks/estimating_causal_effects/index.html

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
