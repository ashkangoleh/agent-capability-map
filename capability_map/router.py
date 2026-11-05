"""Safe, bounded, on-demand YAML graph traversal and explicitly registered skill overlays."""

import re
from pathlib import Path

import yaml

from .domain_selection import load_domain_selection, route_is_in_scope


class RouterError(ValueError):
    """Invalid, unsafe, or internally inconsistent capability mapping."""


class StrictLoader(yaml.SafeLoader):
    def compose_node(self, parent, index):
        if self.check_event(yaml.AliasEvent):
            raise RouterError("YAML aliases are not permitted")
        return super().compose_node(parent, index)

    def construct_mapping(self, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, (str, int)):
                raise RouterError("YAML mapping keys must be strings or integers")
            if key in result:
                raise RouterError(f"Duplicate YAML key: {key}")
            result[key] = self.construct_object(value_node, deep=deep)
        return result


ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
OVERLAY = re.compile(r"<!--\s*capability-map:\s*overlay=([a-zA-Z0-9_./-]+)\s*-->")
MAX_CONFIG_BYTES = 131072
MAX_SKILL_BYTES = 65536
MAX_DEPTH = 16


def secure_path(root, relative, *, exists=True):
    root = Path(root).expanduser().resolve()
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise RouterError("Paths must be nonempty and relative")
    if ".." in Path(relative).parts or "\\" in relative or "\x00" in relative:
        raise RouterError(f"Unsafe path: {relative}")
    target = (root / relative).resolve()
    if not target.is_relative_to(root):
        raise RouterError(f"Path escapes registered root: {relative}")
    if exists and not target.is_file():
        raise RouterError(f"Missing registered file: {relative}")
    return target


def load_yaml(root, relative):
    path = secure_path(root, relative)
    if path.stat().st_size > MAX_CONFIG_BYTES:
        raise RouterError(f"YAML document exceeds size limit: {relative}")
    try:
        content = yaml.load(path.read_text(encoding="utf-8"), Loader=StrictLoader)
    except (yaml.YAMLError, UnicodeError) as exc:
        raise RouterError(f"Invalid YAML at {relative}: {exc}") from exc
    if not isinstance(content, dict):
        raise RouterError(f"Expected YAML object: {relative}")
    return content




MAX_ROLE_BYTES = 4096
ROLE_REQUIRED_SECTIONS = (
    "## Decision lens", "## Required evidence", "## Review gates",
    "## Rejection signals", "## Output contract", "## Authority boundary",
)


MAX_ROLE_CHAIN_BYTES = 8192
MAX_ROLE_CHAIN_FILES = 8


def _role_parts(scope):
    """Return validated canonical route components (not filesystem fragments)."""
    if isinstance(scope, str):
        parts = scope.split("/")
    elif isinstance(scope, (tuple, list)):
        parts = list(scope)
    else:
        raise RouterError("Domain role scope must be a route or route sequence")
    if not parts or any(not isinstance(p, str) or not ID.fullmatch(p) for p in parts):
        raise RouterError("Invalid domain role route")
    return tuple(parts)


def _role_candidate(root, parts):
    root = Path(root).expanduser().resolve()
    candidate = root / "domains"
    for segment in parts:
        candidate /= segment
        if candidate.is_symlink():
            raise RouterError("Symlinked role directory is not permitted")
    candidate /= "ROLE.md"
    if candidate.is_symlink():
        raise RouterError("Symlinked domain role is not permitted")
    return candidate


