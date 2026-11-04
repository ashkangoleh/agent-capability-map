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
| Positive fixtures for new specialists | 11 |
| Near-miss fixtures for cross-domain boundaries | 5 |

The 42 count is the active registry inventory, not a benchmark score.

## Capability coverage matrix

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
