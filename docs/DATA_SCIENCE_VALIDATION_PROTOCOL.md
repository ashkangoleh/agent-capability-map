# Data Science — Leakage-safe Model Evaluation Protocol

**Audit date:** 2026-11-04  
**Branch:** `pre_release`  
**Workstream:** `data/data-science/model-validation`  
**Certification status:** Source-reviewed skill update and executable split-boundary unit tests only. No independently certified end-to-end sklearn or host-model results.

## Problem and routing boundary

The previous sklearn skill registered the one-word trigger `scikit-learn` directly on its specialist. An underspecified request such as "scikit-learn" could therefore silently select leakage-safe validation, although the user might want API exploration, inference, calibration or different modeling tasks.

This increment changes the routing contract:

- Generic `sklearn` / `scikit-learn` still identifies the broader Data Science domain but returns `needs_clarification` at the model-capability step.
- A task identifying *validation* and a specific context (cross-validation, group separation, temporal leakage or split design) resolves to `sklearn-leakage-free-validation`.
- Point-in-time feature integration stays with `feature-engineering-point-in-time`; conformal coverage stays with `ds-conformal-prediction-uncertainty`.
- A term match is a lexical heuristic, not an estimated posterior probability of correct routing; semantic near-misses require actual agent evaluation.

## Split contract decision table

| Evaluation situation | Candidate design | Required checks |
|---|---|---|
| Independent examples, no time dependence | Random or stratified train/validation/test; ordinary CV | No overlap, fold-local preprocessing, independent test set, prevalence/metric |
| Multiple observations per independent entity | `GroupKFold` or group holdout; `StratifiedGroupKFold` where justified | Entity/group disjointness; enough independent groups; group-level uncertainty |
| Ordered samples and future evaluation | Forward holdout / `TimeSeriesSplit` where sampling assumptions hold | Event order, label availability, lookback, horizon, delayed outcomes, window purge |
| Irregular timestamps or overlapping label windows | Custom chronological/purged splitter | Calendar-aware embargo in time units, non-overlapping outcome information, as-of feature availability |
| Both unseen-entity generalization and future-period prediction | Domain-specific group-and-time splitter | Enforce group disjointness and chronology; for forecasts of *seen* entities, reusing historical entities is allowed and should not be confused with entity leakage |
| Repeated model/hyperparameter choices | Nested cross-validation or properly isolated tuning + final holdout | Outer/inner separation, common outer splits, no final-test reuse |

**Version caveat:** `GroupKFold` accepts `shuffle` and `random_state` only in sklearn 1.6 or later. `TimeSeriesSplit(gap)` excludes a number of samples, not a fixed wall-clock interval; equally spaced observations are needed to compare equal-duration folds.

## Example and executable validation

`examples/data_science/split_integrity.py` provides a **dependency-free boundary audit** that accepts common sklearn integer index arrays, checks duplicate/out-of-bounds and train/test overlap, optional group overlap, optional timezone-aware chronological order, and optional label availability before the first held-out decision.

The helper deliberately does **not** train models, detect feature value leakage, establish exchangeability, prove causal identification, or cover every shared-group and overlapping-label variant. It is a precondition/guard, not a production certification.

Run:

```sh
python -m unittest discover -s tests -p 'test_data_science_split_integrity.py' -v
python -m unittest discover -s tests -p 'test_data_science_validation_routing.py' -v
python -m capability_map validate
python scripts/evaluate_graph.py
python scripts/report_coverage.py --summary
python -m unittest discover -s tests -v
```

**Evidence on update:** Local source-equivalent split helper and unit tests were run independently before committing: **17/17 passed**, including an optional NumPy integer-array check. The repo-wide Python router suite and GitHub push CI remain **NOT VERIFIED**. Source-level router reconstruction was used for candidate selection checks; this does not substitute for the actual Python router run.

New `ds-validation-*` fixtures cover generic-tool abstention; positive group/temporal/bilingual requests; and protected feature engineering and conformal routing boundaries. They are not an estimate of false-positive rates in natural production conversations.

## Acceptance evidence needed for mature Data Science coverage

1. Full graph validation, all routing cases and unit tests against a named commit SHA.
2. An environment-pinned sklearn demonstration on a synthetic repeated-entity and time-dependent dataset; compare intentionally leaky and corrected pipelines without claiming the outcome generalizes to real datasets.
3. Group disjointness plus time/label-availability assertions on each fold; verify timezone and data-provenance contracts, not just `TimeSeriesSplit` parameter selection.
4. Quantify realistic deployment validation quality by task: false positives/negatives, calibration/coverage or task-specific metric, temporal and subgroup drift and uncertainty.
5. Independent human/statistical review of the full set of 42 specialist packages and 26 declared capability areas.
6. Confirm host-specific skill invocation, refusal/clarification and correct selective loading on Codex, Claude Code, OpenCode, Copilot and Cursor.
7. Report missing evidence, explicit abstentions and supported version matrix; keep the entire Data top-level domain marked incomplete until all nine subdomains are reviewed.

## Subsequent Data Science slices (not yet completed)

- **Causal inference and experimentation:** its existing skill trio now has identification, assignment-ratio and sequential-monitoring validity gates plus an executable two-arm assignment diagnostic; see `docs/DATA_SCIENCE_CAUSAL_EXPERIMENTATION_PROTOCOL.md`. Live causal-estimator benchmarks, stratified/clustered SRM and sequential error simulations remain unverified.
- **Conformal and calibration:** exchangeability, finite-sample quantiles, subgroup coverage, calibration/test partition separation and distribution shift.
- **Forecasting:** rolling-origin backtests, horizon/label availability, intermittent demand, hierarchical reconciliation, quantile calibration and uncertainty.
- **Statistical inference and surveys:** multiplicity, survey design effects, non-response, cluster/stratification design, power and sensitivity.
- **Evaluation benchmark:** label hard negative and bilingual prompts and measure real model behavior; do not use deterministic fixture accuracy as a model score.

## Primary references

- [scikit-learn common pitfalls and data leakage](https://scikit-learn.org/stable/common_pitfalls.html)
- [Cross-validation strategy and group/time split guidance](https://scikit-learn.org/stable/modules/cross_validation.html)
- [GroupKFold release-specific API](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html)
- [TimeSeriesSplit gap and spacing assumptions](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
- [StratifiedGroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html)

**Next:** independently execute full Python router/CI validation; continue with conformal prediction/calibration and forecasting **within Data Science**. Do not mark Data Science or all of Data complete.