def role_contract_path(root, scope):
    """Validate a fixed-path, source-controlled advisory role at any graph depth."""
    parts = _role_parts(scope)
    candidate = _role_candidate(root, parts)
    path = secure_path(root, str(Path("domains", *parts, "ROLE.md")))
    if path != candidate:
        raise RouterError("Unexpected domain role location")
    if path.stat().st_size > MAX_ROLE_BYTES:
        raise RouterError(f"Domain role exceeds size limit: {'/'.join(parts)}")
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeError as exc:
        raise RouterError(f"Domain role is not valid UTF-8: {'/'.join(parts)}") from exc
    if not content.startswith("---\n"):
        raise RouterError(f"Domain role lacks YAML frontmatter: {'/'.join(parts)}")
    frontmatter, sep, body = content[4:].partition("\n---\n")
    if not sep:
        raise RouterError(f"Domain role frontmatter is not terminated: {'/'.join(parts)}")
    try:
        info = yaml.load(frontmatter, Loader=StrictLoader)
    except yaml.YAMLError as exc:
        raise RouterError(f"Invalid domain role frontmatter: {'/'.join(parts)}") from exc
    if not isinstance(info, dict) or set(info) != {"role_id", "version", "title"}:
        raise RouterError(f"Invalid domain role metadata schema: {'/'.join(parts)}")
    if info["role_id"] != "/".join(parts):
        raise RouterError(f"Domain role ID mismatch: {'/'.join(parts)}")
    if not isinstance(info["version"], str) or not re.fullmatch(r"1\.\d+\.\d+", info["version"]):
        raise RouterError(f"Unsupported domain role version: {'/'.join(parts)}")
    if not isinstance(info["title"], str) or not 8 <= len(info["title"]) <= 128:
        raise RouterError(f"Invalid domain role title: {'/'.join(parts)}")
    if any(heading not in body for heading in ROLE_REQUIRED_SECTIONS):
        raise RouterError(f"Missing domain role review section: {'/'.join(parts)}")
    return path


def role_paths_for_route(root, route):
    """Select only registered-route ancestors with roles, in parent-to-child order."""
    parts = _role_parts(route)
    selected = []
    total_bytes = 0
    for depth in range(1, len(parts) + 1):
        scope = parts[:depth]
        candidate = _role_candidate(root, scope)
        if candidate.is_file() or candidate.is_symlink():
            path = role_contract_path(root, scope)
            selected.append(str(path))
            total_bytes += path.stat().st_size
            if len(selected) > MAX_ROLE_CHAIN_FILES or total_bytes > MAX_ROLE_CHAIN_BYTES:
                raise RouterError("Domain role inheritance exceeds context budget")
        elif depth == 1:
            raise RouterError(f"Missing top-level domain role: {parts[0]}")
    return selected


def require_id(value):
    if not isinstance(value, str) or len(value) > 64 or not ID.fullmatch(value):
        raise RouterError(f"Invalid capability or skill id: {value!r}")


def validate_skill_relations(records):
    """Validate parent/related links between active skill records.

    records maps skill_id to (top_level_domain_id, registry_entry).
    Parent links must remain within a top-level domain; related links may cross domains.
    """
    parents = {}
    for skill_id, (domain_id, entry) in records.items():
        parent = entry.get("parent_skill")
        if parent is not None:
            require_id(parent)
            if parent == skill_id:
                raise RouterError(f"Skill cannot be its own parent: {skill_id}")
            if parent not in records:
                raise RouterError(f"Unknown parent skill {parent!r} referenced by {skill_id}")
            if records[parent][0] != domain_id:
                raise RouterError(f"Parent skill must be in the same top-level domain: {skill_id} -> {parent}")
            parents[skill_id] = parent

        related = entry.get("related_skills", [])
        if not isinstance(related, list):
            raise RouterError(f"related_skills must be a list: {skill_id}")
        seen = set()
        for target in related:
            require_id(target)
            if target == skill_id or target in seen:
                raise RouterError(f"Self or duplicate related skill on {skill_id}: {target}")
            if target not in records:
                raise RouterError(f"Unknown related skill {target!r} referenced by {skill_id}")
            seen.add(target)

    state = {}

    def visit(skill_id):
        if state.get(skill_id) == 1:
            raise RouterError(f"Skill parent cycle detected at: {skill_id}")
        if state.get(skill_id) == 2:
            return
        state[skill_id] = 1
        parent = parents.get(skill_id)
        if parent:
            visit(parent)
        state[skill_id] = 2

    for skill_id in records:
        visit(skill_id)


