---
name: data-science-experiment-design
description: Design and validate data science experiments, statistical analyses, predictive modeling baselines, and trustworthy model evaluation without data leakage.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Data science experiment and model evaluation

## Activate
Use when the requested deliverable is a scientific analysis, baseline predictive model, hypothesis test, feature/target evaluation, or experimental result. Use data-analytics-metrics for descriptive business metrics, and AI/ML skills for model serving or RAG infrastructure.

## Procedure
1. Write the question, population, unit of analysis, decision, outcome metric, and costs of errors. Distinguish causal and predictive claims.
2. Audit source provenance, missingness, label construction, data collection bias, time boundaries, and train/serving mismatch.
3. Establish simple baselines; select random, group, or temporal splits based on leakage risk and actual deployment.
4. Fit transformations inside training folds only; prevent target leakage, duplicate-entity leakage, and future-information leakage.
5. Choose metrics aligned with prevalence, errors, calibration and business utility. Compare confidence intervals and uncertainty, not just one score.
6. Use cross-validation or a held-out test appropriately. Document sample sizes, assumptions, data shifts and failure slices.
7. Report reproducible steps, random seeds where relevant, dependency versions, data-access constraints, and limitations.

## Evidence and outputs
Provide an explicit experimental design, auditable split strategy, baseline, evaluated results (only if run), confidence/uncertainty, and reproducibility checklist. Never fabricate model scores or infer causality from observational correlation.

## Reference
https://scikit-learn.org/stable/common_pitfalls.html
