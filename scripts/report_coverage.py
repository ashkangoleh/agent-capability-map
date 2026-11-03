"""Compute live YAML domain-to-skill coverage without trusting stale README counts."""

import argparse
import json
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]


def compute_coverage(root=ROOT):
    root = Path(root).resolve()
    structural = Router(root).validate()
    master = load_yaml(root, "catalog/root.yaml")
    domains = []

    for domain in master["children"]:
        if not domain.get("map"):
            continue
        pending = [domain["map"]]
        seen_maps = set()
        active_nodes = 0
        mapped_nodes = 0
        discovered_skills = set()

        while pending:
            path = pending.pop()
            if path in seen_maps:
                continue
            seen_maps.add(path)
            document = load_yaml(root, path)
            for child in document.get("children", []):
                if child.get("status") == "mapped":
                    mapped_nodes += 1
                if child.get("status") == "active":
                    active_nodes += 1
                if child.get("map"):
                    pending.append(child["map"])
                elif child.get("skills"):
                    registry = load_yaml(root, child["skills"])
                    for item in registry.get("skills", []):
                        if item.get("status") == "active":
                            discovered_skills.add(item["id"])

        domains.append({
            "id": domain["id"],
            "status": domain.get("status", "unknown"),
            "active_nodes": active_nodes,
            "mapped_only_nodes": mapped_nodes,
            "active_skill_count": len(discovered_skills),
            "active_skill_ids": sorted(discovered_skills),
        })

    report = {
        "domain_count": len(domains),
        "domains_with_active_skills": sum(x["active_skill_count"] > 0 for x in domains),
        "domains_without_active_skills": [x["id"] for x in domains if not x["active_skill_count"]],
        "unique_active_skills": structural["unique_active_skills"],
        "node_count": structural["nodes"],
        "map_count": structural["maps"],
        "mapped_only_subdomain_nodes": sum(x["mapped_only_nodes"] for x in domains),
        "scope": "structural-discovery-coverage-only",
        "domains": domains,
    }
    return report


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", action="store_true", help="Only emit global counters")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    report = compute_coverage(args.root)
    if args.summary:
        report.pop("domains")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["domains_without_active_skills"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