def match_score(request, phrases, negative=()):
    if not isinstance(phrases, list) or not all(isinstance(p, str) for p in phrases):
        raise RouterError("Triggers must be a YAML list of strings")
    text = " ".join(request.casefold().split())
    for term in negative:
        if term != "__none__" and term and re.search(r"(?<!\w)" + re.escape(term.casefold()) + r"(?!\w)", text):
            return 0, []
    matched = [p for p in phrases if p and re.search(r"(?<!\w)" + re.escape(p.casefold()) + r"(?!\w)", text)]
    if not matched:
        return 0, []
    # Deterministic lexical score, not a model probability or confidence.
    score = max(len(p.split()) * 100 + len(p) for p in matched)
    return score, matched


def ranked(request, entries, *, negative_field="excludes", include_mapped=False):
    matches = []
    for entry in entries:
        if entry.get("status") != "active" and not (include_mapped and entry.get("status") == "mapped"):
            continue
        score, terms = match_score(request, entry.get("triggers", []), entry.get(negative_field, []))
        if score:
            matches.append((score, entry, terms))
    matches.sort(key=lambda x: (-x[0], x[1]["id"]))
    return matches


class Router:
    def __init__(self, repo_root, *, project=None, home=None):
        self.root = Path(repo_root).expanduser().resolve()
        self.project = Path(project).expanduser().resolve() if project else None
        self.home = Path(home).expanduser().resolve() if home else Path.home().resolve()
        self.domain_selection = load_domain_selection(self.root, self.home)
        self.inspected = []

    def _yaml(self, root, relative):
        path = secure_path(root, relative)
        self.inspected.append(str(path))
        return load_yaml(root, relative)

    def _result(self, status, *, route=(), message="", candidates=(), skill=None, score=0, source=None):
        result = {
            "status": status,
            "route": list(route),
            "message": message,
            "candidates": list(candidates),
            "inspected_files": list(dict.fromkeys(self.inspected)),
        }
        if self.domain_selection is not None:
            result["enabled_domains"] = list(self.domain_selection)
        if skill is not None:
            result["selected_skill"] = skill["id"]
            result["skill_path"] = str(skill["path"])
            result["source"] = source
            result["match_strength"] = score
            if status == "matched" and source == "master" and route:
                role_paths = role_paths_for_route(self.root, route)
                result["role_paths"] = role_paths
                result["role_path"] = role_paths[0]  # Backward-compatible top-level alias.
        return result

    def _choose(self, request, entries, route, *, include_mapped=False):
        candidates = ranked(request, entries, include_mapped=include_mapped)
        if not candidates:
            return None, self._result(
                "needs_clarification",
                route=route,
                message="The request does not identify a specific validated child capability.",
                candidates=[n["id"] for n in entries][:12],
            )
        if not route and len(candidates) > 1 and candidates[0][0] - candidates[1][0] <= 25:
            return None, self._result(
                "needs_clarification", route=route,
                message="Multiple top-level domains match; choose primary scope before composing.",
                candidates=[n[1]["id"] for n in candidates if candidates[0][0] - n[0] <= 25],
            )
        best_score = candidates[0][0]
        ties = [n[1]["id"] for n in candidates if n[0] == best_score]
        if len(ties) > 1:
            return None, self._result(
                "needs_clarification",
                route=route,
                message="Multiple sibling capabilities match equally; do not silently guess.",
                candidates=ties,
            )
        return candidates[0], None

    def _master(self, request):
        path = "catalog/root.yaml"
        route = []
        visited = set()
        for _ in range(MAX_DEPTH):
            if path in visited:
                raise RouterError(f"Cyclic graph reference at {path}")
            visited.add(path)
            data = self._yaml(self.root, path)
            children = data.get("children", [])
            if not isinstance(children, list):
                raise RouterError(f"Expected children list at {path}")
            if self.domain_selection is not None:
                full_matches = ranked(request, children, include_mapped=True)
                scoped_children = [
                    child for child in children
                    if route_is_in_scope(route + [child.get("id", "")], self.domain_selection)
                ]
                scoped_matches = ranked(request, scoped_children, include_mapped=True)
                if full_matches and not scoped_matches:
                    return self._result(
                        "domain_not_enabled",
                        route=route,
                        message=(
                            "The request matches a domain that is not enabled in this user profile. "
                            "Inspect available domains and explicitly apply the required scope."
                        ),
                        candidates=[
                            "/".join(route + [match[1]["id"]])
                            for match in full_matches[:5]
                        ],
                    )
                children = scoped_children

            node, failure = self._choose(request, children, route, include_mapped=True)
            if failure:
                if not route and failure.get("message") == "The request does not identify a specific validated child capability.":
                    failure["status"] = "unmatched"
                    failure["message"] = "No top-level domain matched. Do not invent a skill."
                return failure
            _, child, _ = node
            require_id(child.get("id"))
            route.append(child["id"])
            if child.get("map"):
                path = child["map"]
                continue
            if child.get("status") != "active":
                return self._result("unavailable", route=route, message="Domain is mapped; no validated skill is published.")
            if child.get("skills"):
                registry = self._yaml(self.root, child["skills"])
                if not isinstance(registry.get("skills"), list):
                    raise RouterError("Missing skill registry entries")
                best, failure = self._choose(request, registry["skills"], route)
                if failure:
                    return failure
                score, item, matched_terms = best
                skill_path = secure_path(self.root, item["path"])
                return self._result(
                    "matched",
                    route=route,
                    message="Deterministic trigger match: " + ", ".join(matched_terms[:3]),
                    skill={"id": item["id"], "path": skill_path},
                    score=score,
                    source="master",
                )
            return self._result("unavailable", route=route, message="No validated skill is registered for this node.")
        raise RouterError(f"Exceeded maximum graph depth {MAX_DEPTH}")

    def _overlay_paths(self):
        personal_root = self.home / ".config" / "agent-capability-map"
        if (personal_root / "personal.yaml").is_file():
            yield "personal", personal_root, "personal.yaml"
        if not self.project:
            return
        instructions = self.project / "AGENTS.md"
        if not instructions.is_file():
            return
        if not instructions.resolve().is_relative_to(self.project):
            raise RouterError("Project AGENTS.md escapes project root")
        if instructions.stat().st_size > MAX_CONFIG_BYTES:
            raise RouterError("Project AGENTS.md exceeds size limit")
        content = instructions.read_text(encoding="utf-8")
        for relative in OVERLAY.findall(content):
            yield "project", self.project, relative

    def _overlays(self, request):
        found = []
        seen = set()
        for source, root, relative in self._overlay_paths():
            manifest = self._yaml(root, relative)
            entries = manifest.get("skills")
            if not isinstance(entries, list):
                raise RouterError(f"Overlay {relative} must declare skills list")
            for entry in entries:
                if not isinstance(entry, dict):
                    raise RouterError("Overlay skill must be an object")
                skill_id = entry.get("id")
                require_id(skill_id)
                if skill_id in seen:
                    raise RouterError(f"Duplicate user skill ID: {skill_id}")
                seen.add(skill_id)
                if entry.get("status", "active") != "active":
                    continue
                score, terms = match_score(request, entry.get("triggers", []), entry.get("excludes", []))
                if not score:
                    continue
                skill_path = secure_path(root, entry.get("path"))
                self._check_skill(skill_path, skill_id)
                found.append({
                    "id": skill_id, "score": score, "path": skill_path,
                    "source": source, "route": entry.get("route", ["personal"]),
                    "matched_terms": terms,
                })
        found.sort(key=lambda item: (-item["score"], item["id"]))
        return found

    def resolve(self, request):
        if not isinstance(request, str) or not request.strip():
            raise RouterError("Request must be non-empty")
        if len(request) > 16000:
            raise RouterError("Request is too long; provide a concise task intent")
        self.inspected = []
        master = self._master(request)
        overlays = self._overlays(request)
        if not overlays:
            return master

        # Never silently shadow a built-in skill ID.
        global_ids = self._all_registered_skill_ids()
        for overlay in overlays:
            if overlay["id"] in global_ids:
                raise RouterError(f"Overlay skill ID conflicts with master skill: {overlay['id']}")

        top = overlays[0]["score"]
        tied_overlay = [o for o in overlays if o["score"] == top]
        if len(tied_overlay) > 1 or (master["status"] == "matched" and top == master["match_strength"]):
            return self._result(
                "needs_clarification",
                message="Personal and master candidates have equal lexical evidence. Choose explicitly.",
                candidates=[o["id"] for o in tied_overlay] +
                    ([master["selected_skill"]] if master["status"] == "matched" and top == master["match_strength"] else []),
            )
        if master["status"] == "matched" and master["match_strength"] > top:
            return master
        chosen = overlays[0]
        return self._result(
            "matched", route=chosen["route"],
            message="Explicitly registered overlay matched: " + ", ".join(chosen["matched_terms"][:3]),
            skill={"id": chosen["id"], "path": chosen["path"]},
            score=chosen["score"], source=chosen["source"],
        )

    def _all_registered_skill_ids(self):
        # A small validated index avoids walking the entire global graph for every personal match.
        index = self._yaml(self.root, "catalog/master-skill-ids.yaml")
        if index.get("schema_version") != 1 or not isinstance(index.get("ids"), list):
            raise RouterError("Invalid master skill ID index")
        return set(index["ids"])

    def _registries(self):
        for path in self._walk_maps():
            data = load_yaml(self.root, path)
            for child in data.get("children", []):
                if child.get("skills"):
                    yield self._yaml(self.root, child["skills"])

    def _walk_maps(self):
        visited = set()
        stack = ["catalog/root.yaml"]
        while stack:
            path = stack.pop()
            if path in visited:
                continue
            visited.add(path)
            yield path
            doc = load_yaml(self.root, path)
            stack.extend(c["map"] for c in doc.get("children", []) if c.get("map"))

    def _check_skill(self, path, name):
        if path.stat().st_size > MAX_SKILL_BYTES:
            raise RouterError(f"SKILL.md exceeds size limit: {path}")
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            raise RouterError(f"SKILL.md is missing valid frontmatter: {path}")
        header = text.split("\n---\n", 1)[0][4:]
        data = yaml.load(header, Loader=StrictLoader)
        if not isinstance(data, dict) or data.get("name") != name:
            raise RouterError(f"Skill name mismatch for {path}: expected {name}")
        if Path(path).parent.name != name:
            raise RouterError(f"Skill folder does not match skill name: {path}")
        description = data.get("description")
        if not isinstance(description, str) or not 1 <= len(description) <= 1024:
            raise RouterError(f"Missing or invalid skill description: {path}")

    def skill_graph(self, skill_id):
        """Inspect a skill's parent chain, direct children and explicit related skills."""
        require_id(skill_id)
        self.validate()
        records = {}
        self.inspected = []
        for map_path in self._walk_maps():
            document = self._yaml(self.root, map_path)
            for child in document.get("children", []):
                if not child.get("skills"):
                    continue
                registry = self._yaml(self.root, child["skills"])
                for entry in registry.get("skills", []):
                    if entry.get("status") == "active":
                        records.setdefault(entry["id"], entry)
        if skill_id not in records:
            raise RouterError(f"Unknown active skill: {skill_id}")

        ancestry = []
        seen = {skill_id}
        parent = records[skill_id].get("parent_skill")
        while parent:
            if parent in seen:
                raise RouterError(f"Skill parent cycle detected at: {parent}")
            if parent not in records:
                raise RouterError(f"Unknown parent skill {parent!r} referenced by {skill_id}")
            seen.add(parent)
            ancestry.append(parent)
            parent = records[parent].get("parent_skill")
        ancestry.reverse()
        children = sorted(
            candidate_id for candidate_id, entry in records.items()
            if entry.get("parent_skill") == skill_id
        )
        return {
            "status": "ok",
            "skill": skill_id,
            "ancestry": ancestry,
            "children": children,
            "related_skills": records[skill_id].get("related_skills", []),
            "inspected_files": list(dict.fromkeys(self.inspected)),
        }

    def related(self, route):
        """Return explicit typed cross-domain edges without loading skill instructions."""
        names = tuple(route.split("/")) if isinstance(route, str) else tuple(route)
        if not names or any(not ID.fullmatch(name) for name in names):
            raise RouterError("Related route must be slash-separated capability IDs")
        self.inspected = []
        catalog = self._yaml(self.root, "catalog/relations.yaml")
        edges = [
            edge for edge in catalog.get("edges", [])
            if tuple(edge.get("from", [])) == names or tuple(edge.get("to", [])) == names
        ]
        return {"status": "ok", "route": list(names), "relations": edges,
                "inspected_files": list(self.inspected)}

    def validate(self):
        """Thorough structural validation; not a measured LLM routing benchmark."""
        map_count = 0
        registry_count = 0
        skill_ids = set()
        skill_records = {}
        node_count = 0
        visited = set()
        active_stack = set()
        routes = set()

        def walk(path, expected_id=None, depth=0, chain=()):
            nonlocal map_count, registry_count, node_count
            if depth > MAX_DEPTH:
                raise RouterError("Graph exceeds maximum depth")
            if path in active_stack:
                raise RouterError(f"Graph cycle: {path}")
            if path in visited:
                return
            visited.add(path)
            active_stack.add(path)
            doc = self._yaml(self.root, path)
            map_count += 1
            if expected_id and doc.get("id") != expected_id:
                raise RouterError(f"Node ID mismatch: {path}")
            if doc.get("schema_version") != 1:
                raise RouterError(f"Unsupported schema version: {path}")
            children = doc.get("children")
            if not isinstance(children, list):
                raise RouterError(f"Missing children list: {path}")
            names = set()
            for node in children:
                if not isinstance(node, dict):
                    raise RouterError(f"Non-object node: {path}")
                name = node.get("id")
                require_id(name)
                node_count += 1
                current_route = chain + (name,)
                routes.add(current_route)
                if name in names:
                    raise RouterError(f"Duplicate sibling ID {name}: {path}; sibling_ids={[child.get('id') for child in children]}")
                names.add(name)
                if node.get("status") == "active":
                    scope = current_route
                    candidate = _role_candidate(self.root, scope)
                    if depth == 0 or candidate.is_file() or candidate.is_symlink():
                        role_contract_path(self.root, scope)
                if not isinstance(node.get("triggers"), list) or not node["triggers"]:
                    raise RouterError(f"Missing node triggers: {name}")
                if node.get("map") and node.get("skills"):
                    raise RouterError(f"Node cannot contain both map and skills: {name}")
                if node.get("map"):
                    walk(node["map"], name, depth + 1, current_route)
                elif node.get("skills"):
                    registry = self._yaml(self.root, node["skills"])
                    registry_count += 1
                    if registry.get("kind") != "skill-registry" or not isinstance(registry.get("skills"), list):
                        raise RouterError(f"Invalid skills registry: {node['skills']}")
                    for item in registry["skills"]:
                        skill_id = item.get("id")
                        require_id(skill_id)
                        if not isinstance(item.get("triggers"), list) or not item["triggers"]:
                            raise RouterError(f"Missing skill triggers: {skill_id}")
                        if item.get("status") == "active":
                            if not isinstance(item.get("description"), str) or len(item["description"]) < 40:
                                raise RouterError(f"Weak skill description: {skill_id}")
                            p = secure_path(self.root, item.get("path"))
                            self._check_skill(p, skill_id)
                            skill_ids.add(skill_id)
                            domain_id = chain[0] if chain else None
                            if skill_id in skill_records:
                                previous_domain, previous_item = skill_records[skill_id]
                                if previous_domain != domain_id:
                                    raise RouterError(f"Skill ID is registered in multiple top-level domains: {skill_id}")
                                merged_item = dict(previous_item)
                                for relation_key in ("parent_skill", "related_skills"):
                                    if relation_key in item:
                                        if relation_key in merged_item and merged_item[relation_key] != item[relation_key]:
                                            raise RouterError(f"Conflicting {relation_key} metadata for skill: {skill_id}")
                                        merged_item[relation_key] = item[relation_key]
                                skill_records[skill_id] = (domain_id, merged_item)
                            else:
                                skill_records[skill_id] = (domain_id, item)
                elif node.get("status") == "active":
                    raise RouterError(f"Active node has neither map nor skill: {name}")
            active_stack.remove(path)

        self.inspected = []
        walk("catalog/root.yaml")
        index = self._yaml(self.root, "catalog/master-skill-ids.yaml")
        indexed = index.get("ids", [])
        if index.get("schema_version") != 1 or not isinstance(indexed, list):
            raise RouterError("Invalid master skill ID index")
        if len(indexed) != len(set(indexed)) or set(indexed) != skill_ids:
            raise RouterError("Stale or duplicate master skill ID index")
        validate_skill_relations(skill_records)
        relations = self._yaml(self.root, "catalog/relations.yaml")
        edges = relations.get("edges", [])
        allowed = {"uses", "runs_on", "orchestrated_by", "supports", "depends_on", "related_to"}
        if relations.get("schema_version") != 1 or not isinstance(edges, list):
            raise RouterError("Invalid typed relationship catalog")
        for edge in edges:
            if not isinstance(edge, dict):
                raise RouterError("Relationship must be an object")
            origin = tuple(edge.get("from", []))
            target = tuple(edge.get("to", []))
            if origin not in routes or target not in routes or origin == target:
                raise RouterError(f"Invalid relationship endpoints: {edge}")
            if edge.get("relation") not in allowed:
                raise RouterError(f"Unsupported relationship type: {edge}")
        user_count = 0
        user_ids = set()
        for source, source_root, relative in self._overlay_paths():
            overlay = self._yaml(source_root, relative)
            if overlay.get("schema_version") != 1 or not isinstance(overlay.get("skills"), list):
                raise RouterError(f"Invalid registered overlay schema: {relative}")
            for entry in overlay["skills"]:
                if not isinstance(entry, dict):
                    raise RouterError(f"Invalid registered skill entry: {relative}")
                uid = entry.get("id")
                require_id(uid)
                if uid in user_ids or uid in skill_ids:
                    raise RouterError(f"Duplicate or shadowed registered skill ID: {uid}")
                user_ids.add(uid)
                if not isinstance(entry.get("triggers"), list) or not entry["triggers"]:
                    raise RouterError(f"Missing registered skill triggers: {uid}")
                if not isinstance(entry.get("route"), list) or not entry["route"] or any(
                    not isinstance(n, str) or not ID.fullmatch(n) for n in entry["route"]
                ):
                    raise RouterError(f"Invalid registered route for: {uid}")
                if entry.get("status", "active") == "active":
                    self._check_skill(secure_path(source_root, entry.get("path")), uid)
                    user_count += 1
        return {
            "maps": map_count,
            "nodes": node_count,
            "registered_user_skills": user_count,
            "registries_checked": registry_count,
            "cross_domain_relations": len(edges),
            "unique_active_skills": len(skill_ids),
            "status": "valid",
            "scope": "structural_only",
        }
