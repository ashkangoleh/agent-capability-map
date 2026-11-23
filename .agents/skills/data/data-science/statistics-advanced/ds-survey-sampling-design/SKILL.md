---
name: ds-survey-sampling-design
description: Use when analyzing probability or complex survey samples with strata, clusters, unequal weights, nonresponse, or replicate-weight variance.
metadata:
  version: "1.0.1"
---

# ds-survey-sampling-design

## Activation boundary

Use for survey estimates where inclusion probabilities, stratification, clustering or nonresponse affect estimation and uncertainty. Do not treat survey weights as ordinary row multipliers without understanding their design role.

## Required context

Target population, sampling frame, strata, primary sampling units, inclusion probabilities, final weights, nonresponse adjustments, finite population information and replicate weights.

## Workflow

1. Document the target population, sampling frame, unit selection stages, strata, clusters and inclusion probabilities.
2. Distinguish base design weights from nonresponse-adjusted, calibrated, post-stratified or trimmed final weights. Preserve the weight construction metadata.
3. Assess frame undercoverage, nonresponse, extreme weights, positivity and the difference between the sample and target population.
4. Declare the full survey design before estimating totals, means, proportions, regression or subgroup/domain estimates.
5. Choose variance estimation consistent with the design: Taylor linearization or supplied replicate weights such as BRR, jackknife or bootstrap. Apply finite population corrections only when the design supports them.
6. Report weighted estimates with design-based standard errors, confidence intervals, effective sample size and design effects. Do not use IID standard errors on a clustered/stratified sample.
7. Estimate subpopulation/domain results using survey-domain methods rather than physically dropping out-of-domain records before variance estimation.
8. Run sensitivity to weight trimming, calibration, nonresponse assumptions and influential clusters. State when small-area estimates require additional modeling.

## Survey-design and variance gate

1. Reconstruct the actual probability design: eligibility and frame, inclusion probabilities, sampling stage, strata, PSU and second-stage IDs, final weights, nonresponse/weight calibration and **finite population correction** (FPC). Avoid interpreting non-probability convenience samples as design-based representative populations.
2. For one-stage structural sanity checks use `examples/data_science/inference_integrity.py::survey_design_guard`: it checks finite positive weights, consistent strata/PSU identifiers and flags a **lonely PSU** stratum. The returned weighted mean is **descriptive**; its Kish weight-based effective sample size ignores clustering and is *not* a design effect or variance estimate. `design_based_standard_error` is deliberately `None`.
3. For inference, use a released design-aware implementation: e.g. `survey::svydesign` followed by `svymean` or `svytotal`. Specify `ids`, `strata`, `weights`, `fpc`, and `nest=TRUE` where PSU IDs repeat between strata; alternatively provide validated replicate weights and documented bootstrap/BRR/jackknife conventions. Preserve strata and PSUs for domain analysis.
4. Resolve lonely-PSU handling according to the design: certainty units, explicit adjustment rules, pooling strata if supported or refusal when variance is not identifiable. Never silently replace design-based uncertainty with IID variance or divide by `sqrt(n)`.
5. Audit population coverage, nonresponse, missingness, weight trimming, design effects, cross-stratum identification and effective sample size. Report target population and changes to the estimand under weighting/trimming.

### Executable design check

```python
from examples.data_science.inference_integrity import survey_design_guard

result = survey_design_guard(
    [1, 3, 5, 7], [1, 1, 2, 2],
    strata=["region"] * 4,
    psus=["cluster-a", "cluster-a", "cluster-b", "cluster-b"],
)
assert result["design_based_standard_error"] is None
```

This helper is **not** a complex survey variance estimator. A valid design-specific confidence interval requires an actual survey analysis package and verified sampling assumptions.

## Failure modes and abstention

- Do not assume weighting removes nonresponse or coverage bias.
- Do not use unweighted sample counts as population totals.
- Do not treat weights as frequency weights unless that interpretation is correct.
- Do not ignore lonely PSUs, certainty strata or replicate-weight conventions.
- If the sampling design or weight provenance is unknown, do not report design-based population inference.

## Validation checklist

- [ ] Target population and sampling frame are documented.
- [ ] Weight construction and design variables are verified.
- [ ] Variance method matches the sampling design.
- [ ] Subpopulation estimates preserve design information.
- [ ] Nonresponse, coverage and weight sensitivity are reported.

## Authoritative references

- https://r-survey.r-forge.r-project.org/pkgdown/docs/index.html
- https://stat.ethz.ch/CRAN/web/packages/survey/index.html
- https://r-survey.r-forge.r-project.org/pkgdown/docs/reference/svydesign.html
- https://search.r-project.org/CRAN/refmans/survey/html/svydesign.html

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
