# ds-conformal-prediction-uncertainty: specialist evaluation and negative controls

Domain `data/data-science/model-validation`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define the estimand as **marginal predictive coverage** or a specific stronger risk/conditional statement. Specify the future population; test whether calibration and deployment observations can plausibly be exchangeable. Flag dependence, cluster sampling, nonstationarity, delayed outcomes and changing data sources instead of silently declaring IID.
2. Freeze model fitting and hyperparameter selection **before** using conformal calibration labels. Keep training, conformalization and final evaluation records disjoint, including indirect duplicates and any group/time constraints required by the deployment task. The example auditor checks only observation IDs, not exchangeability or source integrity.
3. Choose the correct procedure for the target: split absolute-residual conformal for simple regression, LAC/APS or another justified method for classification labels, or a version-verified time/group-aware approach when ordinary exchangeability fails. Never apply a regression residual quantile to class probabilities and call it calibrated classification.
4. For split regression with `n` nonnegative calibration absolute residuals `s_i`, calculate `k = ceil((n+1)*(1-alpha))` and select the **k-th smallest** score; do **not** interpolate the empirical quantile. If `k>n`, a finite guara

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Calibration data used to fit/tune the model or choose the score → contaminated guarantees; rebuild disjoint partitions and rerun.
- `k>n` or low subgroup sample sizes → insufficient support for a finite radius or subgroup claim; record the limitation rather than invent a coverage value.
- Clustered/repeated entities, autocorrelation or distribution shift → standard exchangeability guarantee may fail; require a separately justified design and coverage evidence.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://mapie.readthedocs.io/en/stable/content/conformal-prediction/conformity-scores/
- https://mapie.readthedocs.io/en/stable/content/getting-started/choosing-algorithm/
- https://mapie.readthedocs.io/en/stable/api/regression/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
