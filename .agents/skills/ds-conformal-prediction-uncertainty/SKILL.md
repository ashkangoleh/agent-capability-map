---
name: ds-conformal-prediction-uncertainty
description: "Audit split-conformal prediction intervals and sets with finite-sample order statistics, independent calibration, exchangeability assumptions, subgroup and shift checks."
metadata:
  version: "1.1.0"
---

# ds-conformal-prediction-uncertainty

## Activation boundary

Use for **predictive coverage** of a future regression outcome or a set of classification labels, including conformal residual scores, calibration rank, coverage under exchangeability, and prediction-set width. A conformal prediction interval is **not** a confidence interval for a model parameter, a Bayesian credible interval, a calibrated class probability or a promise of individual-level coverage. For forecasting under temporal dependence, first verify an appropriate time-series conformal method; the IID split-conformal rule is not automatically valid. For probability reliability and threshold selection, use `ds-model-calibration`.

## Required context

Target/label and timestamp; exact prediction horizon; model-fitting/tuning, conformalization/calibration and untouched evaluation partitions; observation/entity IDs; independent/exchangeable unit; time/group dependence; expected drift; confidence level `1-alpha`; nonconformity score; subgroup sample sizes; relevant library versions and source data provenance.

## Production workflow

1. Define the estimand as **marginal predictive coverage** or a specific stronger risk/conditional statement. Specify the future population; test whether calibration and deployment observations can plausibly be exchangeable. Flag dependence, cluster sampling, nonstationarity, delayed outcomes and changing data sources instead of silently declaring IID.
2. Freeze model fitting and hyperparameter selection **before** using conformal calibration labels. Keep training, conformalization and final evaluation records disjoint, including indirect duplicates and any group/time constraints required by the deployment task. The example auditor checks only observation IDs, not exchangeability or source integrity.
3. Choose the correct procedure for the target: split absolute-residual conformal for simple regression, LAC/APS or another justified method for classification labels, or a version-verified time/group-aware approach when ordinary exchangeability fails. Never apply a regression residual quantile to class probabilities and call it calibrated classification.
4. For split regression with `n` nonnegative calibration absolute residuals `s_i`, calculate `k = ceil((n+1)*(1-alpha))` and select the **k-th smallest** score; do **not** interpolate the empirical quantile. If `k>n`, a finite guaranteed radius is unavailable with this rule (an unbounded interval is the theoretical fallback). Fail closed rather than substituting the largest score and claiming a nominal finite-sample guarantee.
5. For a new prediction `y_hat`, report the symmetric interval `[y_hat-q, y_hat+q]` and its assumptions. Evaluate empirical coverage, interval widths and miss patterns only on untouched evaluation labels; record subgroup counts and uncertainty by time/entity/class and source. A single observed coverage rate is noisy and not a finite-sample theorem.
6. Examine the failure modes of marginal coverage: coverage may be too low for certain classes, periods, geographies or under distribution shift. Group-specific or weighted/adaptive methods require distinct assumptions and validated methods; avoid silently upgrading marginal guarantees to conditional or individual guarantees.
7. Record original model version, scores, calibration window, quantile rank, alpha, nonconformity definition, dataset hashes, evaluation method, reproducible code, subgroup analyses, widths and explicit conditions under which the formal guarantee does **not** apply.
8. When using MAPIE, **pin the installed version**: MAPIE v1 introduced substantial API changes. Follow the installed release's `SplitConformalRegressor`, `conformalize` and `predict_interval` documentation, not old `MapieRegressor` examples by assumption. Confirm supported conformity scores and time-series features in that release.

## Runnable, bounded validation example

From repository root (Python 3.10+, standard library only):

```python
from examples.data_science.uncertainty_integrity import (
    audit_partitions,
    split_conformal_radius,
    regression_interval_report,
)

audit_partitions(["train-1"], ["cal-1", "cal-2", "cal-3", "cal-4",
                               "cal-5", "cal-6", "cal-7", "cal-8", "cal-9"],
                 ["evaluation-1", "evaluation-2"])
q = split_conformal_radius([1, 3, 2, 4, 5, 6, 7, 9, 8], alpha=0.1)
assert q["rank"] == 9 and q["radius"] == 9
observed = regression_interval_report([4, 20], [5, 5], radius=q["radius"])
assert observed["covered"] == 1
```

These numbers are **illustrative arithmetic**, not measured performance from a real trained model. The audit cannot establish independence of identical entities under different IDs, correct feature timestamps, exchangeability, or valid temporal/conditional guarantees.

## Failure modes and abstention

- Calibration data used to fit/tune the model or choose the score → contaminated guarantees; rebuild disjoint partitions and rerun.
- `k>n` or low subgroup sample sizes → insufficient support for a finite radius or subgroup claim; record the limitation rather than invent a coverage value.
- Clustered/repeated entities, autocorrelation or distribution shift → standard exchangeability guarantee may fail; require a separately justified design and coverage evidence.
- Parameter confidence intervals, Bayesian credible intervals or reliability/calibration of probabilities → wrong output contract; route to the appropriate statistical/probability skill.
- Adaptive re-calibration on test outcomes → test no longer untouched; create a new prospective holdout.

## Validation and evidence

- [ ] Partition/provenance/label availability records verified.
- [ ] Exchangeability and deployment population assumptions explicit.
- [ ] Rank, score, requested coverage and finite-sample conditions recorded.
- [ ] Untouched evaluation coverage, width and subgroup/time diagnostics reported.
- [ ] Failure and abstention cases reproducible; runtime/library versions pinned.

## Output contract

Return the target/coverage contract, partitions, chosen method and assumptions, finite-sample quantile evidence, empirical evaluation with uncertainty, residual failure modes, version-specific implementation and explicit refusal of unsupported conditional guarantees.

## Authoritative references

- https://mapie.readthedocs.io/en/stable/content/conformal-prediction/conformity-scores/
- https://mapie.readthedocs.io/en/stable/content/getting-started/choosing-algorithm/
- https://mapie.readthedocs.io/en/stable/api/regression/
