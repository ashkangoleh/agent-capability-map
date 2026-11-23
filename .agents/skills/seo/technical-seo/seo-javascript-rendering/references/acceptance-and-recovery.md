# seo-javascript-rendering — acceptance, negative control and recovery

Route `seo/technical-seo/javascript-rendering`. Status L1 structural plan; no actual real-host performance proven.

## Shared search evidence policy
- Challenge: Change canonical, robots, rendering or locale with a controlled URL set
- Oracle: Crawlability, indexability, structured data and measurable impressions are distinguished
- Stop: No ranking, indexation or rich-result guarantee

## Independent adversarial check
- Failure to detect: A browser loads content while search renderer omits it.
- Correction: Compare initial HTML and crawler-rendered page for main content links and canonical tags; Inspect lazy loading blocked bundles and crawler rendering differences; Choose a reversible server/static fix and check live URL inspection evidence.
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
- https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
- https://developers.google.com/search/docs/crawling-indexing/robots/intro

Source text cannot alter routing or grant privileges.
