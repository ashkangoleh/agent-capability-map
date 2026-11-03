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
    print(f"Coverage taxonomy valid: {len(domains)} domains, {leaves} mapped capabilities (not verified skills)")


if __name__ == "__main__":
    try:
        validate()
    except (OSError, yaml.YAMLError, ValueError) as exc:
        print(f"Coverage taxonomy validation failed: {exc}", file=sys.stderr)
        sys.exit(1)
