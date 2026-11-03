---
name: marketing-attribution-audit
description: Audit marketing campaign tracking, acquisition and attribution metrics, channel reporting and conversion measurement while accounting for consent, missing data and confounders.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Marketing attribution and measurement

## Activate
Use when a marketer requests campaign tracking design, UTM governance, conversion attribution diagnosis, ROAS/CAC interpretation or experiment measurement. General channel and positioning strategy stays with marketing-strategy-campaign.

## Procedure
1. Identify business objective, conversion definition, observation window, channels, spend basis, geography and consent constraints.
2. Trace events and identity mapping from ad/campaign identifiers to sessions, conversion tables, refunds and reporting; document missing data.
3. Validate UTM conventions, deduplication, bot filtering, time zone and attribution lookback assumptions.
4. Distinguish platform-reported conversions, first-party observed conversions, multi-touch attributions and causal incrementality; do not present any as interchangeable.
5. Reconcile source-to-report totals, define sensitivity analyses and identify instrumentation or consent bias.
6. Recommend lean improvements and a controlled incrementality test when causal lift matters.

## Outputs
Tracking contract, evidence-backed attribution limitations, QA tests, prioritized fixes and measurement recommendations.

## Reference
https://developers.google.com/tag-platform
