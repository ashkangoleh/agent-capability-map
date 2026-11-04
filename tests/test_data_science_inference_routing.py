import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "ds-inference-"
EXPECTED = {
    "ds-inference-fdr-bh",
    "ds-inference-holm",
    "ds-inference-by",
    "ds-inference-fdr-persian",
    "ds-inference-survey-lonely",
    "ds-inference-survey-design",
    "ds-inference-survey-strata",
    "ds-inference-survey-persian",
    "ds-inference-rubin-pool",
    "ds-inference-mnar",
    "ds-inference-mcar-mar",
    "ds-inference-imputation-persian",
    "ds-inference-bootstrap-cluster",
    "ds-inference-permutation-paired",
    "ds-inference-bca",
    "ds-inference-bayesian-rhat",
    "ds-inference-bayesian-ppc",
    "ds-inference-bayesian-divergence",
    "ds-inference-nearmiss-ci",
    "ds-inference-nearmiss-conformal",
    "ds-inference-nearmiss-sequential",
    "ds-inference-nearmiss-feature",
}
SKILLS = {
    "ds-multiple-testing-control",
    "ds-survey-sampling-design",
    "ds-missing-data",
    "ds-robust-nonparametric-inference",
    "ds-bayesian-pymc-stan",
}


class InferenceSurveyRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = Router(ROOT)
        cls.cases = load_yaml(ROOT, "tests/fixtures/yaml-routing-cases.yaml")["cases"]

    def test_new_positive_bilingual_and_nearmiss_routes(self):
        cases = [case for case in self.cases if case["id"].startswith(PREFIX)]
        self.assertEqual({case["id"] for case in cases}, EXPECTED)
        for case in cases:
            with self.subTest(case=case["id"]):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], case["skill"], result)
                self.assertLessEqual(len(result["inspected_files"]), 12, result)
                self.assertTrue(result["skill_path"].endswith("/SKILL.md"), result)
                if case["id"].startswith("ds-inference-nearmiss-"):
                    self.assertNotIn(result["selected_skill"], SKILLS)

    def test_existing_specialists_are_not_duplicate_entries(self):
        ids = load_yaml(ROOT, "catalog/master-skill-ids.yaml")["ids"]
        reg = load_yaml(ROOT, "domains/data/data-science/statistics-advanced/skills.yaml")
        from_registry = {item["id"] for item in reg["skills"]}
        self.assertTrue(SKILLS.issubset(from_registry))
        for skill in SKILLS:
            self.assertEqual(ids.count(skill), 1)

    def test_skill_contracts_and_arithmetic_helper(self):
        words = {
            "ds-multiple-testing-control": ("## Error-control and family integrity gate", "adjust_pvalues"),
            "ds-survey-sampling-design": ("## Survey-design and variance gate", "survey_design_guard"),
            "ds-missing-data": ("## Imputation pooling integrity gate", "pool_scalar_imputations"),
            "ds-robust-nonparametric-inference": ("## Resampling validity and stopping gate", "paired"),
            "ds-bayesian-pymc-stan": ("## MCMC diagnostic and predictive-validity gate", "BFMI"),
        }
        for name, (heading, marker) in words.items():
            with self.subTest(skill=name):
                text = (ROOT / ".agents" / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
                self.assertIn(heading, text)
                self.assertIn(marker, text)
                self.assertIn("https://", text)
        self.assertTrue((ROOT / "examples/data_science/inference_integrity.py").is_file())


if __name__ == "__main__":
    unittest.main()
