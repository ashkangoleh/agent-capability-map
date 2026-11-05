# Software Engineering — hierarchical capability and role coverage

**Branch:** `pre_release`. **Scope:** Software Engineering only. **Baseline before this change:** 1 general skill, 1 flat domain map, 1 root role, 6 active branches sharing one registry and mobile development mapped/unavailable.

## Target and implementation

The taxonomy organizes the 18 knowledge areas of **IEEE SWEBOK v4.0a** into 15 pragmatic, nonoverlapping routed workstreams. The mapping is **not** one-to-one: for instance Software Construction is divided into backend/frontend/mobile/language concerns, while Software Testing and Software Quality are treated together, and Software Operations remain application-focused rather than duplicating Infrastructure ownership.

| Domain subdomain | Specialized capabilities |
|---|---:|
| `backend` | 4 |
| `developer-tools` | 3 |
| `engineering-process` | 3 |
| `foundations` | 3 |
| `frontend` | 4 |
| `maintenance-evolution` | 3 |
| `mobile-development` | 4 |
| `performance-engineering` | 3 |
| `programming-languages` | 5 |
| `quality-testing` | 4 |
| `release-operations` | 3 |
| `requirements-engineering` | 3 |
| `software-architecture` | 4 |
| `software-design` | 3 |
| `software-security` | 3 |
| **Total** | **52** |

The root `software-engineering` has 15 first-level specialist roles and 52 leaf roles, **68 total role contracts** including the existing root. Each leaf is a deterministic, terminal skill registry with exactly one active skill, avoiding ambiguous multi-registry search. **51 new specialized skills** have been added while the original `software-engineering-implementation` ID, canonical file path, content and legacy registry remain unchanged. Mobile Development is now active with Android, iOS, cross-platform and release workflows.

## Expected resolver behavior

```text
catalog/root.yaml
  → domains/software-engineering/map.yaml
    → domains/software-engineering/<subdomain>/map.yaml
      → domains/software-engineering/<subdomain>/<capability>/skills.yaml
        → .agents/skills/software-engineering/<subdomain>/<capability>/<skill>/SKILL.md
```

`role_paths` returns the owning root, subdomain and capability roles, in that order. The existing legacy implementation skill remains at its canonical `core/software-engineering-implementation/SKILL.md` location; its new leaf registry points there without duplication or renaming.

User-selected domain scopes, maximum-five nonoverlapping selections, trusted project/personal overlays and `needs_clarification` remain unchanged. Unmatched or disabled routes load no domain role. New skills do not grant tool privileges.

## Gates and evidence

- 52 deterministic positive routing fixtures, one per capability, plus retained near-miss API/SEO routing case and regression checks for data/domain allowlist.
- Graph validation requires unique active skills, index-to-registry parity, exact role paths, no orphan skill manifest and no duplicate skill id.
- Standalone Linux/Windows packages must be rebuilt so the new roles and skill files are included, and executable/allowlist smoke must pass for both platforms.
- **Not yet evidence of specialist depth:** structural coverage is separate from successful evaluation against real projects and latest framework versions. A/B quality checks, honest error rates and host-specific actual skill loading are still necessary.
- Guard against sweeping overlap with Infrastructure (clusters, OS, IaC) and Security (organization-wide threat/governance controls). Software Engineering remains code/application owner.

## Official references

- IEEE Software Engineering Body of Knowledge v4.0a (Sept 2025): https://www.computer.org/education/bodies-of-knowledge/software-engineering
- SWEBOK 18 knowledge area contents: https://www.computer.org/education/bodies-of-knowledge/software-engineering/topics
- Open Agent Skills specification: https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- OWASP Application Security Verification Standard 5.0.0: https://asvs.owasp.org/
