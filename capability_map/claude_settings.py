"""Safe, user-scoped Claude Code access for the master skill directory."""

import json
import os
import stat
import tempfile
from pathlib import Path

from .router import RouterError


def resolve_claude_config_dir(home, override=None):
    configured = override if override is not None else os.environ.get("CLAUDE_CONFIG_DIR")
    candidate = Path(configured).expanduser() if configured else Path(home).expanduser() / ".claude"
    return candidate.resolve()


def _resolve_skill_root(root):
    root = Path(root).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise RouterError(f"Master repository root is not a directory: {root}")
    agents = root / ".agents"
    skills = agents / "skills"
    if agents.is_symlink() or skills.is_symlink():
        raise RouterError("Refusing symlinked master skill directories")
    if not skills.is_dir():
        raise RouterError(f"Master skill directory does not exist: {skills}")
    resolved = skills.resolve(strict=True)
    if not resolved.is_relative_to(root):
        raise RouterError("Master skill directory resolves outside the repository root")
    return resolved


def _resolve_role_root(root):
    root = Path(root).expanduser().resolve(strict=True)
    roles = root / "domains"
    if roles.is_symlink() or not roles.is_dir():
        raise RouterError("Master domain role directory is missing or symlinked")
    resolved = roles.resolve(strict=True)
    if not resolved.is_relative_to(root):
        raise RouterError("Domain roles directory escapes repository root")
    return resolved


def _escape_gitignore_segment(segment):
    special = {"\\", "*", "?", "[", "]", "!", "#"}
    return "".join("\\" + char if char in special else char for char in segment)


def _edit_deny_rule(skills_root):
    escaped = "/".join(_escape_gitignore_segment(part) for part in skills_root.parts if part != "/")
    return f"Edit(//{escaped}/**)"


def _atomic_write(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o600
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent)
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def configure_claude_skill_access(config_dir, root, apply=False):
    """Add read access and a built-in-tool edit deny for the master skill directory."""
    skills_root = _resolve_skill_root(root)
    roles_root = _resolve_role_root(root)
    settings_path = Path(config_dir).expanduser().resolve() / "settings.json"

    if settings_path.is_symlink():
        raise RouterError(f"Refusing to modify symlink: {settings_path}")
    if settings_path.exists() and not settings_path.is_file():
        raise RouterError(f"Claude settings destination is not a regular file: {settings_path}")

    settings = {}
    if settings_path.exists():
        try:
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeError) as exc:
            raise RouterError(f"Claude settings must be valid UTF-8 JSON: {settings_path}") from exc
        if not isinstance(settings, dict):
            raise RouterError(f"Claude settings root must be a JSON object: {settings_path}")

    permissions = settings.setdefault("permissions", {})
    if not isinstance(permissions, dict):
        raise RouterError(f"Claude settings 'permissions' must be an object: {settings_path}")

    directories = permissions.setdefault("additionalDirectories", [])
    if not isinstance(directories, list) or any(not isinstance(item, str) for item in directories):
        raise RouterError(f"Claude permissions.additionalDirectories must be an array of strings: {settings_path}")

    deny = permissions.setdefault("deny", [])
    if not isinstance(deny, list) or any(not isinstance(item, str) for item in deny):
        raise RouterError(f"Claude permissions.deny must be an array of strings: {settings_path}")

    skill_path = str(skills_root)
    role_path = str(roles_root)
    edit_rule = _edit_deny_rule(skills_root)
    role_edit_rule = _edit_deny_rule(roles_root)
    add_directory = skill_path not in directories
    add_deny = edit_rule not in deny
    add_role_directory = role_path not in directories
    add_role_deny = role_edit_rule not in deny
    if add_directory:
        directories.append(skill_path)
    if add_role_directory:
        directories.append(role_path)
    if add_deny:
        deny.append(edit_rule)
    if add_role_deny:
        deny.append(role_edit_rule)

    changed = add_directory or add_deny or add_role_directory or add_role_deny
    if apply and changed:
        payload = json.dumps(settings, ensure_ascii=False, indent=2) + "\n"
        _atomic_write(settings_path, payload)

    return {
        "path": str(settings_path),
        "skills_root": skill_path,
        "roles_root": role_path,
        "added_role_directory": add_role_directory,
        "added_role_edit_deny": add_role_deny,
        "changed": changed,
        "applied": bool(apply and changed),
        "added_additional_directory": add_directory,
        "added_edit_deny": add_deny,
    }
