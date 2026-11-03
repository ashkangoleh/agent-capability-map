#!/usr/bin/env python3
"""Validate domain maps, local skill registries, skill metadata, and routing fixtures."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_NAME_RE = re.compile(r"^name:\s*([a-z0-9-]+)\s*$", re.MULTILINE)
FRONTMATTER_DESC_RE = re.compile(r"^description:\s*(.+?)\s*$", re.MULTILINE)


class ValidationError(Exception):
    pass


def load_json(relative_path):
    path = ROOT / relative_path
    if not path.is_file():
        raise ValidationError(f"Missing JSON file: {relative_path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid JSON in {relative_path}: {exc}") from exc


def require_file(relative_path):
    if not (ROOT / relative_path).is_file():
        raise ValidationError(f"Missing referenced file: {relative_path}")


def validate():
    errors = []
    domains_doc = load_json("catalog/domains.json")
    domains = domains_doc.get("domains", [])
    domain_ids = [item.get("id") for item in domains]

    if not domains:
        errors.append("catalog/domains.json has no domains")
    if len(domain_ids) != len(set(domain_ids)):
        errors.append("Duplicate domain IDs")

    all_skill_ids = set()
    active_count = 0

    for domain in domains:
        domain_id = domain.get("id", "")
        if not NAME_RE.fullmatch(domain_id):
            errors.append(f"Invalid domain ID: {domain_id}")

        router = domain.get("router")
        if router:
            try:
                require_file(router)
            except ValidationError as exc:
                errors.append(str(exc))

        registry_path = domain.get("skills_registry")
        if not registry_path:
            continue

        try:
            registry = load_json(registry_path)
        except ValidationError as exc:
            errors.append(str(exc))
            continue

        if registry.get("domain") != domain_id:
            errors.append(f"{registry_path}: domain does not match {domain_id}")

        for skill in registry.get("skills", []):
            skill_id = skill.get("id", "")
            if skill_id in all_skill_ids:
                errors.append(f"Duplicate skill ID: {skill_id}")
            all_skill_ids.add(skill_id)

            if not NAME_RE.fullmatch(skill_id):
                errors.append(f"{registry_path}: invalid skill ID {skill_id}")
            if len(skill.get("description", "")) < 30:
                errors.append(f"{registry_path}: weak description for {skill_id}")
            if not skill.get("triggers"):
                errors.append(f"{registry_path}: missing triggers for {skill_id}")
            if not skill.get("outputs"):
                errors.append(f"{registry_path}: missing outputs for {skill_id}")

            skill_path = skill.get("path", "")
            if skill.get("status") == "active":
                active_count += 1
                try:
                    require_file(skill_path)
                except ValidationError as exc:
                    errors.append(str(exc))
                    continue

                if not skill_path.startswith(".agents/skills/") or not skill_path.endswith("/SKILL.md"):
                    errors.append(f"{skill_id}: skill path must use .agents/skills/<name>/SKILL.md")

                if Path(skill_path).parent.name != skill_id:
                    errors.append(f"{skill_id}: directory name does not match skill ID")

                content = (ROOT / skill_path).read_text(encoding="utf-8")
                if not content.startswith("---\n"):
                    errors.append(f"{skill_id}: missing YAML frontmatter")
                    continue

                closing = content.find("\n---\n", 4)
                if closing < 0:
                    errors.append(f"{skill_id}: unterminated YAML frontmatter")
                    continue

                frontmatter = content[4:closing]
                name_match = FRONTMATTER_NAME_RE.search(frontmatter)
                desc_match = FRONTMATTER_DESC_RE.search(frontmatter)
                if not name_match or name_match.group(1) != skill_id:
                    errors.append(f"{skill_id}: frontmatter name does not match registry ID")
                if not desc_match or len(desc_match.group(1).strip()) < 30:
                    errors.append(f"{skill_id}: missing or weak frontmatter description")

    fixture_doc = load_json("tests/fixtures/routing-cases.json")
    case_ids = set()
    allowed_kinds = {"positive", "negative", "near_miss", "abstention"}
    for case in fixture_doc.get("cases", []):
        case_id = case.get("id", "")
        if not case_id or case_id in case_ids:
            errors.append(f"Missing or duplicate routing case ID: {case_id}")
        case_ids.add(case_id)
        if case.get("kind") not in allowed_kinds:
            errors.append(f"{case_id}: invalid routing case kind")
        if not case.get("prompt", "").strip():
            errors.append(f"{case_id}: empty prompt")
        if case.get("expected_domain") not in domain_ids:
            errors.append(f"{case_id}: unknown expected domain")
        expected_skill = case.get("expected_skill")
        if expected_skill is not None and expected_skill not in all_skill_ids:
            errors.append(f"{case_id}: unknown expected skill {expected_skill}")
        if case.get("kind") == "abstention" and expected_skill is not None:
            errors.append(f"{case_id}: abstention case must have expected_skill=null")

    if active_count == 0:
        errors.append("No active skills found")

    if errors:
        raise ValidationError("\n".join(f"- {item}" for item in errors))

    print(
        f"Validation passed: {len(domains)} domains, "
        f"{active_count} active skills, {len(all_skill_ids)} registered skills, "
        f"{len(case_ids)} routing fixtures."
    )


if __name__ == "__main__":
    try:
        validate()
    except ValidationError as exc:
        print(f"Validation failed:\n{exc}", file=sys.stderr)
        sys.exit(1)
