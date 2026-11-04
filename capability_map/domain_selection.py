"""User-scoped, explicit domain allowlist for the capability router.

A selection controls which branches the resolver may traverse. It does not copy
skills into host directories or change the master repository.
"""

import os
import tempfile
from pathlib import Path

import yaml

MAX_SELECTED_DOMAINS = 5
PROFILE_RELATIVE = Path(".config") / "agent-capability-map" / "domains.yaml"
MAX_PROFILE_BYTES = 131072


def _router_api():
    # Lazy import avoids a module cycle: Router consumes this module as well.
    from .router import RouterError, load_yaml, require_id

    return RouterError, load_yaml, require_id


def _profile_paths(home):
    RouterError, _, _ = _router_api()
    home = Path(home).expanduser().resolve()
    if not home.exists() or not home.is_dir():
        raise RouterError(f"User home is not a directory: {home}")

    config_dir = home / ".config"
    app_dir = config_dir / "agent-capability-map"
    profile = app_dir / "domains.yaml"

    for directory in (config_dir, app_dir):
        if directory.is_symlink():
            raise RouterError(f"Refusing symlinked domain configuration directory: {directory}")
        if directory.exists() and not directory.is_dir():
            raise RouterError(f"Domain configuration path is not a directory: {directory}")
        if not directory.resolve().is_relative_to(home):
            raise RouterError(f"Domain configuration directory escapes user home: {directory}")

    if profile.is_symlink():
        raise RouterError(f"Refusing symlinked domain selection profile: {profile}")
    if profile.exists() and not profile.is_file():
        raise RouterError(f"Domain selection profile is not a regular file: {profile}")
    if not profile.resolve().is_relative_to(home):
        raise RouterError(f"Domain selection profile escapes user home: {profile}")
    return home, app_dir, profile


def _subtree_metrics(root, map_path):
    _, load_yaml, _ = _router_api()
    visited = set()
    skill_ids = set()
    active_nodes = 0
    mapped_nodes = 0

    def walk(path):
        nonlocal active_nodes, mapped_nodes
        if path in visited:
            return
        visited.add(path)
        document = load_yaml(root, path)
        children = document.get("children")
        if not isinstance(children, list):
            raise _router_api()[0](f"Expected children list at {path}")
        for child in children:
            if not isinstance(child, dict):
                raise _router_api()[0](f"Invalid child node at {path}")
            status = child.get("status")
            if status == "active":
                active_nodes += 1
            elif status == "mapped":
                mapped_nodes += 1

            if child.get("map"):
                walk(child["map"])
            elif child.get("skills"):
                registry = load_yaml(root, child["skills"])
                for item in registry.get("skills", []):
                    if item.get("status") == "active":
                        skill_ids.add(item["id"])

    walk(map_path)
    return {
        "active_nodes": active_nodes,
        "mapped_nodes": mapped_nodes,
        "active_skill_count": len(skill_ids),
    }


def discover_domains(root, prefix=None):
    """Return selectable active map nodes, including nested domain scopes."""
    RouterError, load_yaml, require_id = _router_api()
    root = Path(root).expanduser().resolve()
    catalog = load_yaml(root, "catalog/root.yaml")
    results = []

    def walk(map_path, parent_route=()):
        document = load_yaml(root, map_path)
        children = document.get("children")
        if not isinstance(children, list):
            raise RouterError(f"Expected children list at {map_path}")
        for node in children:
            if not isinstance(node, dict):
                raise RouterError(f"Invalid domain node at {map_path}")
            domain_id = node.get("id")
            require_id(domain_id)
            route = parent_route + (domain_id,)
            child_map = node.get("map")
            if node.get("status") == "active" and child_map:
                metrics = _subtree_metrics(root, child_map)
                results.append({
                    "route": "/".join(route),
                    "id": domain_id,
                    "label": node.get("label") or node.get("description") or domain_id,
                    "description": node.get("description", ""),
                    "kind": "domain" if len(route) == 1 else "subdomain",
                    "active_nodes": metrics["active_nodes"],
                    "mapped_nodes": metrics["mapped_nodes"],
                    "active_skill_count": metrics["active_skill_count"],
                })
                walk(child_map, route)

    walk("catalog/root.yaml")
    if prefix is not None:
        parts = tuple(prefix.split("/")) if isinstance(prefix, str) else tuple(prefix)
        if not parts or any(not isinstance(part, str) for part in parts):
            raise RouterError("Domain prefix must be a canonical slash-separated route")
        for part in parts:
            require_id(part)
        prefix_text = "/".join(parts)
        available = {item["route"] for item in results}
        if prefix_text not in available:
            raise RouterError(f"Unknown domain prefix: {prefix_text}")
        results = [
            item for item in results
            if item["route"] == prefix_text or item["route"].startswith(prefix_text + "/")
        ]
    return results


