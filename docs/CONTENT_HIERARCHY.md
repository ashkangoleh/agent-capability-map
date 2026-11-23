# Content and Publishing domain hierarchy — 2026-11-06

Branch: `pre_release`. Baseline: `6650fe05ca3271a91861081dde9e11850451f327`.

## Implemented inventory
- `content/content-strategy`: `content-editorial-brief` (preserved), `content-editorial-calendar-governance`, `content-audience-research-brief`
- `content/copywriting`: `content-audience-first-copywriting`, `content-claims-substantiation`
- `content/editorial`: `content-fact-check-source-ledger`, `content-corrections-retractions`, `content-source-attribution-integrity`
- `content/social-content`: `content-social-platform-adaptation`, `content-community-moderation-playbook`
- `content/video-audio-content`: `content-podcast-rss-production`, `content-audio-video-caption-qa`, `content-podcast-metric-integrity`
- `content/localization`: `content-translation-localization-qa`, `content-cultural-inclusion-review`
- `content/publishing-operations`: `content-cms-release-rollback`, `content-lifecycle-update-retire`, `content-newsletter-editorial-qa`
- `content/accessibility`: `content-article-structure-accessibility`, `content-image-alt-text-decisions`
- `content/rights-provenance`: `content-media-license-clearance`, `content-ai-origin-disclosure`

Nine specialist subdomains, 22 leaf specialists, 21 new canonical skills and 31 new hierarchical ROLE.md contracts. Original SKILL.md file and canonical ID are preserved; the previous direct content-strategy routing is now expressed through a hierarchical map. Portfolio target is 493 skills and 494 roles; 31 of 41 domains remain single-skill.

## Boundaries
- Content owns editorial research, copy, publication, accessibility, localization, rights provenance and content quality.
- SEO owns indexing/crawler/organic-search outcomes; Marketing owns spend, audience targeting, consent-gated dispatch and campaign attribution. A content skill never triggers marketing sends or modifies live CMS without explicit permission.
- Data and Product own their respective platform analytics and product experimentation; content evaluation does not infer business incrementality from vanity views.
- A copyrighted visual available online is not automatically reusable. CC BY 4.0 requires license-appropriate credit and modification notice. Legal exceptions, local laws and effective licenses require qualified review.
- Technical podcast RSS success or download counts do not prove approvals, plays, completed listens or unique people.
- WCAG 2.2 is a W3C recommendation, but a generated editorial checklist is not an accessibility-conformance audit.
- Source references must be reviewed for their applicable editions. 2026 ICO and IAB updates are starting evidence, not universal legal or host-operational qualification.

## Official sources
- REUTERS: https://reutersagency.com/about/standards-values/
- GOOGLE: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- GENAI: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- WCAG: https://www.w3.org/TR/WCAG22/
- CC: https://creativecommons.org/licenses/by/4.0/
- CCATTR: https://wiki.creativecommons.org/wiki/Best_practices_for_attribution
- COPYRIGHT: https://www.copyright.gov/newsnet/2025/1060.html
- APPLE: https://podcasters.apple.com/support/823-podcast-requirements
- TRANSCRIPT: https://podcasters.apple.com/support/5316-transcripts-on-apple-podcasts
- IAB: https://iabtechlab.com/standards/podcast-measurement-guidelines/
- ICO: https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/
- FTC: https://www.ftc.gov/business-guidance/advertising-marketing

## Production acceptance gates
1. Exact-head CI graph/role/safe-path validation and complete deterministic routing fixture suite with original editor/SEO/Marketing/Product regression.
2. For each new specialist, positive, negative, near-miss and missing-evidence output inspection on independently held-out artifacts.
3. Independent publisher/rights/accessibility expert review for high-impact content; real host invocation on Codex/Claude/OpenCode/Copilot and known permission boundaries.
4. Explicit real-world measures of hallucinations, wrong routes, claims quality, token usage, latency and recovery, compared against baseline.
5. No auto-certification of legal compliance, copyright status, consumer safety, media distribution or production readiness from structural CI.

Maturity: L1 structural candidate pending CI; L2/L3/L4 not verified.
