# Data Science — Statistical Inference, Complex Surveys and Missingness

**Date:** 2026-11-05  
**Scope:** `data/data-science/statistics-advanced` on `pre_release`  
**Status:** Five existing specialist skills deepened. Local numerical tests executed; full repository routing/CI, design-specific uncertainty and statistical production validity **not independently verified**.

## Decision matrix

| Requested inference | Existing specialist | Error condition / reason to abstain |
|---|---|---|
| Many outcomes/segments: Bonferroni, Holm, BH or BY adjusted p-values | `ds-multiple-testing-control` | Hypothesis family selected after results, invalid base p-values, unspecified dependence or repeated stopping |
| Weighted, stratified, cluster or multi-stage survey population estimate | `ds-survey-sampling-design` | Inclusion/sampling design unknown, lonely PSUs, nonresponse and weights without provenance |
| MCAR/MAR/MNAR missingness, multiple imputation or sensitivity analysis | `ds-missing-data` | Missingness may be MNAR, imputation parameters mismatched, inferential uncertainty not pooled |
| Rank-based, permutation or bootstrap statistical inference | `ds-robust-nonparametric-inference` | Wrong exchangeable/independent unit, paired/clustered dependence omitted, degenerate BCa intervals |
| Bayesian priors, posterior predictions and MCMC | `ds-bayesian-pymc-stan` | Divergent/nonconverged chains, low ESS, poor posterior predictive fit or unidentified likelihood |

No new skill IDs. Generic confidence intervals stay with `statistical-inference-design`; conformal predictive intervals, sequential experiments and feature engineering retain their own specialists.

## Executable arithmetic and survey-design guard

`examples/data_science/inference_integrity.py` contains only **bounded numerical preconditions**, not statistical estimation for arbitrary dependence:

1. `adjust_pvalues(pvalues, method, alpha)` implements `bonferroni`, `holm`, `fdr_bh`, and `fdr_by`, retaining original hypothesis ordering and rejecting invalid inputs. A procedure's advertised error-rate control requires valid original p-values, a defined family and relevant independence/dependence assumptions. A BH adjusted value is **not** a probability the individual hypothesis is true.
2. `survey_design_guard(values, weights, strata, psus)` validates consistent, non-empty design fields, strictly positive finite weights and at least two distinct PSUs in each supplied stratum. Reports only a **descriptive weighted mean and Kish weight-only effective sample size**. The returned `design_based_standard_error` is deliberately `None`. It does **not** compute a survey variance, design effect, population margin of error, or valid confidence interval. Certainty strata and known lonely-PSU variance conventions need a design-specific method, not silent correction.
3. `pool_scalar_imputations(estimates, within_variances)` uses Rubin's scalar pooling:
   `Qbar = mean(Q_i)`, `Ubar = mean(U_i)`, `B = sample_variance(Q_i)`, `T = Ubar + (1 + 1/m) * B`; pooled standard error is `sqrt(T)`. Confidence interval is deliberately `None`, because degrees of freedom, complete-data inference and MI/complex-sample adjustments are not implemented. **Pool coefficients/estimands and their variance estimates, not imputed rows.**

### Reproducible simple example

```python
from examples.data_science.inference_integrity import (
    adjust_pvalues, survey_design_guard, pool_scalar_imputations
)

adjusted = adjust_pvalues([0.04, 0.001, 0.03, 0.2], method="fdr_bh")
assert adjusted["reject"] == [False, True, False, False]

survey = survey_design_guard(
    [1, 3, 5, 7], [1, 1, 2, 2],
    strata=["region"] * 4,
    psus=["cluster-a", "cluster-a", "cluster-b", "cluster-b"],
)
assert survey["design_based_standard_error"] is None

pooled = pool_scalar_imputations([4, 6, 5], [1, 1, 1])
assert pooled["pooled_estimate"] == 5
assert pooled["confidence_interval"] is None
```

**These values are illustrative arithmetic, not inferred population outcomes.**

## Statistical validation and operational failure realism

