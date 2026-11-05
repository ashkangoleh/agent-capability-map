# Domain role contracts — design backlog (not implemented)

**Status:** DESIGN BACKLOG ONLY — user requested on 2026-11-05. No roles are enabled by this file.
**Branch:** `pre_release`.
**Scope:** all currently published top-level domains, one reviewed domain at a time.

## Problem / explicit design intent

A domain role should improve *how the selected skill's output is reviewed and structured* without changing the authoritative deterministic domain/skill selection. A role is an execution-time advisory contract, **not a second router**, a permission grant, a global character persona, a new user prompt-injection surface, or an excuse to read all skills.

## Proposed progressive-loading execution order

1. **Bootstrap**: read only the small global instructions; resolve user-selected domain scopes (at most five non-overlapping scopes).
2. **Deterministic router**: discover the authorized domain/subdomain/skill; return validated route, source and `skill_path`. An unmatched or `domain_not_enabled` request must stop before any domain role loads.
3. **Role contract (FUTURE, conditional)**: only after an authorized, matched domain, load a small versioned `domains/<domain>/ROLE.md` (or explicit YAML-registered path). Child-category role overrides, if ever needed, must be explicitly registered and inheritance rules reviewed; never scan sibling domains.
4. **Selected SKILL.md**: load only the matched skill and required references. Role may influence evaluation rubric, deliverables, terminology and challenge questions but must not override skill activation/exclusion, user instructions, safety/security policy, permissions or confirmed facts.
5. **Output evaluation**: role-specific reviewer checks assertions, assumptions, operational risks, evidence provenance, testability and constraints. Report missing evidence as unknown, not as a passed verification. Measure quality and tokens before general rollout.

## Contract schema proposal (draft, not active)

- `id`: stable domain ID; `version`: explicit contract version; `role_title`: short discipline-relevant reviewer identity (not model-authority escalation)
- `responsibility_boundaries`: in/out domain ownership and escalation to another domain
- `decision_principles`: simplest production-safe approach; cost and operability over hype
- `required_inputs`: environment/version/constraints; ask only one essential question if blocked
- `output_contract`: reproducible artifacts, checks and uncertainty labels
- `review_gates`: correctness, security, rollback, performance/cost, and cited/current evidence where needed
- `failure_modes`: known bad advice patterns to reject
- `token_budget`: measured maximum added prompt footprint, with opt-out
- `evaluation_cases`: blind positive/negative/ambiguous cases with expected improvements

**Infrastructure candidate role (PROPOSED only):** `Principal Infrastructure Reliability & Platform Architect`. Require environment/version assumptions, availability and failure-domain analysis, blast radius, rollback/recovery, observability, least privilege, operational ownership and staged acceptance tests. Prefer native simpler services unless a more complex control plane is justified.

**Data candidate role (PROPOSED only):** `Principal Data Platform & Reliability Architect`. Require data correctness/grain, schema evolution, replay/backfill, idempotency, reconciliation, SLO/latency, cost and observability. Do not assume `Data Engineering` covers all `Data Science` review needs; test nested role composition before adopting.

Do not preassign generic titles to all 41 domains. Co-design each role with its domain's ownership, benchmark it against current no-role output and review in the same one-domain-at-a-time process.

## Compatibility, security and validation gates

- Reject nested scope/role conflicts, unknown role files, duplicate IDs, path traversal, symlinks and unauthorized profile changes.
- Ensure a role does not turn a blocked domain into an enabled one, alter the matched skill path, or perform unapproved commands.
- Protect from lower-trust skill/reference instructions pretending to change role authority.
- Use deterministic regression suites and blinded task evaluation: measure factual error, false positives/negative routing, omissions, token overhead, latency and useful artifacts on matched vs unmatched tasks.
- Test on **actual** Codex, Claude Code, OpenCode, Copilot and Cursor versions. Native discovery cannot be assumed to honor the Python domain allowlist.
- Keep the default behavior **no role loading** until a separately reviewed ADR/RFC, pinned acceptance test and user approval. Avoid unmeasured global prompt expansion and role stacking.

## Future deliverables

A short cross-domain role interface/RFC, one Infrastructure pilot `ROLE.md`, A/B evaluation against existing skill results, versioned and reversible opt-in loader with negative tests; only then replicate to other selected domains with user consent.

## References inside the repository

- `AGENTS.md` — global minimal bootstrap contract.
- `docs/DOMAIN_SELECTION.md` — allowlist and maximum-five non-overlapping scopes.
- `docs/HOST_COMPATIBILITY_ACCEPTANCE.md` — host boundaries and explicit router.
- `docs/INFRASTRUCTURE_COVERAGE_AUDIT.md` — infrastructure procedure-quality gaps.
