---
name: data-analytics-metrics
description: Build trustworthy analytical metrics, funnel, cohort, retention or segmentation analysis with verified data grain, SQL correctness, and denominator definitions.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Analytics metrics and insight generation

## Activate
Use for descriptive analytics, KPI calculations, funnel and cohort analyses, dashboards and SQL validation. Business operating decisions and commercial KPI ownership route to business-analytics-kpi; data pipeline implementation routes to data-engineering-implementation.

## Procedure
1. Confirm the business question, decision owner, time zone, period, filters, cohorts and expected level of detail.
2. Define event/entity grain, stable keys, deduplication, late events, exclusion policies and numerator/denominator contracts before querying.
3. Inspect real schemas and metric lineage; do not assume all events represent unique users or orders.
4. Build the smallest query or semantic metric definition. Validate distinct counts, nulls, joins, time windows, and denominator drift.
5. Reconcile totals against known aggregates or source truth. Test partial data, missing partitions, and changes in instrumentation.
6. Distinguish association from causation, report uncertainty and confounders, and state which decision the result actually supports.

## Outputs
Metric contract, tested SQL or computation, validation checks, segment/cohort results if data is available, caveats and action-oriented interpretation. Do not invent values or trends.

## Reference
https://www.getdbt.com/blog/what-is-a-semantic-layer
