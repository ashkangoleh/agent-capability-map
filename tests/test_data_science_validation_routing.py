import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "ds-validation-"
EXPECTED_CASES = {
    "ds-validation-underspecified-sklearn",
    "ds-validation-underspecified-scikit",
    "ds-validation-tool-only",
    "ds-validation-pipeline",
    "ds-validation-grouped",
    "ds-validation-temporal",
    "ds-validation-calendar",
    "ds-validation-persian",
    "ds-validation-feature-boundary",
    "ds-validation-conformal-boundary",
    "ds-validation-group-boundary",
}


class DataScienceValidationRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = Router(ROOT)
        cls.cases = load_yaml(ROOT, "tests/fixtures/yaml-routing-cases.yaml")["cases"]

    def test_routing_cases_and_abstention(self):
        cases = [item for item in self.cases if item["id"].startswith(PREFIX)]
        self.assertEqual({item["id"] for item in cases}, EXPECTED_CASES)
        for case in cases:
            with self.subTest(case=case["id"]):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], case["status"], result)
                self.assertEqual(result.get("selected_skill"), case.get("skill"), result)
                self.assertLessEqual(len(result["inspected_files"]), 12, result)
                if case["status"] == "matched":
                    self.assertTrue(result["skill_path"].endswith("/SKILL.md"), result)
                else:
                    self.assertNotIn("skill_path", result)

    def test_generic_sklearn_does_not_force_validation_skill(self):
        domain = load_yaml(ROOT, "domains/data/data-science/map.yaml")
        node = next(item for item in domain["children"] if item["id"] == "model-validation")
        registry = load_yaml(ROOT, node["skills"])
        skill = next(item for item in registry["skills"] if item["id"] == "sklearn-leakage-free-validation")

        self.assertNotIn("sklearn", node["triggers"])
        self.assertNotIn("scikit-learn", node["triggers"])
        self.assertNotIn("scikit-learn", skill["triggers"])
        self.assertIn("sklearn time series split", node["triggers"])
        self.assertIn("sklearn grouped cross validation", skill["triggers"])

    def test_skill_contains_actual_validation_contract_and_references(self):
        registry = load_yaml(ROOT, "domains/data/data-science/model-validation/skills.yaml")
        path = ROOT / next(item["path"] for item in registry["skills"]
                           if item["id"] == "sklearn-leakage-free-validation")
        content = path.read_text(encoding="utf-8")
        for heading in (
            "## Activation boundary",
            "## Required context",
            "## Production workflow",
            "## Executable split-contract example",
            "## Failure modes and recovery",
            "## Validation and evidence",
            "## Authoritative references",
        ):
            self.assertIn(heading, content)
        for requirement in ("GroupKFold", "TimeSeriesSplit", "label availability",
                            "nested CV", "examples/data_science/split_integrity.py"):
            self.assertIn(requirement, content)


if __name__ == "__main__":
    unittest.main()
