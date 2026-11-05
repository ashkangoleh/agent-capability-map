# ds-r-statistics: specialist evaluation and negative controls

Domain `data/data-science/foundations`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Create or inspect a project-local R environment. Pin package versions with renv or an equivalent lockfile and record the R version and system dependencies.
2. Separate raw inputs, derived data, analysis code, outputs and rendered reports. Use explicit project-relative paths and avoid hidden working-directory assumptions.
3. Import data with explicit types and locale/time-zone handling. Validate factor levels, date parsing, missing-value codes and row grain before analysis.
4. Choose statistical functions from the design: independent/paired, clustered, weighted, repeated-measures, survival, time-series or Bayesian. Do not apply a default test based only on variable type.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not rely on an interactive workspace image or a saved global environment as the only reproducibility artifact.
- Do not use default contrasts, reference categories or missing-value codes without documenting them.
- Do not suppress warnings about singular fits, separation or convergence.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://cran.r-project.org/manuals.html
- https://rstudio.github.io/renv/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
