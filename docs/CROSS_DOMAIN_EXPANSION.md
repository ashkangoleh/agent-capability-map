# Cross-Domain Skill Expansion

## Verified structural state

The expansion introduces 29 specialist SKILL.md files: 21 for previously mapped top-level domains and 8 for newly introduced domains. All 41 top-level domains now have at least one active specialist, while many of their individual subdomains are still mapped-only. The legacy 30 active skills remain unchanged.

New specialist domains: security, people, education, finance, legal, health, science, ecommerce, sales, customer-experience, media, gaming, manufacturing, logistics, construction, energy, agriculture, public-sector, travel, sports and personal.

Newly introduced domains with one active skill each: robotics, telecommunications, aerospace, social-sciences, humanities, environment, real-estate and nonprofit.

## Design constraints

- Each active skill contains task boundary, required inputs, domain-specific procedure, evidence expectations, abstention rules and starting references.
- Legal, finance and health skills perform bounded research and evidence synthesis; they must not replace authorized professional advice.
- New domains are mapped-only until domain-specific skills and behavioral evaluations exist.
- Typed graph and personal/project overlays remain unchanged; existing master skill IDs are not overwritten.
- A matching YAML fixture proves **deterministic lexical routing only**. It does not prove semantic accuracy, actual source currency, client integration, lower token usage or safe execution.
- Sources are *starting references*. For any version-sensitive or regulated claim, verify primary sources and jurisdiction/edition/date at task execution.

## QA gates

1. Validate the entire YAML graph and master skill-ID index.
2. Run positive routing tests for each new specialist.
3. Run unavailable tests for mapped-only domains.
4. Add domain-specific negative and mixed-language cases before promoting broad production-readiness.
5. Evaluate real agent outputs for reliability, source fidelity, safety, and measured token usage; record model and client versions.

### Audit issue

The existing router uses deterministic trigger-string matching and cannot infer all user intents across languages. Adding thousands of domain aliases without contextual semantics will increase false activations and ambiguity. The right long-term solution is a calibrated candidate selector with deterministic path validation and clear abstention, not loading all skills or making ungrounded 'complete coverage' claims.

## Newly activated domain packages

| Domain | Active specialist | Standards / primary evidence |
|---|---|---|
| robotics | `robotics-ros2-interface-review` | ROS 2 QoS documentation |
| telecommunications | `telecom-network-change-review` | 3GPP, ITU-T |
| aerospace | `aerospace-requirements-traceability` | NASA Systems Engineering Handbook |
| social-sciences | `social-science-survey-quality` | AAPOR survey standards |
| humanities | `humanities-primary-source-critique` | Library of Congress source interpretation |
| environment | `biodiversity-observation-quality` | GBIF data quality |
| real-estate | `real-estate-due-diligence` | RICS valuation standards |
| nonprofit | `nonprofit-grant-evidence-plan` | Grants.gov eligibility and documentation |

These are narrow specialist procedures, not a claim to full-domain expertise or legal, clinical, flight, financial, or engineering certification.
