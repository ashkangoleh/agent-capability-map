"""Deterministic AI/ML quality fixture runner. Does not evaluate LLM answers."""
import json
import tempfile
from pathlib import Path

from capability_map import Router
from capability_map.domain_selection import update_domain_selection
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]


def evaluate():
    cases = load_yaml(ROOT, "tests/fixtures/ai-ml-quality-cases.yaml")["cases"]
    if len(cases) != 55 or len({c["id"] for c in cases}) != 55:
        raise ValueError("Expected 55 unique AI/ML quality cases")
    results = []
    for case in cases:
        actual = Router(ROOT).resolve(case["request"])
        passed = actual["status"] == case["status"]
        if case.get("route"):
            passed = passed and actual["route"] == case["route"]
        if case.get("domain"):
            passed = passed and actual["route"][:1] == [case["domain"]]
        if case.get("skill"):
            passed = passed and actual.get("selected_skill") == case["skill"]
        if case["category"] == "natural-intent":
            passed = passed and len(actual.get("role_paths", [])) == 3
        results.append({
            "id": case["id"], "group": case["category"], "passed": passed,
            "expected_status": case["status"], "actual_status": actual["status"],
            "expected_skill": case.get("skill"), "actual_skill": actual.get("selected_skill"),
            "actual_route": actual["route"],
        })
    with tempfile.TemporaryDirectory() as directory:
        home = Path(directory)
        update_domain_selection(
            ROOT, home, ["ai-ml/llm-engineering"], apply=True
        )
        allowed = Router(ROOT, home=home).resolve(
            "Please help me llm schema validated json response for a production project"
        )
        denied = Router(ROOT, home=home).resolve(
            "Please help me rag enforce tenant permissions before retrieval for a production project"
        )
        passed = (
            allowed["status"] == "matched"
            and allowed.get("selected_skill") == "aiml-llm-structured-generation"
            and denied["status"] == "domain_not_enabled"
            and "role_paths" not in denied
        )
        results.append({
            "id": "scope-deny-sibling",
            "group": "scope-isolation",
            "passed": passed,
            "expected_status": "domain_not_enabled",
            "actual_status": denied["status"],
            "actual_route": denied["route"],
        })
    summary = {
        group: {
            "total": sum(r["group"] == group for r in results),
            "passed": sum(r["group"] == group and r["passed"] for r in results),
        }
        for group in sorted({r["group"] for r in results})
    }
    return {
        "scope": "lexical_router_regression_not_agent_output_quality",
        "status": "PASS" if all(r["passed"] for r in results) else "FAIL",
        "summary": summary,
        "failures": [r for r in results if not r["passed"]],
    }


def main():
    result = evaluate()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
