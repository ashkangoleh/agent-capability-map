# Data Science Tool and Concept Matrix

| Capability | Main tools | Concepts |
|---|---|---|
| Scientific computing | Python, NumPy, SciPy, R, Julia, Jupyter | numerical stability, vectorization, reproducibility |
| Exploration | pandas, Polars, DuckDB, ydata-profiling | EDA, sampling, missingness, outliers |
| Statistics | SciPy, statsmodels, R, SAS, Stata | estimands, distributions, confidence intervals, power, multiplicity |
| Bayesian | PyMC, Stan, NumPyro, ArviZ | priors, posterior inference, MCMC, convergence |
| Experimentation | Statsmodels, R, Optimizely, Statsig, GrowthBook | A/B, randomization, SRM, MDE, guardrails, CUPED |
| Causal inference | DoWhy, EconML, CausalML, DoubleML, DAGitty | DAGs, potential outcomes, matching, DiD, IV, RDD, synthetic controls |
| Classical ML | scikit-learn, XGBoost, LightGBM, CatBoost, H2O | classification, regression, ranking, calibration, imbalance |
| Model selection | Optuna, Hyperopt, Ray Tune | nested CV, Bayesian optimization, pruning |
| Explainability | SHAP, LIME, InterpretML | global/local explanation, feature dependence |
| Forecasting | statsforecast, sktime, Darts, Prophet, Nixtla | temporal validation, hierarchical reconciliation |
| Survival | lifelines, scikit-survival, R survival | censoring, hazard, competing risks |
| Recommendation | RecBole, implicit, LightFM, LensKit | candidate generation, NDCG, MAP, recall, exposure bias |
| Graph science | NetworkX, igraph, graph-tool | centrality, communities, graph sampling |
| Geospatial | GeoPandas, Shapely, Rasterio, PySAL, PostGIS | CRS, spatial joins, autocorrelation, spatial CV |
| Optimization/simulation | OR-Tools, PuLP, Pyomo, SciPy, SimPy | LP/MIP, constraints, Monte Carlo, sensitivity |
| Robust inference | SciPy, statsmodels, R | permutation tests, bootstrap intervals, rank tests, robust estimators |
| Multiplicity | SciPy, statsmodels | family-wise error, FDR, hierarchical testing, repeated looks |
| Survey inference | R survey, statsmodels | strata, PSU, inclusion weights, nonresponse, Taylor/replicate variance |
| Causal ML and econometrics | DoubleML, EconML, linearmodels, statsmodels | orthogonal scores, cross-fitting, panel FE, staggered DiD, IV, RDD |
| Sequential experimentation | Statsig, Optimizely, statsmodels | alpha spending, always-valid inference, SRM, sequential stopping |
| Probabilistic forecasting | StatsForecast, statsmodels, MAPIE | quantiles, CRPS, pinball loss, coverage, calibration |
| Intermittent demand | StatsForecast | Croston, SBA, TSB, ADIDA, IMAPA, lead-time demand |
| Uncertainty and fairness | MAPIE, Fairlearn, scikit-learn | conformal prediction, risk control, subgroup metrics, coverage |
| Multilingual text analytics | spaCy, scikit-learn, NLTK | language-stratified evaluation, scripts, dialects, code-switching |
| Text analytics | spaCy, NLTK, scikit-learn, Gensim | tokenization, sparse models, topic models, drift |

Data Science owns problem framing, statistical validity, experimentation, quantitative analysis and classical predictive modeling. AI/ML owns deep learning, foundation models, LLM/RAG systems, distributed training, model serving and MLOps. Feature stores and deployment may require explicit cross-domain composition.

Production safeguards: define unit/estimand; prevent target and temporal leakage; split by entity/time; account for missing-not-at-random data; control multiplicity; assess power and effect size; evaluate calibration and decision costs; quantify uncertainty; test subgroup stability; preserve reproducibility and privacy. The Data Science subtree currently contains 42 active specialist skills across 20 active subdomain maps. This is structural coverage; the audit in DATA_SCIENCE_COVERAGE_AUDIT.md distinguishes skill presence from validated task depth.

This matrix covers major ecosystems, not every package or commercial product. Verify APIs, licenses and compatibility before implementation.
