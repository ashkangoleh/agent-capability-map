# Reference provenance and skill maturity — policy (2026-11-06)

## Source-of-truth rules

1. Resolve the **actual** runtime/version, locality/jurisdiction, operating mode, scope, model/connector and intended use before interpreting references. An online newest guide is not evidence of deployed behavior.
2. Prefer the standards owner, vendor/maintainer documentation for the exact release, published specification and official changelog. Use systematic reviews/primary empirical data when the domain is empirical. Secondary discussion cannot override an applicable primary source.
3. Record for each material assertion: claim, source URL/ID, publisher, specification/release version, effective date or timestamp, date accessed, applicability and independent verification status.
4. Explicitly distinguish `stable`, `draft/nightly`, `deprecated`, `superseded`, `jurisdiction_specific` and `unknown`. Disallow auto-promoting an unversioned source or a draft to production normative authority.
5. For high-stakes claims (health, legal, finance, aerospace, construction, energy, security, privacy) require qualified human review, current jurisdiction or standards, and explicit escalation when unsupported. References do not grant access or authorize physical/financial actions.
6. Preserve a frozen negative/regression task suite and independent outcome oracle. Model self-assessment and structural CI are not validation of results.
7. Sources can expire: re-check on dependency upgrade, production incident, rule amendment, CVE, changing platform API or scheduled maintenance. Review cadence must follow risk and change frequency; do not invent a universal 30-day guarantee.
8. The source URLs below are **framework starting points**, not an exhaustive mapping to all 438 skills or an assertion that each was version-checked.

## Verified authoritative framework starting points

| Scope | Owner, version and status | Reference |
|---|---|---|
| Portable skill packages | Agent Skills open specification, consult current normative version | https://agentskills.io/specification |
| AI governance | NIST AI RMF 1.0, 2026 revision ongoing; Playbook is guidance, not mandatory procedure | https://www.nist.gov/itl/ai-risk-management-framework |
| Security governance | NIST CSF 2.0, published 2024-02-26 | https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20 |
| Web/application security | OWASP ASVS v5.0.0 stable, published 2025-05-30 (bleeding-edge not stable) | https://asvs.owasp.org/ |
| Web accessibility | W3C WCAG 2.2 Recommendation, 2024-12-12 revision | https://www.w3.org/TR/2024/REC-WCAG22-20241212/ |
| SRE service reliability | Google SRE Workbook Implementing SLOs; use service-specific SLI and error-budget policy | https://sre.google/workbook/implementing-slos/ |

These references are **not interchangeable**. E.g. security ASVS does not validate a clinical treatment, WCAG does not verify a physical aircraft, and NIST AI RMF does not provide a versioned inference API. Every skill still requires its own source and deployment/subject-specific evidence.

## Maturity states

- `L0`: registered and routable specialist.
- `L1`: source-aware, linked, task-relevant evaluation/negative-control plan; static CI checks only.
- `L2`: release/jurisdiction-pinned correctness, reviewed executable example or advisory rubric, independent offline reproduction.
- `L3`: real authorized system test or qualified field validation with observed recovery, adverse cases and permission boundaries.
- `L4`: blinded external-agent A/B showing task success versus baseline, false claims, harm, cost and latency with uncertainty.

**No domain should be declared complete at L1.** A domain with one skill is only a minimal placeholder and usually lacks the breadth needed for expert coverage.
