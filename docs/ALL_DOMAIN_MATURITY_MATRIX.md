# All-domain evidence coverage and maturity — 2026-11-06

Baseline commit: `5e29a873122fdb13d377ba855b0227e374eb259c`; updated Marketing registry on `pre_release` (new count requires exact-head CI audit).

## Executive result

- 41 top-level domains, 453 canonical `SKILL.md` packages and 432 hierarchical `ROLE.md` files.
- All 453 packages have a linked `references/acceptance-and-recovery.md` companion (L1 **structural coverage**, not runtime proof).
- **32 of 41 domains have only one skill**. These must not be presented as domain-complete taxonomies.
- 76 cross-domain verification policy profiles exist. Some are reused: they are not 453 independently trialed runbooks.
- 453 skill profiles **do not** have a verified real-host A/B study; latest-release correctness and safety qualifications remain unverified as a portfolio.
- For Data Engineering, specialized validation was extended to all 123 skills but only a few packages have standalone offline scripts and examples.
- Structural CI result for previous revision `5e29a873122fdb13d377ba855b0227e374eb259c`: 5/5 jobs passed, 271 unit tests (one skipped). Re-run for changes to this document or source policy.

## Domain-by-domain L1 evidence inventory

| Domain | Skills | Referenced | Taxonomy maturity | L2 / L3 / L4 status |
|---|---:|---:|---|---|
| `aerospace` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `agent-systems` | 2 | 2 | Narrow | Not comprehensively verified |
| `agriculture` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `ai-ml` | 61 | 61 | Large; specialist depth still uneven | Not comprehensively verified |
| `business` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `construction` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `content` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `customer-experience` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `data` | 186 | 186 | Large; specialist depth still uneven | Not comprehensively verified |
| `design` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `ecommerce` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `education` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `energy` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `environment` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `finance` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `gaming` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `health` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `humanities` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `infrastructure` | 95 | 95 | Large; specialist depth still uneven | Not comprehensively verified |
| `legal` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `logistics` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `manufacturing` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `marketing` | 17 | 17 | Seven specialist subdomains; L1 structural, not runtime validated | Not comprehensively verified |
| `media` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `nonprofit` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `people` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `personal` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `product` | 3 | 3 | Narrow | Not comprehensively verified |
| `public-sector` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `real-estate` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `research` | 2 | 2 | Narrow | Not comprehensively verified |
| `robotics` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `sales` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `science` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `security` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `seo` | 3 | 3 | Narrow | Not comprehensively verified |
| `social-sciences` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `software-engineering` | 52 | 52 | Large; specialist depth still uneven | Not comprehensively verified |
| `sports` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `telecommunications` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |
| `travel` | 1 | 1 | Seed-only — major breadth gap | Not comprehensively verified |

## Prioritized implementation work

**P0, breadth gap:** all 32 seed-only domains. Require expert taxonomy review, independently grounded specialization and role inheritance before adding skills. Do not auto-generate 20 shallow skills per domain.

**P1, specialist depth:** Data (186), Infrastructure (95), AI/ML (61), Software Engineering (52). Validate runtime/version APIs, task-specific failure matrices, real adverse scenarios and tool/client compatibility before declaring readiness.

**P2, cross-domain boundary:** Marketing / SEO / Product / Research / Agent Systems and each other small domain. Create held-out near-miss and cross-domain prompts to measure over-routing and abstention.

**P3, production qualification:** high-stakes domains (Health, Legal, Finance, Construction, Aerospace, Energy, Security) must receive competent subject-matter review; a generic AI skill cannot self-certify safety or regulatory correctness.

## Official reference governance

See [Source provenance policy](SOURCE_PROVENANCE_POLICY.md). Confirm applicability and published version before claiming any result. This is not a list of 453 freshly verified, version-pinned external sources.

## Next quality evidence

- For each skill, independently freeze a representative task, input artifact, expected outcome and negative/ambiguous scenario.
- Add high-value version-appropriate implementation/examples only when the capability genuinely requires them.
- Run on actual supported agent hosts; record selected skills, loaded files, task correctness, safety failures, execution cost and p95 latency.
- Keep original `SKILL.md` and routing IDs stable unless a reviewed migration explicitly changes ownership.
