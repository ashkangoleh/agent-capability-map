# Data Science — Forecasting Validity and Operational Depth

**Updated:** 2026-11-05  
**Repository / working branch:** `ashkangoleh/agent-capability-map` / `pre_release`  
**Canonical scope:** `data/data-science`  
**Acceptance status:** Four existing forecasting skills hardened. Executable arithmetic/invariant tests pass locally. **Full repository Python CI, production engine integrations and independent statistical certification remain unverified.**

## Why four specialists are distinct

| User task | Existing specialist | Critical invariant |
|---|---|---|
| Forecast origins, multi-horizon backtests, late labels, exogenous publication | `time-series-forecast-backtesting` | All training targets and covariates are available at the actual decision origin; evaluate future holdouts only |
| Conditional quantiles, interval width, tail risk | `ds-probabilistic-forecasting` | Quantiles do not cross; loss/coverage evaluated per horizon on genuine held-out observations |
| Geographic/product/temporal hierarchy and reconciled totals | `ds-hierarchical-forecasting` | Versioned additive summing matrix; coherent point forecasts, and separately tested joint probabilistic coherence |
| Zero-heavy/intermittent SKU demand and inventory choices | `ds-intermittent-demand-forecasting` | True zeros must be distinguished from stockout-censored demand, outages and missing periods |

These skill IDs are **unchanged**. Do not merge the specialist methods into one generic forecasting answer or add empty duplicate skill wrappers.

## Runnable integrity checker

`examples/data_science/forecast_integrity.py` is a dependency-free, model-free precondition validator with five functions:

1. `rolling_origin_splits`: expanding/rolling training and future evaluation ranges, with a sample-index gap, horizon, origin step and a maximum fold count. Overlapping multi-step evaluation windows imply dependent errors. **Gap is not wall-clock embargo.**
2. `audit_forecast_availability`: for a *single* monotonic timestamp series, enforces timezone-aware decision origin and available training outcomes; optionally checks whether future exogenous covariates were already published at that origin.
3. `quantile_forecast_report`: finite quantile levels, no quantile crossing, separate pinball by quantile, outer-interval empirical coverage and width. The interval mass `q_high-q_low` is nominal, not a validated conditional-coverage guarantee.
4. `hierarchy_coherence_report`: simple one-level additive point-forecast consistency with explicit parent-to-bottom membership. **Does not perform reconciliation** or validate a general multi-level summing matrix, non-additive metrics or probabilistic sample paths.
5. `intermittent_demand_profile`: observed nonnegative demand profile with `ADI`, zero fraction and positive demand size. Refuses `missing` and `stockout` statuses, which require a separately evidenced unconstrained-demand reconstruction.

### Example

```python
from examples.data_science.forecast_integrity import (
    rolling_origin_splits, quantile_forecast_report,
    hierarchy_coherence_report, intermittent_demand_profile,
)

folds = rolling_origin_splits(12, min_train_size=5, horizon=2, step=2, gap=1)
assert [f["evaluation"] for f in folds] == [(6, 8), (8, 10), (10, 12)]

q = quantile_forecast_report([0, 10], {0.1: [-2, 8], 0.9: [2, 12]})
assert q["empirical_interval_coverage"] == 1.0

coherence = hierarchy_coherence_report(
    {"north": [1, 2], "south": [3, 4]}, {"total": [4, 6]},
    {"total": ["north", "south"]},
)
assert coherence["coherent"]

profile = intermittent_demand_profile(
    [0, 0, 4, 0, 2, 0], statuses=["observed"] * 6,
)
assert profile["average_demand_interval"] == 3.0
```

The numbers above are **illustrative arithmetic**, not trained-model benchmark scores. Additional controls must verify as-of joins, timezone/DST irregularities, entity-specific windows, stockout provenance and release versions.

## Production failure and recovery realism

