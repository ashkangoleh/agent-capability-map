# Global Host Adapters — 2026-11-03

This project uses a compact, user-scoped bootstrap per host. The installed Python resolver owns YAML routing; hosts own their own instruction discovery and tool permissions.

| Host | Master bootstrap | Activation expectations |
|---|---|---|
| Codex | ~/.codex/AGENTS.md | Global instructions recognized in local CLI and supported integrations. Agent chooses when to run resolver. |
| Claude Code | ~/.claude/CLAUDE.md | User-level instruction file. Agent uses shell/tool access for resolver; not a native Claude plugin. |
| OpenCode | ~/.config/opencode/AGENTS.md | User-level instruction file in current OpenCode docs. |
| Copilot | ~/.copilot/copilot-instructions.md | User-scoped instructions in supported Copilot CLI and VS Code environments; remote GitHub agent behavior differs. |
| Cursor | ~/.cursor/skills/master-capability-router/SKILL.md | Global router skill discoverable on local machine. Its auto-activation depends on task relevance and host rules. |

Official references:

- Agent Skills specification: https://agentskills.io/specification
- Codex customizations: https://learn.chatgpt.com/docs/customization/overview
- Claude Code skills: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- OpenCode rules: https://docs.opencode.ai/docs/rules/
- Cursor skills: https://cursor.com/help/customization/skills
- VS Code user instructions: https://code.visualstudio.com/docs/agent-customization/custom-instructions
- GitHub Copilot skills: https://docs.github.com/en/copilot/concepts/customizations/agent-skills

## Requirements

The CLI must be installed into a Python environment that the selected host can invoke. The cloned repository must remain available. Global user-scoped instructions may not be copied into cloud agents or remote CI workers.

Do not assume compatibility from the presence of a file. Test invocation, actual selected paths, and permitted filesystem/tool access in every target host/version.

## Safety

Installation is dry-run by default. Managed blocks preserve unrelated content. Avoid placing credentials, retrieved documents, or raw user-provided shell strings into global instructions. Project AGENTS.md may point to an explicitly registered project overlay, but unregistered project files must not be loaded.

## Version and support boundaries

Host discovery behavior changes. Keep a per-host compatibility matrix, record tested host version and date, and repeat smoke tests after each host upgrade. The current repository has implementation and CI tests; it does not assert that every host has completed end-to-end runtime validation.


## Claude Code: managed skill-root access

When `capability-map install --hosts claude --apply` runs, it also configures the user-level Claude Code settings file. If `CLAUDE_CONFIG_DIR` is set, that directory is used; otherwise the path is `~/.claude`.

- Add the canonical master `.agents/skills` directory to `permissions.additionalDirectories`. Claude Code treats it as an additional working directory, so file reads are available without the outside-working-directory approval prompt.
- Add `Edit(//absolute/path/.agents/skills/**)` to `permissions.deny`. Claude Code documents that `Edit(path)` covers built-in file-edit tools, including Write; the deny rule is intentionally scoped to the master skill root.
- Preserve unrelated settings and permission entries. The installer previews both the instruction file and settings mutation during dry-run, and writes only with `--apply`.
- Invalid JSON, invalid permission value types, symlinked settings files, and symlinked master skill roots are rejected before either destination is changed.

This is not OS-level read-only enforcement. Claude Code's path rules do not constrain arbitrary subprocesses that open files indirectly; use OS permissions or Claude Code sandboxing when that stronger boundary is required. Managed settings may also impose higher-priority restrictions.

Official references:
- https://code.claude.com/docs/en/permissions#working-directories
- https://code.claude.com/docs/en/permissions#read-and-edit
- https://code.claude.com/docs/en/settings
