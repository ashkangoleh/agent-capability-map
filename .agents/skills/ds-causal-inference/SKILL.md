---
name: ds-causal-inference
description: Use when selecting and defending a causal identification design for an intervention, policy, product change, or observational treatment.
metadata:
  version: "1.1.0"
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
