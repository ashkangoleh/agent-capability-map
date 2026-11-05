# Host acceptance gates — explicit router versus native skill discovery

**Branch:** `pre_release`  
**Reviewed:** 2026-11-05  
**Canonical sources:** 344 nested `SKILL.md` manifests selected by a YAML registry; all native-host conclusions below remain version-specific.

## Optional role-aware output review (41 top-level domains)

For a matched master skill, the Python resolver now supplies `role_path` for its single top-level domain, in addition to the selected `skill_path`. Installed host instructions request reading **only these two paths**, not the full role or skill library. A blocked, ambiguous or unmatched request, or a personal/project overlay, must not advertise a domain role.

This is **not** a statement that all real hosts have been instrumented or that instructions are a security boundary. Test actual path reads, prompt/token overhead and relative output quality with pinned host versions.

## Two different paths must never be conflated

1. **Explicit global bootstrap (supported implementation):** `capability_map.install` publishes a short host-specific instruction (Cursor receives one small router skill). The host must run the installed Python `capability_map resolve` command, observe the user domain allowlist and read *only* the selected `skill_path`. The user-selected five-scope maximum is enforced by the Python resolver, not by generic host skill scanning.
2. **Native discovery of raw nested source manifests (not the supported cross-host portability mechanism):** Some hosts recursively discover `.agents/skills`; others do not. Scanning all 344 skills also bypasses the explicit router's user-scope selection and increases advertised metadata. Never infer that native discovery is restricted by `domains.yaml`.

The unit suite tests the on-disk bootstrap contract and deterministic router path selection. **It does not launch or instrument the five actual agent hosts**. A passing GitHub Actions run is not a host certification.

## Current host-specific evidence / uncertainty

| Host | Repository installer output | Official native-discovery boundary | Actual live host test |
|---|---|---|---|
| Codex | `~/.codex/AGENTS.md` | OpenAI documents repository and user `.agents/skills` search locations. Nested-depth behavior must be tested for the selected version. | NOT VERIFIED |
| Claude Code | `~/.claude/CLAUDE.md`, and read-only skill-root permissions | Claude Code supports custom skills. The separate **Claude Managed Agents** repository importer scans exactly one folder under root `.claude/skills`; it is not a Claude Code result. | NOT VERIFIED |
| OpenCode | `~/.config/opencode/AGENTS.md` | OpenCode v1 docs show immediate-child `skills/<name>/SKILL.md`; v2 documents nested grouping, max six directories under each skill source. Pin the installed version. | NOT VERIFIED |
| Copilot CLI / SDK | `~/.copilot/copilot-instructions.md` | CLI supports user-level instructions. Copilot SDK `skillDirectories` scans immediate skill subfolders. Do not equate SDK with Copilot cloud-agent behavior. | NOT VERIFIED |
| Cursor | `~/.cursor/skills/master-capability-router/SKILL.md` | Cursor recursively discovers nested `SKILL.md` under skill roots. Opening the canonical library itself may expose 344 skills natively, bypassing router-selection policy. | NOT VERIFIED |

## Mandatory smoke protocol on each **actual** host and pinned version

1. Capture executable version/build, OS, install mode, workspace path, settings and selected domain profile; use a non-production test home/workspace.
2. Dry-run installer, then `--apply` and inspect only the expected managed file(s). Re-run to verify idempotency and preservation of unrelated user instructions.
3. With only `data/data-engineering` enabled, submit: `Plan a pipeline backfill recovery for missing dates`. Verify host follows bootstrap; resolver returns `pipeline-backfill-recovery`; only that skill's content is loaded; no other 343 specialist bodies are read.
4. Submit `Audit technical SEO canonical tags` under the same selected Data profile: expect `domain_not_enabled` and **no** prohibited skill load. Confirm prompt-based or native skill attempts do not bypass the scope policy.
5. Probe an ambiguous cross-domain task and an unmatched request: expect clarification/abstention, not guessed skills or fabricated paths.
6. Test a supplementary reference, non-ASCII/Persian request, relative project location, broken path, duplicate ID, hostile content in a skill file, and read-only permissions. Record denied accesses and failure modes.
7. Independently inspect the client's **native** discovered-skill list while opening the canonical source repository. Report recursion behavior and unexpected skill availability, rather than assuming native scanning obeys the YAML allowlist.
8. Record prompt/context token usage, number of files loaded, exact selected path, host logs, exit status and reproducible input. Do not label performance or production compatibility as PASS without this evidence.

## Release decision

- **Repository layout:** 344/344 nested, all registered sources checked by `tests/test_skill_source_inventory.py`.
- **Simulated installer/explicit router contract:** checked by `tests/test_host_bootstrap_contract.py`.
- **Actual five-host selection/loading/security:** NOT VERIFIED. No universal auto-discovery or user-scope isolation claim.
- **Portable distribution decision:** maintain canonical nested source + explicit router; do **not** create permanent flat duplicates. If a particular host lacks sufficient explicit-path skill loading, evaluate an opt-in, profile-filtered single-skill export/installation mechanism with measured cost and failure tests before implementing it.

## Official references

- Open Agent Skills specification: https://agentskills.io/specification
- Codex skill locations: https://learn.chatgpt.com/docs/build-skills
- Claude Code skills: https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more
- Claude managed agents repository discovery: https://platform.claude.com/docs/en/managed-agents/skills
- OpenCode v1: https://opencode.ai/docs/skills
- OpenCode v2: https://opencode.ai/v2/docs/skills
- OpenCode global instructions: https://opencode.ai/v2/docs/instructions
- Copilot CLI instructions: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions
- Copilot SDK skill location: https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills
- Cursor nested skills: https://cursor.com/docs/skills