- **Multiple testing:** Holm FWER under general dependence; BH FDR under independent/suitable positive dependence; BY FDR for general dependence with lower power. Changing a prespecified hypothesis family or looking repeatedly at results invalidates the advertised decision protocol; no correction retroactively repairs data-driven test selection.
- **Complex surveys:** PSU identifiers can repeat across strata when nested deliberately, as in `survey::svydesign(nest=TRUE)`. A design-based standard error needs actual stage/strata/weights/FPC information and a design-aware variance estimator (Taylor linearization or valid replicates). Dropping out-of-domain records before subgroup variance analysis can change the variance. A weighted point estimate does not certify representativeness or remove nonresponse bias.
- **Multiple imputation:** MCAR/MAR/MNAR hypotheses are not generally identifiable by inspecting observed values alone. For real MI run an imputation model with diagnostic checks and fit each analysis model separately. A valid confidence interval needs an appropriate degrees-of-freedom procedure and compatibility with complex survey and finite sample corrections.
- **Robust statistics:** BCa bootstrap, permutation and rank-based tests depend on resampling/assignment units and model assumptions. `scipy.stats.bootstrap(paired=True)` preserves paired index resampling; it does not create cluster-aware inference or prevent degeneracy in tiny/constant samples.
- **Bayesian:** posterior predictive checks, prior sensitivity and MCMC diagnostics (divergences, rank-normalized R-hat, ESS, MCSE, BFMI) are complementary. No threshold alone can certify identification, likelihood validity or causal claims. Pin PyMC and ArviZ versions because published APIs evolve.

## Test evidence (accurate scope)

- `tests/test_data_science_inference_integrity.py`: **23/23 actual local Python tests passed** after catching and repairing numeric overflow during Rubin pooling. The source and test files are committed verbatim in GitHub and their Git blob SHAs were checked against the files executed locally.
- Cross-implementation numerical verification: **600 local cases** for Bonferroni, Holm, BH and BY (150 method-specific comparisons each) returned adjusted p-values and rejection flags matching installed `statsmodels 0.14.6` using `numpy 2.3.5` and `SciPy 1.17.0`. Inputs were seeded random cases across family sizes `1, 2, 3, 5, 20, 100`. This verifies arithmetic on tested values, not the assumptions of a scientific study.
- `tests/test_data_science_inference_routing.py`: created with **22** `ds-inference-*` positive, bilingual and near-miss fixture cases. A separate JavaScript recreation of the deterministic lexical router matched **22/22** requests against the current YAML graph; this is **not** actual Python Router execution or a semantic LLM benchmark.
- Historical fixture count before this increment: **445**; current declared total: **467**. The skill ID index remains **344 unique IDs**.
- **NOT VERIFIED:** full `Router.validate` and all Python suites at current branch HEAD, actual GitHub Actions push run, real survey inference on released `survey` tooling, a fitted MICE example, actual Bayesian chains/posterior predictive checks, version-pinned bootstrap simulations or real host invocation.

### Acceptance commands

```sh
git rev-parse HEAD
python -m capability_map validate
python scripts/evaluate_graph.py
python scripts/report_coverage.py --summary
python -m unittest discover -s tests -p 'test_data_science_inference_integrity.py' -v
python -m unittest discover -s tests -p 'test_data_science_inference_routing.py' -v
python -m unittest discover -s tests -v
```

Then reproduce a design-based population estimate/standard error from released R `survey`, an actual `mice::pool` (or correctly versioned Python MICE) inference experiment, a clustered/paired resampling example, and an ArviZ/PyMC posterior diagnostic example with intentionally bad chains. Record library versions, sample design, seeds, failure behavior and comparison with independent references.

## Verified primary/official references

- [statsmodels multiple testing](https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html)
- [SciPy BH/BY FDR adjustment](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.false_discovery_control.html)
- [R survey design, PSUs, nesting, fpc](https://r-survey.r-forge.r-project.org/pkgdown/docs/reference/svydesign.html)
- [mice pooling estimates rather than rows](https://search.r-project.org/CRAN/refmans/mice/html/pool.html)
- [statsmodels MICE](https://www.statsmodels.org/stable/imputation.html)
- [SciPy bootstrap API, paired and BCa](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html)
- [ArviZ sampler diagnostics](https://python.arviz.org/projects/stats/en/latest/api/generated/arviz_stats.diagnose.html)
- [PyMC usage and posterior validation](https://www.pymc.io/projects/docs/en/stable/learn/usage_overview.html)

## Next Data Science workstream

Audit the remaining scientific specialists and the cross-skill routing/abstention behavior—especially statistical power, survival analysis, fairness, recommendation, simulation/optimization and multilingual scientific NLP. Before marking Data Science complete, run the actual full Python suite and host behavior/evaluation against a reproducible sample of tasks, and get independent expert review. **The overall Data top-level domain remains incomplete, with seven other subdomains awaiting depth review and Data Engineering operational gaps still open.**
