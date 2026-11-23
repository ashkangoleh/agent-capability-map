#!/usr/bin/env python3
"""Compatibility entry point: validate the authoritative YAML graph, not archived JSON."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from capability_map import Router, RouterError


def main():
    result = Router(ROOT).validate()
    print(
        "Validation passed: "
        f"{result['maps']} YAML maps, "
        f"{result['nodes']} nodes, "
        f"{result['unique_active_skills']} active skills, "
        f"{result['cross_domain_relations']} cross-domain relationships."
    )


if __name__ == "__main__":
    try:
        main()
    except (RouterError, OSError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
