---
name: ds-shap-explainability
description: Use when explaining model predictions or feature contributions with SHAP while checking attribution assumptions, stability, and interpretation limits.
metadata:
  version: "1.1.1"
---

# ds-shap-explainability

## Activation boundary

Use for local or global feature-attribution analysis of a fitted predictive model. Do not use SHAP values as causal effects, feature-selection proof or a substitute for model validation.

## Required context

Model type, output scale, feature pipeline, background/reference population, correlated features, prediction cohort and intended audience.

## Workflow

1. Define the explanation target: raw margin, probability, log-odds, expected value or another model output. State the scale in every report.
2. Verify the model and preprocessing pipeline are frozen and match the prediction path. Explain the same feature representation the model actually consumes.
3. Select a background dataset that represents the intended reference population. Document sampling, time window and privacy constraints.
4. Choose an explainer appropriate to the model and computational budget. Verify whether the implementation uses conditional, interventional or another feature-dependence assumption.
5. Check local additivity/reconstruction and compare explanations with model outputs. For sampled explainers, measure Monte Carlo variability.
6. Summarize global patterns across representative cohorts, not only mean absolute values. Inspect sign, distribution, interactions and subgroup variation.
7. Investigate correlated features and proxy variables. Attribution can be redistributed among correlated inputs and can change with the background distribution.
8. Compare with permutation importance, partial dependence or accumulated local effects where useful. Test explanation stability across time, seeds and nearby observations.
9. Communicate that attribution describes model behavior under the chosen explainer assumptions; it does not identify a causal effect or validate the model.

## Decision rules

- Mean absolute SHAP is magnitude, not direction or causal importance.
- Feature attribution is conditional on the model, data representation and reference distribution.
- Local explanations can be unstable even when global summaries look smooth.
- A feature's absence from a top-k plot does not prove irrelevance.

## Failure modes and abstention

- Do not explain a model with a different preprocessing pipeline from production.
- Do not compare SHAP values across models or cohorts without compatible scales and baselines.
- Do not infer intervention outcomes from observational attributions.
- If explanations are unstable or reference data are unrepresentative, state that the attribution is not reliable for the intended claim.

## Validation checklist

- [ ] Output scale and reference population are documented.
- [ ] Explainer assumptions and dependence handling are explicit.
- [ ] Local reconstruction and stability are checked.
- [ ] Correlation and subgroup effects are reviewed.
- [ ] Causal claims are explicitly excluded.

## Authoritative reference

- https://shap.readthedocs.io/en/latest/

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
