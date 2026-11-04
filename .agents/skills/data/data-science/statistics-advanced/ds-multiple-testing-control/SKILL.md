---
name: ds-multiple-testing-control
description: Use when controlling family-wise error or false discovery across multiple hypotheses, metrics, segments, features, or repeated analyses.
metadata:
  version: "1.0.0"
---

# ds-multiple-testing-control

## Activation boundary

Use when more than one hypothesis contributes to a scientific or product conclusion. It covers confirmatory families, exploratory discovery and structured testing programs.

## Required context

Hypothesis family, primary/secondary outcomes, number of tests, dependence structure, confirmatory status, alpha budget, repeated looks and decision consequences.

## Workflow

1. Define the family of hypotheses before examining results. Explain whether it is all outcomes, all segments, all model variants, all time windows or a hierarchical family.
2. Separate confirmatory tests from exploratory discovery. Freeze primary endpoints and planned contrasts before outcome inspection.
3. Choose the error criterion:
   - family-wise error rate for confirmatory claims where any false positive is costly;
   - false discovery rate for discovery settings where a controlled expected proportion of false discoveries is acceptable;
   - hierarchical gatekeeping or alpha allocation when tests have a predeclared dependency structure.
4. Select a procedure with a defensible dependence assumption. Holm controls family-wise error under general dependence; Benjamini-Hochberg controls FDR under independence or suitable positive dependence; Benjamini-Yekutieli is more conservative under arbitrary dependence.
5. Account for repeated looks and adaptive selection separately. Ordinary post-hoc adjustment does not repair invalid optional stopping or outcome-driven family changes.
6. Report raw p-values, adjusted p-values or q-values, family size, procedure, alpha and dependence assumptions.
7. Report effect sizes and uncertainty intervals alongside adjusted significance. A small adjusted p-value does not imply practical importance.
8. For large-scale discovery, validate selected findings on independent data or a predeclared replication stage.

## Error-control and family integrity gate

1. Freeze **all tested hypotheses in one decision family**, including unreported negative comparisons and exploratory segments. Record the family key, the complete ordered p-value list, test validity assumptions and confirmatory/exploratory status. If family selection followed results, adjusted p-values do not recover pre-registered confirmatory error control.
2. Select the target error metric **before seeing p-values**: `FWER` (e.g. Bonferroni/Holm) bounds the probability of at least one false rejection; `FDR` (BH/BY) bounds the *expected false discovery proportion* for the specified dependence conditions. Neither adjusted p-values nor FDR represent posterior probabilities that each hypothesis is true.
3. Match the procedure to dependence and stopping: Holm controls FWER without independence; BH controls FDR for independent or suitably positively dependent tests; BY is more conservative and supports broader dependence. Repeated peeking, adaptive test creation and multi-stage selection need procedures justified for those settings, not only an end-of-run BH adjustment.
4. Use `examples/data_science/inference_integrity.py::adjust_pvalues` for a bounded, standard-library **arithmetic audit** of Bonferroni, Holm, BH and BY. Original hypothesis order is preserved, ties are stable, invalid/nonfinite p-values fail closed. Do not claim that this helper verifies that individual p-values are statistically valid.
5. Compare `adjusted_pvalues` and reject flags to release-pinned `statsmodels.stats.multitest.multipletests`. For reproducibility report sorted and original hypothesis IDs, family size, chosen alpha, dependence assumptions, method, adjusted decisions, confidence intervals and practical effect sizes.

### Executable arithmetic audit

```python
from examples.data_science.inference_integrity import adjust_pvalues

result = adjust_pvalues([0.04, 0.001, 0.03, 0.20], method="fdr_bh")
assert result["reject"] == [False, True, False, False]
```

This is not proof of control under optional stopping or invalid p-values. Never derive a test family from observed significance.

## Failure modes and abstention

- Do not choose the correction after seeing which one makes results significant.
- Do not silently shrink the hypothesis family after observing outcomes.
- Do not treat FDR control as a guarantee that each reported finding is true.
- Do not use a fixed-horizon correction to justify repeated unplanned peeking.
- If the family cannot be reconstructed, label the analysis exploratory and do not claim confirmatory error control.

## Validation checklist

- [ ] Hypothesis family and confirmatory status are explicit.
- [ ] Error criterion matches decision risk.
- [ ] Dependence and repeated-look assumptions are documented.
- [ ] Adjusted values and effect sizes are reported.
- [ ] Independent validation is planned for discovery results.

## Authoritative references

- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.false_discovery_control.html
- https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html
