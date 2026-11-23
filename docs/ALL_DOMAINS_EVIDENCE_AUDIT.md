# Cross-domain evidence contracts — 2026-11-06

**Working branch:** `pre_release`. **Scope:** all 41 currently registered top-level domains and all 438 canonical skill packages.

## What was done

- **315 previously unaugmented skills** received an on-demand `references/acceptance-and-recovery.md`, linked from their existing `SKILL.md`. The earlier **123 Data Engineering** references were preserved. Every existing skill now has a package-local review resource; no new skill ID or routing key was introduced.
- Added `catalog/cross-domain-verification-profiles.json`: **41 domain review profiles** plus **35 family overrides** (AI/ML, Infrastructure, Software Engineering, Data and adjacent areas). These define an adversarial case, independent acceptance oracle and stop/escalation condition. Skill-specific inputs, procedures, failure notes and source links were retained from each original skill.
- Preserved original main skill procedures rather than replacing them with generic new steps. The reference is lazy-loaded and is **not** an executable script, permission token or real-world test result.
- Added a complete structural audit `scripts/audit_all_skill_evidence.py` and its unit tests. This audit verifies the master skill inventory, per-skill reference, metadata, domain ownership, content size, link/path integrity and explicit limits on quality claims.

## Current coverage and material gaps

| Metric | Observed structural inventory | Qualification |
|---|---:|---|
| Top-level domains | 41 | Entire existing catalog; root-only domains have not been expanded |
| Canonical skill packages | 438 | No new skills added |
| Independently linked review references | 438 | Structural L1; not a witnessed test |
| Previous Data Engineering references | 123 | Preserved |
| New cross-domain references | 315 | Generated with domain/family-specific challenge and original procedure fragments |
| Domain/family evaluation policies | 41 + 35 | Repeatable review templates; not standalone certifications |
| Production integration tests across all domains | NOT VERIFIED | Separate L3 evidence required |
| Human or agent-host quality A/B for all domains | NOT VERIFIED | Separate L4 evidence required |

**Important limitation:** these are editorially structured, profile-derived review guides. They do not constitute 315 separately hand-validated, up-to-date vendor runbooks. Domain coverage is also not equivalent to full subdomain taxonomy coverage.

## Required next passes

**L2:** Verify each skill's version-specific official source, actual API/schema/tool compatibility, runnable example (where appropriate), and domain-qualified correctness. Reject unsupported or obsolete feature claims.

**L3:** Run safe integration, adversarial and failure/recovery tests on authorized representative systems. For legal/health/science/design tasks, use domain-qualified source review and independent verification, not fake infrastructure chaos tests.

**L4:** Conduct blinded task-output A/B on the supported agent hosts with held-out multilingual user tasks and measurable correctness, cost, latency, unsafe-action and abstention rates.

**Release policy:** `CI PASS` proves packaging, routing and static contracts only. Any stronger claim must link a date-stamped experiment and a qualified reviewer.

## Primary current sources (independently checked 2026-11-06)

- [Agent Skills specification](https://agentskills.io/specification) — relative on-demand references, resource structure and skill frontmatter rules.
- [OWASP Top 10:2025](https://top10.owasp.org/2025/) — current web application risk awareness list.
- [OWASP GenAI LLM Top 10:2026](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/tree/main/2026/final) — prompt injection, agency, privacy, model/data poisoning and other current GenAI risks.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) — revision ongoing in 2026; do not treat the currently available 1.0 as a new 2026 final standard.
- [Google SRE workbook](https://sre.google/workbook/alerting-on-slos/) — alerting on customer-impacting SLOs and error budgets.
- [Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) — evidence and people-first SEO guidance; no ranking guarantee.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — lifecycle and engineering verification practice.

All other links in the 438 original skills were **inherited, not independently revalidated**. They must be checked against an actual deployed version, current standard edition and jurisdiction before technical or regulated advice.
