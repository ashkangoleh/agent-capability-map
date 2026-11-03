"""Safe, bounded, on-demand YAML graph traversal and explicitly registered skill overlays."""

import re
from pathlib import Path

import yaml


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


def require_id(value):
    if not isinstance(value, str) or len(value) > 64 or not ID.fullmatch(value):
        raise RouterError(f"Invalid capability or skill id: {value!r}")


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
        if skill is not None:
            result["selected_skill"] = skill["id"]
            result["skill_path"] = str(skill["path"])
            result["source"] = source
            result["match_strength"] = score
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
            node, failure = self._choose(request, children, route, include_mapped=True)
            if failure:
                if not route:
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

    def validate(self):
        """Thorough structural validation; not a measured LLM routing benchmark."""
        map_count = 0
        registry_count = 0
        skill_ids = set()
        node_count = 0
        visited = set()
        active_stack = set()

        def walk(path, expected_id=None, depth=0):
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
                if name in names:
                    raise RouterError(f"Duplicate sibling ID {name}: {path}")
                names.add(name)
                if not isinstance(node.get("triggers"), list) or not node["triggers"]:
                    raise RouterError(f"Missing node triggers: {name}")
                if node.get("map") and node.get("skills"):
                    raise RouterError(f"Node cannot contain both map and skills: {name}")
                if node.get("map"):
                    walk(node["map"], name, depth + 1)
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
                            p = secure_path(self.root, item.get("path"))
                            self._check_skill(p, skill_id)
                            skill_ids.add(skill_id)
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
        return {
            "maps": map_count,
            "nodes": node_count,
            "registries_checked": registry_count,
            "unique_active_skills": len(skill_ids),
            "status": "valid",
            "scope": "structural_only",
        }
