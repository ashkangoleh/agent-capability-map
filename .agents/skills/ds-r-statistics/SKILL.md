---
name: ds-r-statistics
description: Use when implementing reproducible statistical analysis or modeling workflows in R and its scientific package ecosystem.
metadata:
  version: "1.1.0"
---

# ds-r-statistics

## Activation boundary

Use for R-based statistical analysis, model fitting, diagnostics, inference and reproducible research. Do not select R solely because a task contains statistical terminology; choose the runtime based on package capability, team workflow and deployment constraints.

## Required context

R version, project structure, package dependencies, data grain, statistical design, output artifacts and reproducibility requirements.

## Workflow

1. Create or inspect a project-local R environment. Pin package versions with renv or an equivalent lockfile and record the R version and system dependencies.
2. Separate raw inputs, derived data, analysis code, outputs and rendered reports. Use explicit project-relative paths and avoid hidden working-directory assumptions.
3. Import data with explicit types and locale/time-zone handling. Validate factor levels, date parsing, missing-value codes and row grain before analysis.
4. Choose statistical functions from the design: independent/paired, clustered, weighted, repeated-measures, survival, time-series or Bayesian. Do not apply a default test based only on variable type.
5. Use model formulas and contrasts explicitly. Inspect residuals, leverage, influence, link assumptions, separation, convergence and collinearity as appropriate.
6. Preserve uncertainty and design structure: cluster-robust inference, survey weights, multiple imputation or time dependence must be handled by design-specific methods.
7. Keep data transformations reproducible with explicit pipelines. Use targets or another dependency-aware workflow when the analysis has multiple expensive stages.
8. Render reports from a clean session and test the project in a fresh library environment. Keep exploratory choices distinct from confirmatory analysis.
9. Export estimates with confidence intervals, effect sizes, sample counts, model specification, package versions and diagnostics.

## Failure modes and abstention

- Do not rely on an interactive workspace image or a saved global environment as the only reproducibility artifact.
- Do not use default contrasts, reference categories or missing-value codes without documenting them.
- Do not suppress warnings about singular fits, separation or convergence.
- If package versions or data access cannot be reproduced, label the result as environment-dependent.

## Validation checklist

- [ ] Project and dependency lockfile are present.
- [ ] Data import and factor/time semantics are explicit.
- [ ] Model assumptions and design-specific variance are checked.
- [ ] A clean-session render succeeds.
- [ ] Results include uncertainty, diagnostics and package versions.

## Authoritative references

- https://cran.r-project.org/manuals.html
- https://rstudio.github.io/renv/
