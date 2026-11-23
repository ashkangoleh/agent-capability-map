"""Deterministic routing regression evaluation (not a model-level or token benchmark)."""

import json
from pathlib import Path

import yaml

from capability_map import Router

ROOT = Path(__file__).resolve().parents[1]


def main():
    path = ROOT / "tests" / "fixtures" / "yaml-routing-cases.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    cases = doc["cases"]
    results = []
    for case in cases:
        actual = Router(ROOT).resolve(case["request"])
        passed = actual["status"] == case["status"]
        if "skill" in case:
            passed = passed and actual.get("selected_skill") == case["skill"]
        results.append({
            "case": case["id"],
            "passed": passed,
            "actual_status": actual["status"],
            "actual_skill": actual.get("selected_skill"),
            "inspected_yaml_documents": len(actual["inspected_files"]),
        })
    passed = sum(item["passed"] for item in results)
    result = {
        "status": "passed" if passed == len(results) else "failed",
        "scope": "deterministic_lexical_router_only",
        "total": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "cases": results,
    }
    print(json.dumps(result, indent=2))
    if passed != len(results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
