# Research and Communication hierarchy — 2026-11-06

Target branch: `pre_release`. Baseline: `46d995b209a824ec9080d1a0c0fcc1b988fb2f4e`.

## Active route inventory
- `research/evidence-research`: `evidence-research` (preserved), `research-primary-source-triangulation`, `research-conflicting-evidence-adjudication`, `research-claim-to-source-traceability`
- `research/academic-research`: `research-systematic-review-reporting`, `research-scholarly-doi-metadata-integrity`, `research-protocol-reproducibility-review`
- `research/technical-writing`: `technical-writing-docs` (preserved), `research-api-reference-documentation`, `research-operational-runbook-recovery`, `research-documentation-version-qa`
- `research/decision-documents`: `research-rfc-proposal-tradeoff-review`, `research-adr-decision-traceability`
- `research/editing-translation`: `research-technical-translation-fidelity`, `research-technical-copyedit-precision`
- `research/presentation-reports`: `research-executive-evidence-brief`, `research-visual-claim-integrity`, `research-technical-presentation-evidence`
- `research/research-integrity`: `research-contributor-credit-coi`, `research-ai-generated-citation-audit`
- `research/knowledge-transfer`: `research-knowledge-base-source-curation`, `research-handoff-reproducible-findings`

8 first-level specialist subdomains; 22 total active leaf skills, 20 newly created, 2 original immutable skills; 30 new independent hierarchical ROLE.md contracts. Total repository inventory expected: 513 canonical skills, 524 roles; 31 of 41 top-level domains still have one seed skill.

## Evidence and authority boundaries
- Research owns evidence provenance, academic reporting protocols, documentation accuracy and communication of uncertainty.
- Data Science owns statistical modeling, experimental inference and computational analysis implementations; Research does not assert significance from an unavailable dataset.
- Software Engineering owns executable code, API design and delivery; Research documents verified behavior but does not invent endpoints.
- Content owns editorial publishing workflows and media rights; Research owns fact verification and knowledge transfer, not publishing rights.
- An ADR records a decision and its evidence; an RFC solicits review and must not be presented as adopted without approval.
- PRISMA 2020 is a reporting guideline for systematic reviews, not generic certification that a study is rigorous. CRediT roles describe contributions, not formal authorship entitlement. BCP 14 uppercase requirement words carry specialized interpretation only when explicitly applied.
- Bibliographic metadata, DOI existence, search snippets and AI output alone never demonstrate a source supports an attached claim.

## Primary authoritative starting references
- Google: https://developers.google.com/tech-writing/overview
- Style: https://developers.google.com/style
- Inclusive: https://developers.google.com/style/inclusive-documentation
- PRISMA: https://www.prisma-statement.org/prisma-2020
- EQUATOR: https://equator-network.org/reporting-guidelines/
- Crossref: https://www.crossref.org/documentation/retrieve-metadata/rest-api
- RFC: https://www.rfc-editor.org/info/rfc7322/
- RFC8174: https://www.rfc-editor.org/info/rfc8174/
- NISO: https://credit.niso.org/contributor-roles/
- NIST: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- W3C: https://www.w3.org/WAI/standards-guidelines/wcag/

Source versions, release/effective dates and context must be revalidated for each high-impact task.

## Acceptance gates
1. Verify registry graph, 22 leaf paths, 30 roles, canonical index and both original SKILL.md blob hashes unchanged against baseline commit.
2. Route all 20 new specialist positive fixtures and old research, developer documentation, product, content and SEO regressions.
3. Verify user-selected domain scope deny, untrusted data behavior and no privilege escalation.
4. Evaluate separate blinded expert tasks with negative and near-miss claims, actual source inspection, abstention and citation integrity; check token cost and host compatibility.
5. Do not call structural CI a validation of research methods or production quality. L2/L3/L4 remain unverified.
