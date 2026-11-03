#!/usr/bin/env python3
"""Validate the YAML coverage taxonomy. This is an authoring-time check only."""

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class TaxonomyValidationError(ValueError):
    pass


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str):
            raise TaxonomyValidationError("Non-string taxonomy key")
        if key in result:
            raise TaxonomyValidationError(f"Duplicate taxonomy key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    unique_mapping,
)


def validate_tree(node, path=()):
    if isinstance(node, dict):
        if not node:
            raise TaxonomyValidationError(f"Empty taxonomy branch: {'/'.join(path)}")
        count = 0
        for key, value in node.items():
            if not NAME.fullmatch(key):
                raise TaxonomyValidationError(f"Invalid node name at {'/'.join(path + (key,))}")
            count += validate_tree(value, path + (key,))
        return count
    if isinstance(node, list):
        if not node:
            raise TaxonomyValidationError(f"Empty taxonomy leaves: {'/'.join(path)}")
        seen = set()
        for item in node:
            if not isinstance(item, str) or not NAME.fullmatch(item):
                raise TaxonomyValidationError(f"Invalid capability under {'/'.join(path)}")
            if item in seen:
                raise TaxonomyValidationError(f"Duplicate capability {item} under {'/'.join(path)}")
            seen.add(item)
        return len(node)
    raise TaxonomyValidationError(f"Expected sub-branches or capability list at {'/'.join(path)}")



def validate_priorities(root, taxonomy):
    path = root / "catalog/phase1-priorities.yaml"
    with path.open(encoding="utf-8") as handle:
        priorities = yaml.load(handle, Loader=UniqueKeyLoader)
    if not isinstance(priorities, dict) or priorities.get("phase") != 1:
        raise TaxonomyValidationError("Invalid phase-one priority manifest")
    groups = priorities.get("priority_groups")
    if not isinstance(groups, list) or not groups:
        raise TaxonomyValidationError("Phase-one priorities are empty")
    ids = set()
    domain_ids = set(taxonomy["domains"])
    for group in groups:
        if not isinstance(group, dict):
            raise TaxonomyValidationError("Priority group must be a mapping")
        key = group.get("id")
        if not isinstance(key, str) or not NAME.fullmatch(key) or key in ids:
            raise TaxonomyValidationError(f"Invalid or duplicate priority group: {key}")
        ids.add(key)
        route = group.get("canonical_path")
        if not isinstance(route, list) or not route or not all(isinstance(x, str) for x in route):
            raise TaxonomyValidationError(f"{key}: invalid canonical_path")
        if route[0] not in domain_ids or group.get("registry_domain") != route[0]:
            raise TaxonomyValidationError(f"{key}: unknown or mismatched domain")
        node = taxonomy["domains"]
        for part in route:
            if not isinstance(node, dict) or part not in node:
                raise TaxonomyValidationError(f"{key}: broken taxonomy path {'/'.join(route)}")
            node = node[part]
        if not isinstance(node, dict) or group.get("coverage") != "partial":
            raise TaxonomyValidationError(f"{key}: expected mapped subtree and partial coverage")
        for child in group.get("subdomain_branches", []):
            if child not in node:
                raise TaxonomyValidationError(f"{key}: unknown infrastructure subdomain {child}")
        catalog = json.loads((root / "catalog/domains.json").read_text(encoding="utf-8"))
        domain = next((d for d in catalog["domains"] if d["id"] == route[0]), None)
        if domain is None or not domain.get("skills_registry"):
            raise TaxonomyValidationError(f"{key}: domain has no skill registry")
        registry = json.loads((root / domain["skills_registry"]).read_text(encoding="utf-8"))
        active = {s["id"] for s in registry["skills"] if s["status"] == "active"}
        requested = group.get("active_skills")
        if not isinstance(requested, list) or not requested or len(requested) != len(set(requested)):
            raise TaxonomyValidationError(f"{key}: invalid active skill list")
        unknown = set(requested) - active
        if unknown:
            raise TaxonomyValidationError(f"{key}: nonexistent or inactive skills: {sorted(unknown)}")
    return len(groups)

def validate(root=ROOT):
    path = root / "catalog/coverage-taxonomy.yaml"
    with path.open(encoding="utf-8") as handle:
        taxonomy = yaml.load(handle, Loader=UniqueKeyLoader)
    if not isinstance(taxonomy, dict):
        raise TaxonomyValidationError("Taxonomy must be a mapping")
    if taxonomy.get("readiness") != "mapped":
        raise TaxonomyValidationError("Coverage taxonomy must not imply implemented skills")
    with (root / "catalog/domains.json").open(encoding="utf-8") as handle:
        catalog = json.load(handle)
    registered = {item["id"] for item in catalog["domains"]}
    domains = taxonomy.get("domains")
    if not isinstance(domains, dict):
        raise TaxonomyValidationError("Missing domains mapping")
    if set(domains) != registered:
        missing = sorted(registered - set(domains))
        extra = sorted(set(domains) - registered)
        raise TaxonomyValidationError(f"Root mismatch: missing={missing}, extra={extra}")
    leaves = validate_tree(domains)
    priority_count = validate_priorities(root, taxonomy)
    print(f"Coverage taxonomy valid: {len(domains)} domains, {leaves} mapped capabilities, {priority_count} priority groups (not verified skills)")


if __name__ == "__main__":
    try:
        validate()
    except (OSError, yaml.YAMLError, ValueError) as exc:
        print(f"Coverage taxonomy validation failed: {exc}", file=sys.stderr)
        sys.exit(1)
