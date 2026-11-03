# Client compatibility and installation boundary

Canonical files live under .agents/skills/<id>/SKILL.md. Each skill is self-contained and follows the portable Agent Skills frontmatter contract. The domain registry and parent_skill/related_skills fields are **project conventions**, not portable standard fields.

| Client | Supported approach | Important limitation |
| --- | --- | --- |
| Codex | Repo AGENTS.md plus Agent Skills in .agents/skills | Domain graph traversal is advisory unless the host follows this repository's routing contract. |
| OpenCode | Repo AGENTS.md and skills in .agents/skills | Skill discovery and precedence depend on the installed OpenCode version. |
| GitHub Copilot / VS Code agent mode | Agent Skills in .agents/skills and supported repository instructions | VS Code is an editor, not an independent guarantee that every extension interprets the graph. |
| Claude Code | Install/symlink selected skills into .claude/skills where required; provide CLAUDE.md guidance if needed | Do not assume Claude Code automatically interprets this custom registry or repo AGENTS.md. |
| Other clients | Use an Agent Skills-aware installer or explicit file access | Discoverability, activation, and permissions must be tested per client. |

Do not copy all skill bodies into the root AGENTS.md, CLAUDE.md, or copilot-instructions.md. Prefer client-native discovery and a tiny adapter pointing to the canonical map. Avoid committing duplicate skill copies that will drift.

For cross-client installation, review the Vercel Skills installer before using it, pin refs for reproducibility, and choose explicit skills and agents rather than indiscriminately installing the entire catalog. Installing skills does not by itself enforce our hierarchical routing rules.

## Acceptance tests per client

1. Can the client discover the selected skill's name and description?
2. Does it choose the correct leaf skill for the PySpark ETL, join, skew, and near-miss cases?
3. Does it avoid loading irrelevant sibling/parent skills or unrelated references?
4. Does it distinguish unverified performance claims from measurements?
5. Does it honor permission boundaries and reject instruction injection from retrieved content?
6. What are the measured input tokens and task outcome compared with the baseline?

Record model, client/version, selected skill, files read, task success, and tokens. Do not claim "works everywhere" without these runs.

## Authoritative references

- https://agentskills.io/specification
- https://developers.openai.com/blog/skills-agents-sdk
- https://docs.opencode.ai/docs/skills/
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
- https://github.com/vercel-labs/skills/blob/main/docs/commands.md
