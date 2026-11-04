---
name: ds-clustering-evaluation
description: Use when selecting, validating, comparing, or interpreting unsupervised clustering and segmentation solutions.
metadata:
  version: "1.1.0"
---

# ds-clustering-evaluation

## Activation boundary

Use for unsupervised segmentation, cluster discovery and cluster stability evaluation. Do not use supervised classification metrics as the primary criterion when labels are absent.

## Required context

Feature grain, entity definition, time window, distance semantics, categorical/numeric mix, scale, missingness, expected cluster use and downstream action.

## Workflow

1. Define what one row represents and whether multiple observations per entity create weighting or leakage.
2. Choose features from the intended construct. Remove identifiers and target leakage; inspect redundancy, scale, skew, outliers and missingness.
3. Select a representation and distance metric that respect data types. Standardization is not automatically correct for sparse, count, compositional or heavy-tailed features.
4. Establish simple baselines before complex methods: k-means for suitable compact numeric clusters, hierarchical methods for interpretable nested structure, Gaussian mixtures for probabilistic ellipsoidal clusters, and density-based methods for irregular shapes/noise.
5. Tune cluster count or density parameters using multiple diagnostics: silhouette, Davies-Bouldin, Calinski-Harabasz, likelihood/information criteria where valid, cluster size, separation and domain interpretability.
6. Test stability under bootstrap/subsampling, feature perturbation, time windows and random seeds. Compare assignments with ARI/NMI only when a meaningful reference labeling exists.
7. Profile clusters using original-scale features, confidence/assignment uncertainty and representative examples. Check whether small clusters are artifacts or valuable rare populations.
8. Validate usefulness against downstream decisions, operational cost, drift and segment actionability; retain an unclustered/noise outcome where appropriate.

## Decision rules

- There is no universally optimal number of clusters.
- Silhouette can favor compact separated groups and penalize valid non-convex or overlapping structures.
- A high internal score does not prove business usefulness or causal segment differences.
- Density-based noise points should not be silently forced into a cluster.

## Failure modes and abstention

- Do not interpret clusters as natural ground truth without stability and external validity.
- Do not use post-outcome variables when the segmentation is intended for pre-outcome decisions.
- Do not compare scores across incompatible distance metrics or feature spaces.
- If clusters are unstable or not actionable, report that segmentation is unsupported.

## Validation checklist

- [ ] Unit, feature semantics and distance metric are explicit.
- [ ] Scaling and missingness treatment are justified.
- [ ] Multiple internal diagnostics and stability checks are used.
- [ ] Cluster profiles are interpretable in original units.
- [ ] Downstream utility and drift are assessed.

## Authoritative reference

- https://scikit-learn.org/stable/modules/clustering.html
