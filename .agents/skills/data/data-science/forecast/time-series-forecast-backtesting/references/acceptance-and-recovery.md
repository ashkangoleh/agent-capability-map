# time-series-forecast-backtesting: specialist evaluation and negative controls

Domain `data/data-science/forecast`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define the `origin_at` decision timestamp and information set for **each** backtest. An observed value is not automatically available when measured; use label-materialization and feature-publication timestamps. For weather/promotions, distinguish planned values known at origin from realized values collected later.
2. Choose expanding versus fixed-width rolling windows, `initial_window`, `h`, `step_size`, `n_windows` and `refit` schedule. Hold out an untouched future period after model selection. The `step_size` between origins can be less than the horizon; then evaluation windows overlap and their errors are not independent.
3. Validate monotonically increasing, deduplicated timestamps **per series**, expected regularity, timezones/DST, missing periods and late/corrected labels before applying a splitter. Unevenly spaced observations are **not** made equal-duration by an index-based `gap`.
4. Fit scalers, imputers, transformations, lag features, model selection and intervals **inside the available training window at each origin**. An exogenous variable for a future timestamp is allowed only if its forecast/planned value was truly published before `origin_at`; actual future observations are leakage.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Last training label or a future exogenous value not yet published at `origin_at` → reject that fold; reconstruct as-of inputs.
- Duplicate or irregular timestamps → validate per-series calendar; use an explicit calendar-aware splitter rather than assuming a fixed index gap.
- Zero-heavy demand, missing vs stockout-censored observations → route to intermittent-demand quality gates.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://otexts.com/fpp3/tscv.html
- https://nixtla.github.io/statsforecast/docs/tutorials/crossvalidation.html
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
