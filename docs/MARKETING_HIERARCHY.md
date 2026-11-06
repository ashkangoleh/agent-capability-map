# Marketing domain expansion and verification boundary — 2026-11-06

Target branch: `pre_release`. Baseline: `1a109687ca81e05497e6748360d368586098d183`.

## Implemented hierarchy
- `marketing/campaign-strategy`: `campaign-plan` (`marketing-strategy-campaign`, preserved), `launch-readiness` (`marketing-launch-readiness`)
- `marketing/performance-marketing`: `budget-pacing` (`marketing-spend-pacing`), `creative-experimentation` (`marketing-creative-experimentation`), `landing-page-qa` (`marketing-landing-page-conversion-qa`)
- `marketing/brand-positioning`: `audience-research` (`marketing-audience-research-evidence`), `message-validation` (`marketing-brand-message-validation`)
- `marketing/lifecycle-crm`: `consent-suppression` (`marketing-consent-suppression`), `journey-holdouts` (`marketing-lifecycle-journey-holdouts`), `email-deliverability` (`marketing-email-deliverability`)
- `marketing/marketing-analytics`: `event-attribution` (`marketing-measurement-attribution`, preserved), `incrementality` (`marketing-incrementality-geo-lift`), `offline-conversions` (`marketing-offline-conversion-reconciliation`)
- `marketing/influencer-partnerships`: `creator-disclosure` (`marketing-creator-disclosure-review`), `affiliate-integrity` (`marketing-affiliate-payout-integrity`)
- `marketing/marketing-operations`: `campaign-taxonomy` (`marketing-campaign-taxonomy-utm`), `release-controls` (`marketing-campaign-release-controls`)

**Structural inventory:** 7 subdomain maps; 17 active leaf routes; 15 new canonical skill files; 24 new hierarchical role contracts. Portfolio target: 453 skills, 432 roles, 41 main domains and 32 still-singleton domains. The previous two marketing skill IDs and SKILL.md bodies are unchanged.

## Decision boundaries
- **Marketing** covers paid channel operations, lifecycle permission checks, causal advertising measurement, branding and creator disclosure.
- **SEO** covers crawl/indexation/rich results, not paid creative or marketing analytics.
- **Data Science** owns generic statistical experimental methods; Marketing owns channel-specific design, identity, spend and compliance.
- **Data Engineering** owns pipelines, storage and ETL implementations; Marketing owns source-to-conversion event semantics and reconciliation criteria.
- **Product** owns product analytics/feature experimentation; Marketing owns acquisition exposures and lifecycle messaging.
- User-enforced scope selection (up to five non-overlapping domain scopes) is untouched.

## Official research starting points
- GA4 event names and validation: https://support.google.com/analytics/answer/9267735/
- Google Ads Conversion Lift and its availability conditions: https://support.google.com/google-ads/answer/12003020
- Google Ads API conversions, account ownership and partial failures: https://developers.google.com/google-ads/api/docs/conversions/overview
- Marketing mix model calibration to experiments: https://developers.google.com/meridian/docs/advanced-modeling/roi-priors-and-calibration
- ICO direct marketing guidance, updated 2026: https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/
- Google bulk sender authentication: https://support.google.com/mail/answer/81126?hl=en-GB
- FTC material endorsements: https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers
- AAPOR research practices: https://aapor.org/standards-and-ethics/best-practices/

These are starting sources, not endorsements that every platform feature or law is available in all jurisdictions. Refresh sources for the actual campaign region, API release and provider account.

## Acceptance gates and remaining gaps
1. Validate all YAML/skills/role paths and new canonical IDs at exact new commit.
2. Run a positive and a near-miss regression for every new skill, plus historical marketing/SEO/Product/Data cases.
3. Verify role inheritance stays within the selected route and does not bypass the user domain allowlist.
4. Run actual host agent evaluations for routing choice, business correctness, consent violations, cost and abstention; structural tests **do not** supply this evidence.
5. Do not infer revenue lift from last-click attribution. No performance forecast is grounded without campaign data.
6. Legal requirements are jurisdiction-dependent; qualified review required before production creator, privacy or regulated campaign advice.

**Status:** L1 structural candidate pending exact-head CI; L2/L3/L4 NOT VERIFIED.
