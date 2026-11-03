#!/usr/bin/env python3
"""Read-only graph inspection. This is not a semantic router or agent loader."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_records(root=ROOT):
    records = {}
    doc = json.loads((root / "catalog/domains.json").read_text(encoding="utf-8"))
    for domain in doc["domains"]:
        if not domain.get("skills_registry"):
            continue
        registry = json.loads((root / domain["skills_registry"]).read_text(encoding="utf-8"))
        for skill in registry["skills"]:
            records[skill["id"]] = {"domain": domain["id"], **skill}
    return records


def describe(skill_id, records):
    if skill_id not in records:
        raise ValueError(f"Unknown skill: {skill_id}")
    ancestry = []
    visited = {skill_id}
    parent = records[skill_id].get("parent_skill")
    while parent:
        if parent in visited or parent not in records:
            raise ValueError("Invalid parent graph; run validate_registry.py")
        ancestry.append(parent)
        visited.add(parent)
        parent = records[parent].get("parent_skill")
    return {
        "skill": skill_id,
        "domain": records[skill_id]["domain"],
        "ancestry": list(reversed(ancestry)),
        "children": sorted(name for name, node in records.items()
                           if node.get("parent_skill") == skill_id),
        "related_skills": records[skill_id].get("related_skills", []),
        "path": records[skill_id]["path"],
    }


def main():
    parser = argparse.ArgumentParser(description="Inspect graph metadata for one skill")
    parser.add_argument("skill_id")
    args = parser.parse_args()
    try:
        print(json.dumps(describe(args.skill_id, load_records()), indent=2))
    except ValueError as exc:
        parser.exit(2, f"{exc}\n")


if __name__ == "__main__":
    main()
