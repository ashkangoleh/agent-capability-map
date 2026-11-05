# Domain roles — implemented contracts and open evaluation gates

**Status:** All 41 currently registered top-level domains have a versioned role contract. The resolver returns a domain-specific `role_path` only for authorized matched master skills. Real-host execution and measurable output uplift remain unverified.

## Implementation

- Canonical role file: `domains/<domain-id>/ROLE.md`. This is an advisory reviewer contract, **not** a routable Agent Skill, an additional LLM, a new permission level or a second router.
- The deterministic resolver first applies the existing user-scoped allowlist (maximum five non-overlapping roots), then selects one master skill. Only a `matched` master result includes `role_path` beside the unchanged `skill_path`.
- `role_path` is absent for `unmatched`, `unavailable`, `needs_clarification`, `domain_not_enabled` and project/personal overlay selections.
- `role_contract_path` validates the top-level domain ID and exact path, rejects role-file and parent-directory symlinks, limits to 4096 bytes, checks UTF-8 and unique YAML frontmatter with `role_id` / `version` / `title`, and requires six review sections.
- `Router.validate()` verifies all 41 active top-level roles. `AGENTS.md` and installers now tell hosts to read only the matched role and selected skill. Other roles are never advertised on each request.
- Role text can improve review questions, assumptions and output structure, but cannot re-route the skill, grant permissions, invent evidence, change user approvals or override the safety/security policy. Python validation is a path/schema check, **not** an LLM prompt-injection sandbox.

## One-role-per-domain contract

Each `ROLE.md` contains a concise, distinct decision lens, domain-specific evidence needs, review gates, failure/rejection criteria, and output contract. Domains remain separate: the Data domain role does not claim to subsume Data Science, and the Security domain role does not grant authorization for offensive activity.

## Maturity and acceptance

- **41/41 roles present and validated:** repository completeness, not a measured quality score.
- **Resolver and host instruction integration:** implemented; no native host API changes.
- **Host runtime tests:** NOT VERIFIED on Codex, Claude Code, OpenCode, GitHub Copilot or Cursor. Actual file reads and allowlist enforcement must be observed on pinned versions.
- **Quality improvement:** NOT VERIFIED. Run blinded A/B evaluations with and without each role, measuring task correctness, unsafe/incomplete advice, false claims, omissions, response length and token/latency overhead.
- **Infrastructure pilot:** fault recovery, Kubernetes operator migration, IAM boundaries and DR exercise scenarios. A role should be revised or disabled if its extra context harms correctness.
- **Maintenance:** add a new role whenever a top-level domain is registered; `Router.validate()` must fail without it. No subdomain role stacking without an explicit evaluated design.

## Official reference basis

- https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- https://learn.chatgpt.com/docs/build-skills
- https://support.claude.com/en/articles/12512176-what-are-skills