- **Invalid model comparison:** if features or target labels were published after an origin, quarantine that fold and recompute with as-of records. Never show training residuals as out-of-sample forecasting metrics.
- **Temporal overlap:** rolling origin `step_size < h` is permissible but errors are dependent; report aggregate uncertainty using a defensible method rather than assuming independent folds.
- **Quantile crossing or uncalibrated tails:** do not sort/massage outputs silently to make metrics pass. Retrain or use an explicitly justified quantile-reconciliation method and independently re-evaluate each horizon.
- **Hierarchy drift:** changes in product/category, store or region membership change the summing matrix. Record effective dates, repair duplicate/missing mappings, and backtest all hierarchy levels with the same version. Point coherence does not prove coherent predictive distributions.
- **Stockouts and item retirement:** a zero sale during out-of-stock periods is censored demand; do not train/evaluate Croston/SBA/TSB as though that were true zero demand. All-zero observations do not establish permanent obsolescence.
- **Model operation:** monitor available target latency, covariate freshness, horizon-level bias, missing forecast batches, drift, cost and business service levels. Roll back to a measured appropriate baseline, not a fabricated performance claim.

## Runtime/version and sources

- **StatsForecast** cross-validation supports `h`, `step_size`, `n_windows`; the output includes `cutoff` when invoked as documented. Exact APIs depend on the installed version, and the project recommends version pinning.
- **scikit-learn TimeSeriesSplit** uses `gap` measured in **samples** and assumes equally spaced observations for comparable fold durations. Irregular calendars, late outcomes, or overlapping label windows need additional design-specific validation.
- **HierarchicalForecast** uses summing-matrix reconciliation methods including BottomUp and MinTrace. Predictive quantiles do not generally add to their parent's quantile; joint scenarios require separate probabilistic reconciliation.
- **Intermittent** Croston-style point estimates are not equivalent to calibrated lead-time demand distributions. TSB separately updates occurrence probability and positive-demand size under its method assumptions.
- **Pinball loss** is a proper quantile scoring rule; evaluate horizon-wise rather than using point-only MAE for probabilistic outputs.

Primary sources:

- https://otexts.com/fpp3/tscv.html
- https://nixtla.github.io/statsforecast/docs/tutorials/crossvalidation.html
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html
- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html
- https://github.com/Nixtla/hierarchicalforecast
- https://help.sap.com/docs/SAP_HANA_PLATFORM/319d36de4fd64ac3afbf91b1fb3ce8de/croston-tsb-method-8203847.html

## Evidence collected for this increment

- **30/30** actual local Python unit tests passed in `tests/test_data_science_forecast_integrity.py`. The helper and test files' **Git blob SHAs exactly matched** the tested local files after synchronization.
- `tests/test_data_science_forecast_routing.py` was added. **22** new positive, bilingual and near-miss `ds-forecast-*` fixtures bring total declared deterministic routing cases to **445**. Master skill-ID index remains **344 unique IDs**.
- A **separate JS reconstruction** of the deterministic lexical router evaluated all **22/22** new cases against the actual GitHub YAML and found the expected routes; it also found no duplicate triggers in the changed ancestor/registry maps. This is not a Python Router test or measured agent-level accuracy.
- **Unknown / not verified:** full `Router.validate`, all Python test cases, push GitHub Actions CI outcome, real engine/version integrations, independent forecaster review, multi-agent host invocation and production failure drills. Do not claim `445/445 PASS` from the source fixture count.

### Required next validations

```sh
git rev-parse HEAD
python -m capability_map validate
python scripts/evaluate_graph.py
python scripts/report_coverage.py --summary
python -m unittest discover -s tests -p 'test_data_science_forecast_integrity.py' -v
python -m unittest discover -s tests -p 'test_data_science_forecast_routing.py' -v
python -m unittest discover -s tests -v
```

Then run a version-pinned StatsForecast rolling-window backtest on a small, well-defined dataset, a horizon-specific quantile scoring experiment, and a HierarchicalForecast reconciliation experiment with a versioned hierarchy. Independently test stockout observations and lead-time inventory decisions. Record measured metrics and runtime.

## Subsequent inference and survey workstream

The later statistical inference/survey increment deepens existing multiple-testing, complex survey and missing-data skills. Its more recent evidence and known limits are in `docs/DATA_SCIENCE_INFERENCE_SURVEY_VALIDATION_PROTOCOL.md`. Continue with the **remaining Data Science specialist and host-behavioral audit**, not another top-level domain.

## Next Data Science focus

Review statistical inference/survey methods (design effects, cluster/sampling weights, multiple testing, missingness, robust/bayesian uncertainty), then the remaining specialist boundaries. **Data Science and the top-level Data domain remain incomplete** until all required evidence and nine Data subdomain audits are finished.
