# Data Science Remaining Skills & Layout Audit

**Scope:** `data/data-science` only  
**Branch:** `pre_release`  
**Assessment date:** 2026-11-05  
**Status:** Structural inventory verified from registered YAML; detailed remaining-skill behavior and native host execution **not yet certified**.

## What was actually reviewed

The Data Science map currently has **20 registered capability categories** and **42 registered specialist skill IDs**. These are structural counts from the registry files, not independent statistical correctness or production claims.

The first source-tree reorganization has migrated **10 of 42** packages across `statistics-advanced` and `foundations` categories to nested domain paths, with byte-identical content and updated registry links. **32** Data Science packages still have their existing flat source locations. See `docs/SKILL_LIBRARY_LAYOUT.md` for detailed compatibility restrictions.

## Registered category inventory and next audit order

| Category | Registered specialist count | Source migration | Next validation evidence |
|---|---:|---|---|
| `statistics-advanced` | 6 | Migrated | Actual Python graph/router CI; survey variance and MICE/PyMC reproducible validations |
| `model-validation` | 4 | Flat | Group/temporal holdout, conformal assumptions, fairness evaluation validity |
| `statistics` | 1 | Flat | Independent inference method, CI interpretation and multiple-testing boundary |
| `causal-inference` | 3 | Flat | Identification/refutation and clustered/panel estimator assumptions |
| `forecasting` | 1 | Flat | Rolling-origin backtest in an actual supported runtime |
| `feature-engineering` | 1 | Flat | As-of joins, feature/label availability and leakage under late data |
| `exploration` | 1 | Flat | Dataset profiling/column types, missingness and outlier handling |
| `geospatial` | 1 | Flat | CRS units, geometry validity and reprojection effects |
| `anomaly-detection` | 1 | Flat | Baseline drift, threshold choice and alert false-positive behavior |
| `foundations` | 4 | Migrated | Reproducibility, numerics, Python/R environment/version controls |
| `experimentation` | 3 | Flat | Assignment integrity, sequential stopping and causal design boundaries |
| `modeling` | 5 | Flat | Boosting/calibration/explainability and optimization leakage |
| `survival` | 1 | Flat | Censoring, competing events, time-dependent covariates and risk sets |
| `forecasting-advanced` | 3 | Flat | Hierarchical/probabilistic coherence, zero-vs-stockout demand |
| `recommendation` | 1 | Flat | Logged-policy bias, ranking offline vs online metrics, exposure/position |
| `graph-science` | 1 | Flat | Network dependence, leakage from transductive edges and scaling |
| `geospatial-advanced` | 1 | Flat | Spatial correlation, spatial CV and uncertainty calibration |
| `simulation` | 1 | Flat | RNG determinism, Monte Carlo error and sensitivity convergence |
| `optimization` | 1 | Flat | Constraint infeasibility, solver status, numerical stability and cost |
| `text-analytics` | 2 | Flat | Multilingual/code-switched evaluation, label quality, language imbalance |

The table describes **required acceptance evidence**, not verified gaps in every skill. Detailed source review of the 32 unmigrated packages and runtime benchmark results are still pending.

## Recommended controlled completion order

1. Validate **current** `pre_release` full graph, all deterministic routing fixtures, unit suites and GitHub push CI before claiming the first two category migrations are safe.
2. Test host behavior for the six nested skills with actual Codex, Claude Code, OpenCode, Cursor and Copilot usage paths. Explicit router resolution is the project's intended mechanism; implicit native discovery cannot be assumed.
3. Only after those checks, migrate further Data Science capability categories **one category at a time**, updating registries, tests and eliminating flat duplicates. Avoid sweeping changes that mix source moves with new behavior.
4. Independently audit statistical methods in the remaining categories against release-pinned references and deliberately invalid cases. Report structural, method-level and deployment-level evidence separately.
5. Once Data Science evidence is sufficient, explicitly ask which of the other eight Data subdomains to continue; do not declare the entire Data domain complete.

## Verification commands (not yet claimed executed)

- `python -m capability_map validate`
- `python scripts/evaluate_graph.py`
- `python scripts/report_coverage.py --summary`
- `python -m unittest discover -s tests -v`

**No new example files or specialist skill IDs were added in this layout increment.**
