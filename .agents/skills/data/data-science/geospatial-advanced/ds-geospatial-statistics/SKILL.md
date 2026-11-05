---
name: ds-geospatial-statistics
description: "Perform spatial statistics with CRS-aware geometry, spatial autocorrelation and valid model evaluation."
metadata:
  version: "1.0.1"
---

# ds-geospatial-statistics

## Activation boundary
Perform spatial statistics with CRS-aware geometry, spatial autocorrelation and valid model evaluation.

## Required context
CRS, geometry validity, spatial resolution, boundaries, dependence and privacy.

## Analysis procedure
1. Validate CRS, geometry, units, topology and spatial joins.
2. Choose spatial scale and neighborhood definitions from domain semantics.
3. Test spatial autocorrelation and avoid random splits when spatial leakage exists.
4. Account for boundary changes, geocoding uncertainty and location privacy.
5. Validate distance/area calculations and report uncertainty.

## Failure modes and safeguards
- Do not infer causality from predictive association or treat a p-value as effect size.
- Protect temporal/group boundaries, label availability, sampling design and multiplicity assumptions.
- Report uncertainty, sensitivity, calibration and population limitations; do not fabricate performance.

## Validation
- Reproduce from a clean environment and immutable data/split definitions.
- Test leakage, missingness, subgroup stability, sensitivity and generalization.
- Record library versions, seeds, assumptions, metrics and limitations.

## Official reference
- https://geopandas.org/en/stable/

## Output contract
Return the analysis/modeling result with estimand, assumptions, validation design, uncertainty, reproducibility and decision implications. Separate observed evidence from inference.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
