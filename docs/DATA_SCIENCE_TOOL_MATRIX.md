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
| Text analytics | spaCy, NLTK, scikit-learn, Gensim | tokenization, sparse models, topic models, drift |

Data Science owns problem framing, statistical validity, experimentation, quantitative analysis and classical predictive modeling. AI/ML owns deep learning, foundation models, LLM/RAG systems, distributed training, model serving and MLOps. Feature stores and deployment may require explicit cross-domain composition.

Production safeguards: define unit/estimand; prevent target and temporal leakage; split by entity/time; account for missing-not-at-random data; control multiplicity; assess power and effect size; evaluate calibration and decision costs; quantify uncertainty; test subgroup stability; preserve reproducibility and privacy.

This matrix covers major ecosystems, not every package or commercial product. Verify APIs, licenses and compatibility before implementation.
