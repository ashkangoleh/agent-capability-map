# Domain roles — implemented contracts and open evaluation gates

**Status:** All 41 currently registered top-level domains have a versioned role contract. The resolver returns a domain-specific `role_path` only for authorized matched master skills. Real-host execution and measurable output uplift remain unverified.

## Implementation

- Canonical role file: `domains/<domain-id>/ROLE.md`. This is an advisory reviewer contract, **not** a routable Agent Skill, an additional LLM, a new permission level or a second router.
- The deterministic resolver first applies the existing user-scoped allowlist (maximum five non-overlapping roots), then selects one master skill. Only a `matched` master result includes `role_path` beside the unchanged `skill_path`.
- `role_path` is absent for `unmatched`, `unavailable`, `needs_clarification`, `domain_not_enabled` and project/personal overlay selections.
- `role_contract_path` validates the top-level domain ID and exact path, rejects role-file and parent-directory symlinks, limits to 4096 bytes, checks UTF-8 and unique YAML frontmatter with `role_id` / `version` / `title`, and requires six review sections.
- `Router.validate()` verifies all 41 active top-level roles. `AGENTS.md` and installers now tell hosts to read only the matched role and selected skill. Other roles are never advertised on each request.
- Role text can improve review questions, assumptions and output structure, but cannot re-route the skill, grant permissions, invent evidence, change user approvals or override the safety/security policy. Python validation is a path/schema check, **not** an LLM prompt-injection sandbox.

## Hierarchical role inheritance (Data pilot: 2026-11-05)

- A `ROLE.md` may be declared at any **existing logical route**: `domains/data/ROLE.md` → `domains/data/data-engineering/ROLE.md` → `domains/data/data-engineering/distributed-processing/ROLE.md` → `domains/data/data-engineering/distributed-processing/spark/ROLE.md` → `domains/data/data-engineering/distributed-processing/spark/pyspark/ROLE.md`.
- The resolver returns `role_paths` ordered **parent to child** for authorized matched master results only; the historical `role_path` remains a top-level alias for backward compatibility.
- Role paths are derived only from the **selected verified route**, never by guessing directory layouts or scanning unrelated domains. Absent deep roles inherit the nearest defined ancestor; an invalid present role fails closed.
- Individual role files max 4096 bytes; the complete selected chain max **8192 bytes and 8 roles**. No silent truncation; overly verbose roles are a validation failure and must be consolidated.
- The semantic responsibilities are layered: parent provides general principles, more-specific role provides specialized evaluation criteria, while the selected SKILL.md remains the procedural authority. A role never grants permissions, modifies the deterministic route or authorizes external actions.
- **Data domain:** 127/127 active logical graph nodes now have distinct ROLE.md files, including the root Data role, nine first-level subdomains, all Data Engineering and Data Science capabilities, and nested Lakehouse/SQL, Spark, Kafka, Airflow, dbt and relational DB routes. The dynamic test walks all 21 reachable Data map files, verifies exact route-to-role ownership, detects missing and orphan contracts, and rejects future nodes without roles. **Infrastructure** now has 97/97 roles across 22 maps (16 first-level scopes, 96 non-root active nodes) with a separate dynamic inventory test. The remaining **37** domains still only have root roles; hierarchical role coverage across all 41 is NOT complete.
- Unit tests enforce selected role order, file safety, match-only availability, profile isolation and overall context bounds. Native host execution / output-quality uplift are still not measured.

## One-role-per-domain contract

Each `ROLE.md` contains a concise, distinct decision lens, domain-specific evidence needs, review gates, failure/rejection criteria, and output contract. Domains remain separate: the Data domain role does not claim to subsume Data Science, and the Security domain role does not grant authorization for offensive activity.

## Maturity and acceptance

- **41/41 roles present and validated:** repository completeness, not a measured quality score.
- **Resolver and host instruction integration:** implemented; no native host API changes.
- **Host runtime tests:** NOT VERIFIED on Codex, Claude Code, OpenCode, GitHub Copilot or Cursor. Actual file reads and allowlist enforcement must be observed on pinned versions.
- **Quality improvement:** NOT VERIFIED. Run blinded A/B evaluations with and without each role, measuring task correctness, unsafe/incomplete advice, false claims, omissions, response length and token/latency overhead.
- **Infrastructure role coverage:** 97/97 graph nodes (structural only); review A/B outputs for fault recovery, Kubernetes operator migration, IAM boundaries, networking and DR. A role should be revised or disabled if its extra context harms correctness.
- **Maintenance:** new active Data or Infrastructure graph nodes require matching role contracts in CI. Parent-to-child role inheritance is bounded at 8 files/8192 bytes. Do not add other domains' nested roles without a domain review and tests.

## Official reference basis

- https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- https://learn.chatgpt.com/docs/build-skills
- https://support.claude.com/en/articles/12512176-what-are-skills

## Software Engineering specialist role rollout — 2026-11-05

- 15 active first-level Software Engineering domains, each with a role; 52 terminal capability nodes, each with a leaf role. Root + 15 + 52 = **68 roles**.
- 51 additional specialist SKILL.md packages and 52 one-skill terminal registries (one still points to the unchanged legacy skill).
- 52 positive route fixtures + dynamic graph/role/source inventory tests. No change to Data/Infrastructure routing contracts or five-scope allowlist.
- Other **37** top-level domains still have only one root role. This structure is not proof of response quality: execute blinded task-level evaluation and real host read checks before production signoff.

## AI/ML specialist role rollout — 2026-11-05

- 12 first-level areas and 66 active terminal capability routes, each with an independent role contract: root + 12 + 66 = **79 AI/ML role contracts**.
- 43 new specialist SKILL.md packages; existing skill IDs, package content and legacy registry locations are preserved. Legacy skill IDs may be referenced by multiple terminal routes only when their canonical source path is identical; newly added specialist skill IDs are unique. The mapped ML validation route remains unavailable and is not counted as active.
- Across the repository this results in **438 active skill packages** and **408 role contracts**. Remaining top-level domains with root-only role guidance: **37**.
- New deterministic fixtures, graph ownership tests, and negative cross-domain/scoped tests are in `tests/test_ai_ml_coverage.py`. Structural pass does not prove useful outputs, host integration or release qualification; use commit-pinned CI and blinded A/B evaluations.
