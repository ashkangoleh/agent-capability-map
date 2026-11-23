import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "ds-uncertainty-"
EXPECTED_CASE_IDS = {
    "ds-uncertainty-conformal-rank",
    "ds-uncertainty-conformal-marginal",
    "ds-uncertainty-conformal-subgroup",
    "ds-uncertainty-conformal-residual",
    "ds-uncertainty-conformal-persian",
    "ds-uncertainty-calibration-reliability",
    "ds-uncertainty-calibration-frozen",
    "ds-uncertainty-calibration-brier",
    "ds-uncertainty-calibration-persian",
    "ds-uncertainty-calibration-existing",
    "ds-uncertainty-forecast-near-miss",
    "ds-uncertainty-parameter-near-miss",
    "ds-uncertainty-bayesian-near-miss",
    "ds-uncertainty-conformal-existing",
    "ds-uncertainty-fairness-near-miss",
}


class DataScienceUncertaintyRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = Router(ROOT)
        cls.cases = load_yaml(ROOT, "tests/fixtures/yaml-routing-cases.yaml")["cases"]

    def test_conformal_calibration_and_hard_negative_cases(self):
        cases = [item for item in self.cases if item["id"].startswith(PREFIX)]
        self.assertEqual({case["id"] for case in cases}, EXPECTED_CASE_IDS)
        for case in cases:
            with self.subTest(case=case["id"]):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], case["status"], result)
                self.assertEqual(result.get("selected_skill"), case["skill"], result)
                self.assertLessEqual(len(result["inspected_files"]), 12, result)
                self.assertTrue(result["skill_path"].endswith("/SKILL.md"), result)

    def test_current_skills_are_not_duplicate_entries(self):
        index = load_yaml(ROOT, "catalog/master-skill-ids.yaml")["ids"]
        graph = load_yaml(ROOT, "domains/data/data-science/map.yaml")
        by_id = {node["id"]: node for node in graph["children"]}
        for node_name, skill_id in (
            ("model-validation", "ds-conformal-prediction-uncertainty"),
            ("modeling", "ds-model-calibration"),
        ):
            with self.subTest(skill=skill_id):
                self.assertEqual(index.count(skill_id), 1)
                self.assertEqual(by_id[node_name]["status"], "active")
                registry = load_yaml(ROOT, by_id[node_name]["skills"])
                items = [item for item in registry["skills"] if item["id"] == skill_id]
                self.assertEqual(len(items), 1)

    def test_precise_triggers_and_release_aware_skill_contract(self):
        graph = load_yaml(ROOT, "domains/data/data-science/map.yaml")
        by_id = {node["id"]: node for node in graph["children"]}
        self.assertIn("split conformal regression", by_id["model-validation"]["triggers"])
        self.assertIn("calibrated classifier cv", by_id["modeling"]["triggers"])
        for skill_id, phrases in (
            ("ds-conformal-prediction-uncertainty",
             ["## Production workflow", "## Failure modes and abstention",
              "## Runnable, bounded validation example", "k>n", "exchangeability"]),
            ("ds-model-calibration",
             ["## Production workflow", "## Failure modes and abstention",
              "## Runnable, bounded validation example", "FrozenEstimator",
              "scikit-learn 1.8"]),
        ):
            with self.subTest(skill=skill_id):
                category = "model-validation" if skill_id == "ds-conformal-prediction-uncertainty" else "modeling"
                registry = load_yaml(ROOT, f"domains/data/data-science/{category}/skills.yaml")
                path = next(item["path"] for item in registry["skills"] if item["id"] == skill_id)
                content = (ROOT / path).read_text(encoding="utf-8")
                for phrase in phrases:
                    self.assertIn(phrase.casefold(), content.casefold())
                self.assertIn("https://", content)


if __name__ == "__main__":
    unittest.main()
