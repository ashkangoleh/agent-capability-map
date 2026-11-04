# Data Science Specialist Coverage Audit

## Scope and completion definition

Data Science is a first-class subdomain under `data`, with canonical route `data/data-science`. It owns statistical reasoning, experimentation, causal analysis, scientific computing, classical predictive modeling and quantitative decision science. Data Engineering owns data systems and pipelines; AI/ML owns deep learning, foundation models, LLM/RAG, distributed training, model serving and MLOps.

"Complete" is evaluated against this explicit capability inventory, not against every package or product that may exist. A capability is considered structurally covered only when it has an active specialist Skill, an active registry entry, a reachable map route, official reference starting points and positive/negative routing evidence. Structural presence does not prove expert correctness or production certification.

## Current inventory

| Measure | Current state |
|---|---:|
| Canonical domain route | `data/data-science` |
| Active subdomain maps | 20 |
| Active specialist skills | 42 |
| New specialist skills in this expansion | 11 |
| Existing specialist skills materially rewritten | 15 |
| Defined capability areas with active routes | 26 / 26 |
| Positive fixtures for new specialists | 11 |
| Near-miss fixtures for cross-domain boundaries | 5 |

The 42 count is the active registry inventory, not a benchmark score.

## Capability coverage matrix

All 26 areas below have at least one active specialist route and registry. This is 100% structural coverage of the declared matrix; it is not a claim that every statistical method, package, or production use case has been independently certified.

| Capability area | Current specialist coverage | Status |
|---|---|---|
| Problem framing and estimands | `ds-problem-framing`, `statistical-inference-design` | Active |
| Scientific Python, R and reproducibility | `ds-scientific-python`, `ds-r-statistics`, `ds-jupyter-reproducibility` | Active |
| EDA and data profiling | `pandas-eda-data-profiling` | Active |
| Frequentist and robust inference | `statistical-inference-design`, `ds-robust-nonparametric-inference` | Active |
| Multiple testing and survey design | `ds-multiple-testing-control`, `ds-survey-sampling-design` | Active |
| Bayesian modeling and diagnostics | `ds-bayesian-pymc-stan` | Active |
| Missing-data mechanisms and sensitivity | `ds-missing-data` | Active |
| Power and sample-size design | `ds-power-sample-size` | Active |
| Fixed-horizon and sequential experiments | `ds-ab-experimentation`, `ds-sequential-experimentation` | Active |
| Causal design and observational identification | `ds-causal-inference`, `causal-inference-observational` | Active |
| Double/debiased ML and panel econometrics | `ds-doubleml-causal-estimation`, `ds-panel-econometrics` | Active |
| Classical supervised ML and validation | `ds-gradient-boosting`, `sklearn-leakage-free-validation` | Active |
| Imbalanced learning and calibration | `imbalanced-classification-evaluation`, `ds-model-calibration` | Active |
| Explainability and subgroup/fairness measurement | `ds-shap-explainability`, `ds-fairness-subgroup-evaluation` | Active |
| Conformal uncertainty and risk control | `ds-conformal-prediction-uncertainty` | Active |
| Clustering and model selection | `ds-clustering-evaluation`, `ds-optuna-search` | Active |
| Time-series and hierarchical forecasting | `time-series-forecast-backtesting`, `ds-hierarchical-forecasting`, `ds-probabilistic-forecasting` | Active |
| Intermittent demand | `ds-intermittent-demand-forecasting` | Active |
| Survival and time-to-event analysis | `ds-survival-analysis` | Active |
| Recommendation and ranking science | `ds-recommender-evaluation` | Active |
| Graph and network science | `ds-graph-science` | Active |
| Geospatial analysis and spatial statistics | `geospatial-analysis-crs-quality`, `ds-geospatial-statistics` | Active |
| Anomaly detection | `anomaly-detection-baselines` | Active |
| Simulation and uncertainty | `ds-monte-carlo` | Active |
| Operations research and optimization | `ds-operations-research` | Active |
| Classical and multilingual NLP | `ds-classical-nlp`, `ds-multilingual-nlp-evaluation` | Active |

## New specialist boundaries

- Robust/nonparametric inference is distinct from Bayesian posterior inference and from routine metric reporting.
- Multiple-testing control handles families of hypotheses; it does not repair optional stopping or undisclosed outcome selection.
- Survey inference preserves the sample design and design-based variance; ordinary weighted regression is not automatically survey analysis.
- Conformal prediction produces prediction sets/intervals under explicit exchangeability assumptions; it is not a confidence interval for a parameter.
- Fairness subgroup evaluation measures statistical disparities and uncertainty; policy/legal compliance remains a separate review.
- DoubleML uses orthogonal scores and cross-fitting for nuisance estimation; it does not create causal identification.
- Panel econometrics treats entity/time dependence, fixed effects, clustered errors and staggered treatment timing explicitly.
- Sequential experimentation requires a valid stopping/monitoring procedure; repeated fixed-horizon p-values are not acceptable.
- Probabilistic forecasting evaluates distributions and calibration; intermittent-demand forecasting handles sparse occurrence/size processes separately.
- Multilingual NLP evaluation reports per-language and script-level performance; translation is not a substitute for native-language evaluation.

## Model-validation hardening — 2026-11-04 (post-audit increment)

This increment improves the **existing** `sklearn-leakage-free-validation` package rather than inflating the skill inventory. The previously reported 42 active Data Science skills and 26 declared capability areas are unchanged; the latest authoritative master index remains 344 total skill IDs across domains.

