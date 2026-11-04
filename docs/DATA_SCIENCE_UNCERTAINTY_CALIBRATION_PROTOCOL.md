# Data Science: Conformal Prediction & Probability Calibration

**Date:** 2026-11-05  
**Canonical branch:** `pre_release`  
**Domain:** `data/data-science`  
**State:** Implemented specialist hardening and arithmetic diagnostics; **not independently production-certified**.

## Scope and key distinctions

The existing `ds-conformal-prediction-uncertainty` and `ds-model-calibration` specialists are reused. They solve **different uncertainty questions**:

| Question | Specialist | Evidence required |
|---|---|---|
| What prediction interval/set has marginal coverage under declared assumptions? | `ds-conformal-prediction-uncertainty` | Independent conformalization scores; exchangeability; finite-sample quantile; holdout empirical coverage |
| Are binary class predictions reliable event probabilities? | `ds-model-calibration` | Independent base-model/calibrator split; reliability bins, proper scores and discrimination |
| Does a regression *parameter* confidence interval include an unknown coefficient? | `statistical-inference-design` | Inferential sampling/estimand assumptions, not a conformal predictive interval |
| Is a Bayesian parameter interval credible under a posterior model? | `ds-bayesian-pymc-stan` | Posterior/prior and convergence assumptions, not a frequentist prediction-set guarantee |
| Are the forecast's temporal predictive quantiles accurate? | `ds-probabilistic-forecasting` | Rolling-origin, horizon, pinball/coverage under temporal dependence |
| Are model errors equitable across groups? | `ds-fairness-subgroup-evaluation` | Disaggregated metrics, uncertainty and context; marginal conformal coverage does not establish fairness |

A single well-scoring (or low-Brier) classifier may remain miscalibrated; a marginally valid interval may have poor subgroup coverage. No single metric proves all requirements.

## Split-conformal finite-sample arithmetic

For a *fixed model* and `n` independent conformalization residual scores, if calibration and a future test observation are exchangeable under the relevant setup, the usual split-conformal rank for nominal miscoverage `alpha` is:

```text
k = ceil((n + 1) * (1 - alpha))
q = sorted(abs_residuals)[k - 1]  # 1-based k, no interpolation
interval = [y_hat - q, y_hat + q]
```

The simple **symmetric absolute-residual regression** method is implemented by `examples/data_science/uncertainty_integrity.py`. If `k>n`, a finite interval is not supplied by this finite-score quantile rule: the code raises rather than silently using the maximum observed residual while asserting the target guarantee. An infinite interval is a theoretical alternative with no operational usefulness.

Do **not** use that regression-specific code for classification labels, multi-output intervals, weighted, clustered, nonexchangeable or time-series data and claim the same theorem. The code does not fit a model and cannot verify underlying exchangeability.

### Example

```python
from examples.data_science.uncertainty_integrity import (
    audit_partitions,
    split_conformal_radius,
    regression_interval_report,
)

assert audit_partitions(["train"], ["cal-a", "cal-b"], ["holdout"])["evaluation_rows"] == 1
q = split_conformal_radius(range(1, 20), alpha=0.2)
assert q["rank"] == 16 and q["radius"] == 16
result = regression_interval_report([1, 3], [2, 2], radius=q["radius"])
assert result["empirical_coverage"] == 1.0
```

These are **hand-constructed arithmetic examples**, not benchmark measurements of a learned model. Partition checking is row-ID disjointness only: duplicates under other IDs, labels arriving after the prediction time, shared entities, transformation leakage or temporal dependency require separate controls.

## Probability calibration: correct data contract

1. Establish positive-label semantics, model score type, outcome horizon and target population.
2. Keep model fitting/tuning, calibration mapping and final evaluation disjoint **at the relevant unit/time scope**, or obtain unbiased calibration scores from appropriate held-out folds.
3. Verify version-specific scikit-learn APIs:
   - `CalibratedClassifierCV` offers sigmoid and isotonic; `FrozenEstimator` for pretrained estimators was introduced in scikit-learn 1.6. It does **not** enforce train/calibration separation itself.
   - `method="temperature"` was added in scikit-learn **1.8**, and is not an option on 1.7.
   - The default CV strategy may stratify by class without protecting groups, time and delayed labels. Validate folds explicitly.
