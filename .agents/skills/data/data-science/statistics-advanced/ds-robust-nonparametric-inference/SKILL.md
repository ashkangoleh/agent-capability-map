---
name: ds-robust-nonparametric-inference
description: Use when choosing robust, rank-based, permutation, bootstrap, or distribution-free inference under non-standard data assumptions.
metadata:
  version: "1.0.0"
---

# ds-robust-nonparametric-inference

## Activation boundary

Use when classical parametric assumptions are doubtful, outcomes are heavy-tailed or ordinal, or inference requires robust resampling. This skill does not mean that nonparametric methods are assumption-free.

## Required context

Estimand, outcome scale, independent/paired/clustered unit, sampling design, sample size, missingness, hypothesis family and dependence structure.

## Workflow

1. Define the estimand and experimental/sampling unit. Decide whether observations are independent, paired, repeated or clustered.
2. Inspect distribution, outliers, heteroskedasticity, ties, censoring and group-size imbalance. Do not use a normality-test p-value as the sole method selector.
3. Choose a statistic aligned to the estimand: mean/trimmed mean, median, quantile, rank effect, probability of superiority or another interpretable contrast.
4. Select a procedure whose null and assumptions match the design:
   - Welch-type methods for unequal variances under suitable conditions;
   - Mann-Whitney for rank/distributional comparison, not automatically a median test;
   - Wilcoxon signed-rank only with its symmetry assumptions for paired differences;
   - Kruskal-Wallis for independent multi-group rank comparisons;
   - permutation tests only when the permutation scheme preserves exchangeability and the assignment/sampling design;
   - bootstrap intervals by resampling the independent sampling unit or cluster.
5. For skewed or heavy-tailed data, compare robust estimators such as trimmed means, medians and median absolute deviation. State the target each estimator represents.
6. Use exact or Monte Carlo resampling according to sample size and computational budget. Record resample count, random generator and Monte Carlo error.
7. Report effect size and interval, not only a p-value. Apply the relevant multiplicity policy when many outcomes or subgroups are tested.
8. Run sensitivity checks to influential observations, alternative statistics and plausible dependence structures.

## Resampling validity and stopping gate

1. Define the estimand and **resampling unit** before selecting a method. IID row bootstrap fails for correlated panels, randomization by clusters and matched pairs. Paired data require resampling the same observation indices across input arrays; clustered designs require cluster-preserving resampling.
2. A permutation p-value is valid only with an exchangeable null distribution and a permutation scheme consistent with treatment assignment/sampling. Shuffling individual outcomes between randomized clusters destroys the actual randomization mechanism.
3. In release-pinned SciPy, `scipy.stats.bootstrap` supports `paired=True`, `method="BCa"` and an explicit random generator. BCa may be degenerate for constant statistics, tiny samples or influence outliers: detect warnings/NaN endpoints and report the interval as unsupported rather than silently substituting a narrow interval.
4. For Monte Carlo methods, record generator state, exact resamples, randomized test-unit count, null statistic and uncertainty from finite resamples; do not conflate a Monte Carlo approximation with the exact randomization distribution. Use a preregistered adaptive stop criterion only if its inference remains valid.
5. Compare robust location/scale estimates with the original estimand, include subgroup/outlier sensitivity and correct multiplicity across reported comparisons.

## Failure modes and abstention

- Do not interpret Mann-Whitney as a test of medians unless additional distribution-shape assumptions hold.
- Do not permute individual rows when randomization occurred by cluster or matched pair.
- Do not bootstrap correlated observations as IID.
- Do not call a method assumption-free; identify exchangeability, symmetry, independence or sampling assumptions.
- If the design does not support the chosen resampling scheme, abstain from inferential claims.

## Validation checklist

- [ ] Estimand and resampling unit are explicit.
- [ ] Test assumptions match the design.
- [ ] Effect size and uncertainty interval are reported.
- [ ] Monte Carlo error and multiplicity are addressed.
- [ ] Sensitivity to outliers and dependence is checked.

## Authoritative references

- https://docs.scipy.org/doc/scipy/reference/stats.html
- https://www.statsmodels.org/stable/stats.html
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html
