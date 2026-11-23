# seo-indexability-diagnostics: specialist evaluation and negative controls

Domain `seo/technical-seo`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Classify the reported issue: discovered, fetched, rendered, indexed or selected canonical. Do not equate crawl success with indexing.
2. Inspect representative final URLs for HTTP status, robots.txt access, meta robots/X-Robots-Tag, redirects, canonical hint, hreflang, internal links and sitemap inclusion.
3. Separate declared canonical from Google's selected canonical; Google can ignore hints, and repeated sitemap submission cannot force indexing.
4. Review logs or trustworthy crawl samples and Search Console URL Inspection/Page Indexing reports. Avoid drawing sitewide conclusions from a single URL.

## Challenge / acceptance
- **Challenge:** Change canonical, robots, rendering or locale with a controlled URL set. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Crawlability, indexability, structured data and measurable impressions are distinguished. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No ranking, indexation or rich-result guarantee. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://developers.google.com/search/docs/crawling-indexing
- https://developers.google.com/search/docs/crawling-indexing/canonicalization
- https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
