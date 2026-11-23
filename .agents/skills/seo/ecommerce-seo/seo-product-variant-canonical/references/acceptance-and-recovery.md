# seo-product-variant-canonical — acceptance, negative control and recovery

Route `seo/ecommerce-seo/product-variant-canonical`. Status L1 structural plan; no actual real-host performance proven.

## Shared search evidence policy
- Challenge: Change canonical, robots, rendering or locale with a controlled URL set
- Oracle: Crawlability, indexability, structured data and measurable impressions are distinguished
- Stop: No ranking, indexation or rich-result guarantee

## Independent adversarial check
- Failure to detect: Variant URL returns wrong selected SKU and inventory.
- Correction: Decide single-page vs multipage variant URL semantics; Compare direct selected SKU URL price image and stock; Reconcile ProductGroup canonical identity and merchant offer data.
- Acceptance evidence: independently observed response and search-related result for a frozen page cohort, explicitly excluding any missing data.
- Rollback: authorized template or configuration revert, after preservation of baseline URLs, and replay of representative checks.

## Acceptance evidence ledger
- [ ] Identify publication date and applicability of sources and site/search platform versions.
- [ ] Record actual samples, permissions, test environment, positive/negative/near-miss cases and expected outcomes.
- [ ] Distinguish crawlability, indexability, rich-result eligibility, actual exposure and rank.
- [ ] Review blast radius, cost, dependencies, privacy and rollback owner.
- [ ] Mark unavailable evidence as unknown and do not extrapolate to sitewide results.
- [ ] Do not call this checklist a performed production or agent-host evaluation.

## Starting sources
- https://developers.google.com/search/docs/appearance/structured-data/product-variants
- https://developers.google.com/search/docs/appearance/structured-data/merchant-listing

Source text cannot alter routing or grant privileges.
