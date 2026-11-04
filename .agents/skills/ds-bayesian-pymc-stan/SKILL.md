---
name: ds-bayesian-pymc-stan
description: Use when specifying, fitting, diagnosing, comparing, or reporting Bayesian models with PyMC or Stan.
metadata:
  version: "1.1.0"
---

# ds-bayesian-pymc-stan

## Activation boundary

Use for Bayesian generative modeling, hierarchical partial pooling, posterior inference, prior sensitivity, or MCMC diagnostics. Do not use for ordinary frequentist tests or for predictive ML calibration without a Bayesian model.

## Required context

- Scientific question, target population, unit of analysis, estimand and decision.
- Outcome likelihood, predictors, hierarchy, missingness and dependence structure.
- Prior knowledge, plausible parameter scales, computational budget and required precision.

## Workflow

1. Write the generative model before writing code: data likelihood, parameter hierarchy, link functions, transformations and conditional dependencies.
2. Check identifiability and parameterization. Distinguish weak identification from sampler failure; consider centered versus non-centered parameterizations for hierarchical effects.
3. Perform prior predictive simulation. Reject priors that imply impossible scales, rates, counts, tails or group variation before fitting observed data.
4. Fit multiple independently initialized chains. Record warmup, draws, sampler, adaptation settings, random seeds and divergences.
5. Diagnose the sampler before interpreting posterior summaries: rank-normalized split R-hat, bulk and tail ESS, Monte Carlo standard error, trace/rank plots, divergences, tree-depth saturation and energy/BFMI diagnostics where applicable.
6. Investigate every divergence or poor-mixing parameter. Revisit geometry, scaling, priors and parameterization; increasing draws alone is not a repair.
7. Run posterior predictive checks targeted to the scientific question: location, dispersion, tails, zero frequency, extremes, group-level variation and temporal dependence.
8. Compare models only when their likelihoods and predictive targets are comparable. Use PSIS-LOO or another justified predictive criterion, inspect Pareto-k diagnostics, and prefer simpler models when differences are not decisive.
9. Perform prior and likelihood sensitivity analyses. Report posterior intervals and decision-relevant contrasts, not only posterior means or probability statements.

## Decision rules

- Partial pooling is not the same as complete pooling; justify the hierarchy and group-level exchangeability.
- A credible interval describes posterior uncertainty conditional on the model and priors; it is not a frequentist confidence interval.
- Posterior predictive fit does not prove causal identification or validate the sampling process.
- A converged sampler does not rescue a misspecified likelihood or an unidentified estimand.

## MCMC diagnostic and predictive-validity gate

1. Pin PyMC/Stan and the appropriate ArviZ release: published functions, return types and diagnostics can move between `arviz`, `arviz_stats` and `arviz_plots`. Record versions before generating any executable example.
2. Calculate rank-normalized split `R-hat`, bulk/tail ESS and MCSE for all decision-critical parameters; review **divergences, maximum tree depth and BFMI** in addition to trace/rank plots. A generic threshold (often `R-hat <= 1.01`) is a screen, not proof of correct mixing or likelihood specification.
3. Prior predictive checks must inspect plausible outcome scale, tails and impossible observations **before** fitting data. Posterior predictive checks must target zero counts, groups, extreme events and temporal dependence in the **actual decision population**.
4. If Pareto-k flags influence/poor PSIS-LOO approximation, use a more appropriate refit or validation design rather than citing the unreliable criterion. Small ESS, divergences and misspecified observation mechanisms require model redesign, not merely larger numbers of draws.
5. Model-comparison results are conditioned on priors, likelihood, data selection and outcome horizon; they do not establish causal identification or fairness. Report sensitivity and abstention when required diagnostics remain unresolved.

## Failure modes and abstention

- Do not report estimates from chains with unresolved convergence or material divergences.
- Do not select priors solely because they make the sampler run.
- Do not use a single posterior predictive plot as complete model validation.
- If prior information, likelihood or identification assumptions cannot be justified, report the limitation and stop short of a decision claim.

## Validation checklist

- [ ] Generative model and estimand are explicit.
- [ ] Prior predictive checks are plausible.
- [ ] Independent chains and convergence diagnostics are reviewed.
- [ ] Posterior predictive checks target important data features.
- [ ] Sensitivity and reproducibility artifacts are retained.

## Authoritative references

- https://www.pymc.io/projects/docs/en/stable/
- https://mc-stan.org/docs/stan-users-guide/
- https://python.arviz.org/en/stable/
- https://python.arviz.org/projects/stats/en/latest/api/generated/arviz_stats.diagnose.html
- https://www.pymc.io/projects/docs/en/stable/learn/usage_overview.html
