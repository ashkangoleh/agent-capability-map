import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "ds-causal-exp-"
EXPECTED = {
    "ds-causal-exp-srm-assignment",
    "ds-causal-exp-ab-integrity",
    "ds-causal-exp-fixed-horizon",
    "ds-causal-exp-cluster",
    "ds-causal-exp-persian-srm",
    "ds-causal-exp-alpha-spending",
    "ds-causal-exp-continuous",
    "ds-causal-exp-early-stopping",
    "ds-causal-exp-identification",
    "ds-causal-exp-interference",
    "ds-causal-exp-observational-near-miss",
    "ds-causal-exp-data-analysis-near-miss",
}


class CausalExperimentationRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = Router(ROOT)
        cls.cases = load_yaml(ROOT, "tests/fixtures/yaml-routing-cases.yaml")["cases"]

    def test_positive_and_near_miss_cases(self):
        cases = [case for case in self.cases if case["id"].startswith(PREFIX)]
        self.assertEqual({case["id"] for case in cases}, EXPECTED)
        for case in cases:
            with self.subTest(case=case["id"]):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], case["status"], result)
                self.assertEqual(result.get("selected_skill"), case["skill"], result)
                self.assertLessEqual(len(result["inspected_files"]), 12, result)
                self.assertTrue(result["skill_path"].endswith("/SKILL.md"), result)

    def test_existing_specialists_are_reused_without_duplicate_ids(self):
        indexed = load_yaml(ROOT, "catalog/master-skill-ids.yaml")["ids"]
        graph = load_yaml(ROOT, "domains/data/data-science/map.yaml")
        entry = next(item for item in graph["children"] if item["id"] == "experimentation")
        registry = load_yaml(ROOT, entry["skills"])
        specialists = {
            "ds-ab-experimentation",
            "ds-causal-inference",
            "ds-sequential-experimentation",
        }
        self.assertEqual({item["id"] for item in registry["skills"]}, specialists)
        for skill in specialists:
            self.assertEqual(indexed.count(skill), 1)

    def test_skills_include_discriminative_validity_gates(self):
        expectations = {
            "ds-ab-experimentation": ("## Assignment integrity, SRM and exposure diagnostics",
                                      "assignment_integrity.py", "alpha=0.001"),
            "ds-causal-inference": ("## Identification gate and adversarial review",
                                    "unmeasured confounding", "identification table"),
            "ds-sequential-experimentation": ("## Interim-monitoring validity gate",
                                               "alpha-spending", "type-I"),
        }
        for skill_id, must_have in expectations.items():
            with self.subTest(skill=skill_id):
                registry = load_yaml(ROOT, "domains/data/data-science/experimentation/skills.yaml")
                path = ROOT / next(item["path"] for item in registry["skills"] if item["id"] == skill_id)
                text = path.read_text(encoding="utf-8")
                for required in must_have:
                    self.assertIn(required.casefold(), text.casefold())


if __name__ == "__main__":
    unittest.main()
