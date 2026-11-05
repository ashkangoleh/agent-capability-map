# ds-probabilistic-forecasting: specialist evaluation and negative controls

Domain `data/data-science/forecasting`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Specify a predictive target, valid support and **each horizon**. Quantiles describe predictive distribution tails; quantile interval mass `q_high-q_low` is a target mass, not an empirical or conditional coverage guarantee.
2. Use rolling-origin windows and an honest out-of-sample holdout with the information actually available at origin; never calibrate intervals on all-series in-sample residuals and reuse those same outcomes as independent tests.
3. Choose a release-supported quantile/parametric/ensemble/simulation/conformal forecasting method. Record forecast origin, model version, quantile levels and covariate scenarios, especially uncertainty in future covariates.
4. Validate **quantile monotonicity on every observation and horizon** (`q_0.1 <= q_0.5 <= q_0.9`). Do not silently sort crossing predictions into apparently valid outputs; correct the model/reconciliation method and revalidate.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Crossing quantiles, missing horizons or invalid probability levels → fail rather than silently rearrange scores.
- Short calibration sample, drift, autocorrelation or changed covariate distribution → report nominal guarantee as unsupported.
- Sparse counts or inventory stockouts → use zero-demand and availability controls, not a continuous Gaussian forecast by default.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html
- https://otexts.com/fpp3/
- https://nixtla.github.io/statsforecast/docs/tutorials/crossvalidation.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
