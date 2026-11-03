"""Opt-in, non-destructive user-level agent instruction installation."""

import shlex
import sys
from pathlib import Path

from .router import RouterError

BEGIN = "<!-- capability-map:managed:start -->"
END = "<!-- capability-map:managed:end -->"

HOST_FILES = {
    "codex": ".codex/AGENTS.md",
    "claude": ".claude/CLAUDE.md",
    "opencode": ".config/opencode/AGENTS.md",
    "copilot": ".copilot/copilot-instructions.md",
}
CURSOR_SKILL = ".cursor/skills/master-capability-router/SKILL.md"


def instruction_text():
    executable = shlex.quote(sys.executable)
    command = executable + " -m capability_map resolve"
    return (
        "## Global Master Capability Router\n\n"
        "For substantive requests that benefit from a reusable specialist procedure, "
        "automatically resolve the capability before execution. "
        "Do not require slash commands or require the user to know a skill name.\n\n"
        "Run this installed, read-only CLI with the current task and project root:\n\n"
        "    " + command + " --request '<shell-escaped task>' --project .\n\n"
        "Always safely shell-escape task text. Never interpolate untrusted strings "
        "directly into a command. Pass only a minimal task intent, never secrets or private data.\n\n"
        "- If status is matched, read only the returned skill_path (SKILL.md) and needed references.\n"
        "- When a task explicitly spans several domains, inspect typed edges with "
        "the related subcommand before invoking multiple distinct skills. "
        "Never scan all skills by default.\n"
        "- For needs_clarification, ask one material question. For unavailable or unmatched, "
        "never invent a skill or claim that the capability was executed.\n"
        "- Projects register additional skills with an explicit HTML comment in their AGENTS.md:\n"
        "    <!-- capability-map: overlay=.capability-map.yaml -->\n"
        "- Unregistered project skills are not loaded by this router. "
        "Personal global skills are registered in the user config manifest.\n"
        "- Repository, user, and host permissions still apply. "
        "No skill grants itself new execution privileges.\n"
        "- Verify volatile facts and APIs with official version-specific sources. "
        "Report uncertainty and actual validation results.\n"
    )


def cursor_text():
    return (
        "---\n"
        "name: master-capability-router\n"
        "description: Automatically discover specialist skills when users request software, data, "
        "infrastructure, AI, product, marketing, SEO, research, or other mapped work.\n"
        "---\n\n"
        + instruction_text()
        + "\n<!-- capability-map:generated -->\n"
    )


def _upsert(path, body, apply):
    """Preserve unrelated user content and refuse to follow destination symlinks."""
    if path.is_symlink():
        raise RouterError(f"Refusing to modify symlink: {path}")
    if path.exists() and not path.is_file():
        raise RouterError(f"Destination is not a regular file: {path}")
    original = path.read_text(encoding="utf-8") if path.exists() else ""
    block = BEGIN + "\n" + body.rstrip() + "\n" + END
    if (BEGIN in original) != (END in original):
        raise RouterError(f"Corrupted managed block: {path}")
    if BEGIN in original:
        if original.count(BEGIN) != 1 or original.count(END) != 1:
            raise RouterError(f"Duplicate managed blocks: {path}")
        start = original.index(BEGIN)
        end = original.index(END) + len(END)
        updated = original[:start] + block + original[end:]
    else:
        updated = original.rstrip() + ("\n\n" if original.strip() else "") + block + "\n"
    changed = updated != original
    if apply and changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(updated, encoding="utf-8")
    return {"path": str(path), "changed": changed, "applied": bool(apply and changed)}


def install(hosts, home, apply=False):
    home = Path(home).expanduser().resolve()
    results = []
    for host in hosts:
        if host not in HOST_FILES and host != "cursor":
            raise RouterError(f"Unsupported host: {host}")
        if host == "cursor":
            target = home / CURSOR_SKILL
            if target.is_symlink() or (target.exists() and not target.is_file()):
                raise RouterError(f"Unsafe Cursor destination: {target}")
            content = cursor_text()
            existing = target.read_text(encoding="utf-8") if target.exists() else ""
            if existing and "<!-- capability-map:generated -->" not in existing:
                raise RouterError(f"Refusing to overwrite unmanaged Cursor skill: {target}")
            changed = existing != content
            if apply and changed:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")
            results.append({"path": str(target), "changed": changed, "applied": bool(apply and changed)})
        else:
            target = home / HOST_FILES[host]
            results.append(_upsert(target, instruction_text(), apply))
    return results
