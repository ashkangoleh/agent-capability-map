# Data Science: Causal Identification & Experimentation Validity

**Updated:** 2026-11-04  
**Canonical scope:** `data/data-science` on `pre_release`  
**Status:** Existing skills deepened and assignment-unit checks implemented; **not production-certified**.

## Decision and boundaries

Causal identification, randomized A/B experimentation and sequential testing **are not interchangeable**. A credible estimator is not a substitute for identifying assumptions; a passing assignment-ratio check is not a causal estimate; a fixed-horizon p-value repeatedly inspected is not sequentially valid.

| Task intent | Specialist | Critical boundary |
|---|---|---|
| Fixed-horizon A/B design, assignment integrity, sample ratio mismatch (SRM), guardrails | `ds-ab-experimentation` | Independent randomization unit and reliable **pre-outcome assignment** log |
| Group-sequential alpha spending, early stopping or always-valid inference | `ds-sequential-experimentation` | Prespecified monitoring design, error budget, delayed outcomes and boundary calculation |
| Choice/defense of identification strategy | `ds-causal-inference` | Explicit estimand, DAG, assignment/selection assumptions and falsification |
| Observational causal question | `causal-inference-observational` | Unmeasured confounding, overlap, adjustment set, outcome-selection bias |
| Double/debiased ML estimation | `ds-doubleml-causal-estimation` | Cross-fitting reduces nuisance overfit; does **not** create identification |
| Reporting observed experiment metrics | `experiment-analysis-results` (Data Analysis) | Do not misroute reporting tasks into causal study design |

Existing IDs are reused. No duplicate or renamed skills were registered.

## Assignment integrity diagnostic

File: `examples/data_science/assignment_integrity.py`

- Input: iterable of `(randomization_unit_id, assigned_arm)` plus a **predeclared** two-arm allocation map. It counts unique assigned units; repeated identical events are deduplicated and counted; conflicting assignments fail closed.
- Invalid arm, allocation probabilities, unknown variants and malformed records raise errors.
- Only when each expected arm count is at least five, returns Pearson `chi_square` and an approximate df=1 tail probability computed using `math.erfc`; otherwise returns `insufficient_expected_count` with no p-value.
- Default alert threshold is `alpha=0.001`, only a **diagnostic convention**. `no_srm_alarm_detected` is not a proof of unbiased telemetry, correct randomization or effect identification.
- The approximation is intended for **independent assignment** with a fixed allocation probability. Quota/block randomization, differing strata, adaptive assignment, repeated interim monitoring and cluster-level correlation can require another null distribution or design-aware inference.
- **Do not apply this helper to exposure, conversion or outcome rows.** Their missingness/selection often depends on treatment. The study must separately validate assignment/exposure identity, attrition and metric logging.
- Two arms only. Multi-arm, stratified and clustered allocation are explicitly out of scope rather than silently generalized.

### Minimal executable example

```python
from examples.data_science.assignment_integrity import audit_assignment_ratio

events = [(f"user-{i}", "control" if i % 2 else "treatment") for i in range(100)]
result = audit_assignment_ratio(events, {"control": 0.5, "treatment": 0.5})
assert result["status"] == "no_srm_alarm_detected"
assert result["total_randomized_units"] == 100
```

For SRM triage, determine the true unit of randomization, expected allocation by stratum/time, duplicate assignments, bucketing stability, eligibility, enrolment windows, client/app logging loss, bot filters and identity re-keying before interpreting any metric lift. Do not "repair" the split by dropping users.

## Causal and sequential inferential gates

**Causal inference:** Define intervention and estimand first, separate observed vs untestable identification assumptions, reject post-treatment collider/mediator adjustment, assess interference/positivity/measurement. Pre-trend non-significance does not establish DiD parallel trends. DoWhy explicitly separates `model -> identify -> estimate -> refute`, and even refutation success does not prove the graph or absence of confounding.

**Sequential testing:** Freeze hypotheses, allocation, looks/information fractions, type-I error/multiplicity budget, stopping boundaries and delayed-outcome rules before analyzing treatment effects. Alpha spending controls *cumulative* error; it is not an unadjusted p-value threshold for every interim look. Adaptive allocation and continuously monitored p-values require methods justified for those designs.

## Evidence collected in this increment

- `tests/test_data_science_assignment_integrity.py`: **18/18 locally executed** against source-equivalent standard-library code, including balanced and distorted allocation, duplicate events, conflicting assignment, small counts, malformed arms, numeric/NaN thresholds and non-50/50 assignment.
- `tests/test_data_science_causal_experimentation.py`: registered 12 distinct positive/negative-domain routing fixtures with expectations for fixed-horizon, sequential, causal design, bilingual SRM, observational and Data Analysis reporting.
- `tests/fixtures/yaml-routing-cases.yaml`: **408 declared cases** after this increment; `catalog/master-skill-ids.yaml` remains **344 unique IDs**.
- A separate **JavaScript reconstruction of deterministic lexical matching** against the GitHub YAML matched the proposed routing requests. This is **not** execution of Python `Router.resolve`, the entire fixture suite, or a measured model/agent accuracy benchmark.
- **GitHub Actions push CI and the full Python validator/unit suite have not been independently verified** against the new branch HEAD.

## Acceptance commands

Run on the exact newest `pre_release` checkout and record SHA and logs:

```sh
python -m capability_map validate
python scripts/evaluate_graph.py
python scripts/report_coverage.py --summary
python -m unittest discover -s tests -p 'test_data_science_assignment_integrity.py' -v
python -m unittest discover -s tests -p 'test_data_science_causal_experimentation.py' -v
python -m unittest discover -s tests -v
```

Additional proof required before declaring this family complete: real-source assignment/exposure consistency, stratified and clustered tests, randomized A/A calibration, a version-pinned causal estimator example with deliberately broken identification assumptions, and a simulated group-sequential design that measures empirical type-I error and power. Host-specific skill invocation and Persian/English ambiguous task evaluation remain open.

## Primary/official sources

- [DoWhy causal estimation methodology](https://www.pywhy.org/dowhy/v0.11/user_guide/causal_tasks/estimating_causal_effects/index.html): formalize, identify, estimate, refute
- [DoubleML sample splitting](https://docs.doubleml.org/stable/guide/resampling.html): cross-fitting and nuisance estimation limits
- [Online experiment SRM diagnosis, KDD 2019](https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf): diagnostics and data integrity
- [Penn State interim analysis and alpha spending](https://online.stat.psu.edu/stat509/Lesson10): sequential error-control and information time

**Next inside Data Science:** independent statistical validation of conformal prediction and probability calibration, then forecasting and inference/survey methods. Keep Data Science and the entire top-level Data domain incomplete pending their remaining gates.