- Removed the overly broad, one-word `sklearn` and `scikit-learn` triggers at the specialist/model-validation routing layer while preserving top-level domain discovery. Bare tool names now ask for clarification instead of silently selecting model validation.
- Added explicit sklearn validation, grouped and temporal split, label-leakage and Persian task triggers. Group/temporal requirements distinguish future predictions for **seen entities** from generalization to **unseen entities**.
- Expanded the existing skill to address fit-before-split, target encoding, fold-local resampling, independent hyperparameter selection, group leakage, prediction-time feature and outcome availability, irregular timestamps and post-hoc holdout reuse.
- Added `examples/data_science/split_integrity.py` (a standard-library split-boundary guard), and `tests/test_data_science_split_integrity.py` with **17** unit tests. The source-equivalent helper was executed locally with **17/17 passed**, including NumPy integer arrays when NumPy is installed.
- Added `tests/test_data_science_validation_routing.py` with structural and ambiguity regression tests; appended **11** `ds-validation-*` fixtures, bringing the full routing fixture file to **396 cases**.
- A separate JavaScript reconstruction of the current lexical resolver matched **11/11** new cases against the authoritative GitHub YAML. This is **not** a Python `Router.resolve` run and does not certify the full routing suite or model accuracy.
- Comprehensive evidence matrix and acceptance/next steps: `docs/DATA_SCIENCE_VALIDATION_PROTOCOL.md`.

**Unverified:** The new commits have not been accompanied by independently retrieved full GitHub Actions push-job results; the complete repo `Router.validate()`, routing evaluation and unit suite must still run against the current HEAD. No sklearn-dependent model benchmarking or human statistics review was performed in this increment. Do not claim production certification or Data Science completion.

## Causal identification and experimentation hardening — 2026-11-04 (post-audit)

The three existing skills `ds-causal-inference`, `ds-ab-experimentation` and `ds-sequential-experimentation` received stricter validity boundaries. No specialist IDs were added or renamed.

- **Causal:** separate identification from estimation, record unverifiable assumptions, audit selection/interference and pre-trends, reject causal claims without design-specific identification.
- **A/B:** use pre-outcome, unique assignment-unit logs; distinguish SRM from exposure/metric selection, handle conflicts and duplicates, respect randomization design. The two-arm `examples/data_science/assignment_integrity.py` provides a bounded approximate Pearson chi-square diagnostic.
- **Sequential:** predeclare looks, information fractions, boundaries, alpha spending and delayed-outcome rules; prohibit retroactive ordinary fixed-horizon peeking claims.
- New tests: `tests/test_data_science_assignment_integrity.py` (**18/18 locally run against source-equivalent helper**), `tests/test_data_science_causal_experimentation.py` and **12** `ds-causal-exp-*` fixtures. Current fixture file has **408 cases** and the master index still has **344 unique IDs** (file inventory counts, not validated full-suite totals).
- Static JavaScript reconstruction matched 12 candidate routes but did not run the Python router. Actual push CI, full Python suite and production/host behavior are **not yet verified**.

See `docs/DATA_SCIENCE_CAUSAL_EXPERIMENTATION_PROTOCOL.md` for error assumptions and the required execution/reproduction gates.

## Conformal prediction and probability calibration — 2026-11-05 (post-audit)

The existing `ds-conformal-prediction-uncertainty` and `ds-model-calibration` specialists were hardened without adding skill IDs. The first now specifies finite-sample split-conformal quantile rank and exchangeability/coverage boundaries; the second separates probability reliability, discrimination and threshold utility, including scikit-learn 1.6 `FrozenEstimator` and 1.8 temperature scaling compatibility.

- New dependency-free arithmetic example: `examples/data_science/uncertainty_integrity.py`.
- **23/23 locally executed** standard-library tests on the exact code replicated in `tests/test_data_science_uncertainty_integrity.py` (partition collisions, quantile rank, sparse calibration, probability bounds, numeric overflow).
- **15 new** positive, bilingual and near-miss `ds-uncertainty-*` routing fixtures, guarded by `tests/test_data_science_uncertainty_routing.py`. Fixture file total is **423**; index remains **344 unique** master skill IDs.
- An independent JS reconstruction of lexical routing matched 15/15 newly proposed requests. **Python router/CI/full-suite results and real-agent performance remain NOT VERIFIED.**
- Detailed claims, mathematical/operational limitations, and acceptance procedure: `docs/DATA_SCIENCE_UNCERTAINTY_CALIBRATION_PROTOCOL.md`.

No guarantee of conditional coverage, exchangeability, cross-group fairness, calibration under shift, or production readiness is established by these structural/source tests.

## Remaining limitations

1. Routing fixtures measure deterministic lexical matching, not semantic accuracy of an LLM choosing when to call the resolver.
2. Skill text has not been independently reviewed by a statistician/econometrician for every specialized estimator.
3. No executable benchmark suite currently validates all 42 skills on real datasets.
4. Current references are entry points, not a complete version compatibility matrix for every library.
5. Legal fairness determinations, clinical/regulated statistical validation and production model deployment require separate domain-specific governance and human review.
6. Coverage is not exhaustive for every specialist area: spatial causal inference, advanced survey small-area estimation, functional data analysis, psychometrics, survival causal inference, online learning and advanced econometric identification remain candidate future expansions.

## Promotion gates

A future Data Science specialist is promoted only when:
- it owns one distinct task boundary and does not duplicate an existing skill;
- its procedure is specific to the method and includes assumptions, failure cases and an output contract;
- official or primary references are verified;
- the route has positive, negative and near-miss fixtures;
- the full graph validator, routing evaluator and unit tests pass;
- human review confirms that the skill adds useful specialist depth.

## Validation evidence

Run:

~~~sh
python -m capability_map validate
python scripts/report_coverage.py --summary
python scripts/evaluate_graph.py
python -m unittest discover -s tests -v
~~~

The deterministic evaluator validates route selection only. It does not certify the statistical correctness of analyses produced by an agent.
