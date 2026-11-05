# ds-clustering-evaluation: specialist evaluation and negative controls

Domain `data/data-science/modeling`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define what one row represents and whether multiple observations per entity create weighting or leakage.
2. Choose features from the intended construct. Remove identifiers and target leakage; inspect redundancy, scale, skew, outliers and missingness.
3. Select a representation and distance metric that respect data types. Standardization is not automatically correct for sparse, count, compositional or heavy-tailed features.
4. Establish simple baselines before complex methods: k-means for suitable compact numeric clusters, hierarchical methods for interpretable nested structure, Gaussian mixtures for probabilistic ellipsoidal clusters, and density-based methods for irregular shapes/noise.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not interpret clusters as natural ground truth without stability and external validity.
- Do not use post-outcome variables when the segmentation is intended for pre-outcome decisions.
- Do not compare scores across incompatible distance metrics or feature spaces.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://scikit-learn.org/stable/modules/clustering.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