def _normalize_domains(root, domains):
    RouterError, _, require_id = _router_api()
    if not isinstance(domains, (list, tuple)) or not domains:
        raise RouterError("Select at least one domain scope")
    if len(domains) > MAX_SELECTED_DOMAINS:
        raise RouterError(
            f"At most {MAX_SELECTED_DOMAINS} domain scopes can be applied at once"
        )

    available = {item["route"] for item in discover_domains(root)}
    normalized = []
    for value in domains:
        if not isinstance(value, str):
            raise RouterError("Domain scopes must be strings")
        parts = value.split("/")
        if not parts or any(not part for part in parts):
            raise RouterError(f"Invalid domain route: {value!r}")
        for part in parts:
            require_id(part)
        route = "/".join(parts)
        if route not in available:
            raise RouterError(f"Unknown or non-selectable domain scope: {route}")
        if route in normalized:
            raise RouterError(f"Duplicate domain scope: {route}")
        normalized.append(route)

    route_parts = [(route, tuple(route.split("/"))) for route in normalized]
    for index, (left, left_parts) in enumerate(route_parts):
        for right, right_parts in route_parts[index + 1:]:
            if (
                left_parts == right_parts[:len(left_parts)]
                or right_parts == left_parts[:len(right_parts)]
            ):
                raise RouterError(
                    f"Overlapping domain scopes are not allowed: {left} and {right}"
                )
    return normalized


def route_is_in_scope(candidate_route, selected_domains):
    """True when a traversed route is an ancestor or descendant of a selected scope."""
    candidate = tuple(candidate_route)
    for selected in selected_domains:
        parts = tuple(selected.split("/"))
        if candidate == parts[:len(candidate)] or parts == candidate[:len(parts)]:
            return True
    return False


def load_domain_selection(root, home):
    """Load and fully validate the user's optional domain allowlist.

    None means unrestricted legacy behavior; a list means strict allowlist mode.
    """
    RouterError, load_yaml, _ = _router_api()
    _, app_dir, profile = _profile_paths(home)
    if not profile.exists():
        return None
    if profile.stat().st_size > MAX_PROFILE_BYTES:
        raise RouterError("Domain selection profile exceeds size limit")
    manifest = load_yaml(app_dir, "domains.yaml")
    if set(manifest) != {"schema_version", "domains"}:
        raise RouterError("Domain selection profile has unsupported fields")
    if manifest.get("schema_version") != 1:
        raise RouterError("Unsupported domain selection schema version")
    return _normalize_domains(root, manifest.get("domains"))


def domain_status(root, home):
    selected = load_domain_selection(root, home)
    available = discover_domains(root)
    return {
        "status": "ok",
        "mode": "restricted" if selected is not None else "all",
        "registered_domains": selected or [],
        "available_domain_scopes": len(available),
        "max_domains_per_apply": MAX_SELECTED_DOMAINS,
        "profile_path": str(_profile_paths(home)[2]),
        "message": (
            "Only registered domain scopes are eligible for master routing."
            if selected is not None
            else "No domain allowlist is configured; all active domain scopes remain eligible."
        ),
    }


def _write_profile(app_dir, profile, domains):
    RouterError, _, _ = _router_api()
    app_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
    if app_dir.is_symlink() or not app_dir.is_dir():
        raise RouterError(f"Unsafe domain configuration directory: {app_dir}")
    if profile.is_symlink() or (profile.exists() and not profile.is_file()):
        raise RouterError(f"Unsafe domain selection destination: {profile}")

    payload = yaml.safe_dump(
        {"schema_version": 1, "domains": domains},
        sort_keys=False,
        allow_unicode=True,
    )
    descriptor, temporary = tempfile.mkstemp(
        prefix=".domains-", suffix=".tmp", dir=str(app_dir)
    )
    try:
        if hasattr(os, "fchmod"):
            os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, profile)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def _remove_profile(profile):
    RouterError, _, _ = _router_api()
    if profile.is_symlink():
        raise RouterError(f"Refusing to remove symlinked domain profile: {profile}")
    if profile.exists():
        if not profile.is_file():
            raise RouterError(f"Domain profile is not a regular file: {profile}")
        profile.unlink()


def update_domain_selection(root, home, domains=None, *, operation="replace", apply=False):
    """Preview or atomically update the user-scoped domain allowlist."""
    RouterError, _, _ = _router_api()
    _, app_dir, profile = _profile_paths(home)
    current = load_domain_selection(root, home)

    if operation == "replace":
        after = _normalize_domains(root, domains)
    elif operation == "add":
        additions = _normalize_domains(root, domains)
        new_additions = [item for item in additions if item not in (current or [])]
        after = _normalize_domains(root, (current or []) + new_additions)
    elif operation == "remove":
        if current is None:
            raise RouterError("No restricted domain selection exists; use apply to choose scopes")
        removals = _normalize_domains(root, domains)
        unknown = sorted(set(removals) - set(current))
        if unknown:
            raise RouterError("Cannot remove domains that are not registered: " + ", ".join(unknown))
        remaining = [item for item in current if item not in removals]
        if not remaining:
            raise RouterError("At least one domain must remain; use domains clear to restore all domains")
        after = _normalize_domains(root, remaining)
    elif operation == "clear":
        after = None
    else:
        raise RouterError(f"Unsupported domain selection operation: {operation}")

    changed = after != current
    if apply and changed:
        if after is None:
            _remove_profile(profile)
        else:
            _write_profile(app_dir, profile, after)

    return {
        "status": "applied" if apply else "dry_run",
        "operation": operation,
        "changed": changed,
        "before_mode": "restricted" if current is not None else "all",
        "before_domains": current or [],
        "after_mode": "restricted" if after is not None else "all",
        "after_domains": after or [],
        "max_domains_per_apply": MAX_SELECTED_DOMAINS,
        "profile_path": str(profile),
        "message": (
            "Domain selection updated atomically."
            if apply and changed
            else "Preview only; no files were changed."
            if not apply
            else "Selection already matches the requested state; no write was needed."
        ),
    }
