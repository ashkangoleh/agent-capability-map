---
name: ds-missing-data
description: Use when diagnosing missingness mechanisms and selecting imputation, weighting, likelihood, or MNAR sensitivity methods.
metadata:
  version: "1.1.0"
---

# ds-missing-data

## Activation boundary

Use when missing observations can change an estimand, model, sample composition or operational decision. This skill covers statistical missing-data reasoning, not routine null cleanup in a data pipeline.

## Required context

- Unit of analysis, target estimand, variables with missing values and missingness indicators.
- Collection process, time ordering, data source, eligibility and reasons for absence.
- Whether the task is descriptive, inferential or predictive, and whether missing values are structural, not applicable, censored or genuinely unobserved.

## Workflow

1. Profile missingness by variable, row, time, source, outcome, treatment and important subgroups. Check whether missingness itself is informative.
2. Separate structural absence, not-applicable values, source outages, delayed arrival, censoring and nonresponse. Do not impute these as if they were the same mechanism.
3. State the plausible mechanism: MCAR, MAR conditional on observed variables, or MNAR depending on unobserved values. These assumptions are not generally identifiable from observed data alone.
4. Define the estimand and compare complete-case analysis, likelihood-based methods, inverse-probability weighting and imputation against that estimand.
5. For multiple imputation, include variables predictive of missingness and the incomplete values, preserve interactions/nonlinearities and respect the analysis model. Use appropriate variable-specific models and pool estimates with within- and between-imputation uncertainty.
6. For predictive ML, fit imputation only inside each training fold. Compare missing indicators, native missing-value handling and imputation; keep validation/test distributions untouched.
7. For plausible MNAR mechanisms, run pattern-mixture, selection-model or delta-adjustment sensitivity analyses. Report tipping points rather than presenting one untestable MNAR assumption as fact.
8. Compare estimates, uncertainty, sample composition and subgroup results across defensible scenarios.

## Decision rules

- MCAR cannot be established merely because a test is non-significant.
- Complete-case analysis may change the target population and can be biased outside restrictive conditions.
- Single deterministic imputation understates uncertainty for many inferential tasks.
- Multiple imputation does not automatically solve MNAR or model misspecification.
- Weighting requires positivity and a defensible response/observation model.

## Failure modes and abstention

- Do not replace missing values with zero unless zero is the actual observed meaning.
- Do not impute across time or entity boundaries using future information.
- Do not hide high missingness behind a single overall percentage.
- If the missingness mechanism materially changes the conclusion and cannot be bounded, report the conclusion as non-identified or sensitivity-dependent.

## Validation checklist

- [ ] Missingness is profiled by time, source and subgroup.
- [ ] Structural missingness is separated from nonresponse.
- [ ] Mechanism assumptions are explicit and qualified.
- [ ] Imputation/weighting respects the data design and validation split.
- [ ] MNAR sensitivity is reported when material.

## Authoritative references

- https://scikit-learn.org/stable/modules/impute.html
- https://stefvanbuuren.name/fimd/