4. On untouched evaluation data, compare bin-level predicted probabilities to observed event rates, with counts and uncertainty; measure Brier/log loss alongside discrimination. Brier is a proper score that also reflects resolution/base-rate uncertainty, **not an isolated proof of calibration**.
5. Do not choose business thresholds on the final test labels. Thresholds require explicit cost/capacity objectives. Document subgroup, time and prevalence-shift behavior; global calibration does not imply conditional or individual calibration.

`binary_probability_report` implements a **descriptive** binary Brier/reliability table with strict finite/label bounds. Bins with fewer than `min_bin_size` observations return `null` reliability estimates; this suppresses false precision but does not replace confidence intervals. No library calibration algorithm is fitted by this helper.

## Validation and evidence

- **Executed locally:** `23/23` standard-library unit tests in `tests/test_data_science_uncertainty_integrity.py` on the code replicated exactly in `examples/data_science/uncertainty_integrity.py`. The tests cover partition overlaps, duplicate IDs, finite-sample quantile rank, insufficient calibration data, invalid alpha/scores, inclusive empirical coverage, sparse bins, bounded probabilities, invalid labels and numeric overflow.
- **Routing fixtures:** added **15** `ds-uncertainty-*` examples to `tests/fixtures/yaml-routing-cases.yaml`; the fixture file now contains **423 cases** and the master skill ID registry still contains **344 IDs**. Positive/bilingual intents and hard negatives protect conformal vs calibration vs Bayesian/parameter/forecast/fairness cases.
- **Static routing check:** a JavaScript reconstruction of the repository's deterministic lexical rules selected the expected skills on **15/15** candidate scenarios. This is **not** execution of the Python `Router` or CI, and not a measured semantic accuracy benchmark.
- **Not yet executed/verified:** full Python graph validator, full routing fixture runner, complete unit suite, actual GitHub Actions push-run result, pinned sklearn/MAPIE model-fitting integration test, independent statistical review, and real agent-host invocation.

### Acceptance commands

Run these in a fresh checkout of **current** `pre_release`, record `git rev-parse HEAD` and the actual exit statuses:

```sh
python -m capability_map validate
python scripts/evaluate_graph.py
python scripts/report_coverage.py --summary
python -m unittest discover -s tests -p 'test_data_science_uncertainty_integrity.py' -v
python -m unittest discover -s tests -p 'test_data_science_uncertainty_routing.py' -v
python -m unittest discover -s tests -v
```

### Outstanding production-depth gates

1. Pinned (at least one maintained release) MAPIE split regression implementation tested against synthetic exchangeable and shifted distributions; check exact runtime API and optional coverage behavior.
2. Pinned sklearn binary/multiclass `CalibratedClassifierCV` example: guard train/calibration/evaluation separation, class absence, `FrozenEstimator`, Brier/log loss, subgroup sample sizes, temporal shift and `temperature` version support.
3. Empirical rejection cases: severe temporal drift, cross-entity dependence, subgroup undercoverage and a contaminated calibration partition. Do not misrepresent a failed assumption as “validated coverage”.
4. Record confidence/coverage diagnostics with uncertainty on independent evaluation datasets, test bounded computational cost and false routing across agent hosts.
5. Audit the other 42 Data Science specialists and all other Data subdomains before marking all of Data complete.

## Official/reference sources

- [MAPIE conformal conformity-score quantiles](https://mapie.readthedocs.io/en/stable/content/conformal-prediction/conformity-scores/)
- [MAPIE algorithm choice, assumptions and API selection](https://mapie.readthedocs.io/en/stable/content/getting-started/choosing-algorithm/)
- [MAPIE split-conformal regression API](https://mapie.readthedocs.io/en/stable/api/regression/)
- [scikit-learn calibration overview](https://scikit-learn.org/stable/modules/calibration.html)
- [scikit-learn CalibratedClassifierCV release-aware API](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV)
- [scikit-learn 1.7 frozen-estimator and available methods](https://scikit-learn.org/1.7/modules/generated/sklearn.calibration.CalibratedClassifierCV.html)

**Next Data Science family:** forecasting (rolling-origin validation, distribution shift, probabilistic and hierarchical forecasting), then inference/survey methods. Do not switch to an unrelated top-level domain yet.
