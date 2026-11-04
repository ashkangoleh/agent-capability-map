import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "ds-forecast-origin-window",
    "ds-forecast-origin-availability",
    "ds-forecast-origin-weekly",
    "ds-forecast-origin-persian",
    "ds-forecast-quantile-crossing",
    "ds-forecast-quantile-pinball",
    "ds-forecast-quantile-coverage",
    "ds-forecast-quantile-persian",
    "ds-forecast-hierarchy-reconciliation",
    "ds-forecast-hierarchy-coherence",
    "ds-forecast-hierarchy-summing",
    "ds-forecast-hierarchy-persian",
    "ds-forecast-intermittent-croston",
    "ds-forecast-intermittent-stockout",
    "ds-forecast-intermittent-coldstart",
    "ds-forecast-intermittent-persian",
    "ds-forecast-existing-probabilistic",
    "ds-forecast-existing-intermittent",
    "ds-forecast-existing-hierarchy",
    "ds-forecast-nearmiss-conformal",
    "ds-forecast-nearmiss-features",
    "ds-forecast-nearmiss-dense",
}
SPECIALISTS = {
    "time-series-forecast-backtesting",
    "ds-probabilistic-forecasting",
    "ds-hierarchical-forecasting",
    "ds-intermittent-demand-forecasting",
}


class ForecastRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = Router(ROOT)
        cls.cases = load_yaml(ROOT, "tests/fixtures/yaml-routing-cases.yaml")["cases"]

    def test_forecast_routes_and_near_misses(self):
        cases = [case for case in self.cases if case["id"].startswith("ds-forecast-")]
        self.assertEqual({case["id"] for case in cases}, EXPECTED)
        for case in cases:
            with self.subTest(case=case["id"]):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], case["skill"], result)
                self.assertLessEqual(len(result["inspected_files"]), 12, result)
                self.assertTrue(result["skill_path"].endswith("/SKILL.md"), result)
                if "nearmiss-conformal" in case["id"] or "nearmiss-features" in case["id"]:
                    self.assertNotIn(result["selected_skill"], SPECIALISTS)

    def test_existing_four_specialists_not_duplicated(self):
        ids = load_yaml(ROOT, "catalog/master-skill-ids.yaml")["ids"]
        self.assertTrue(SPECIALISTS.issubset(ids))
        for skill_id in SPECIALISTS:
            self.assertEqual(ids.count(skill_id), 1)
        advanced = load_yaml(ROOT, "domains/data/data-science/forecasting/skills.yaml")
        classic = load_yaml(ROOT, "domains/data/data-science/forecast/skills.yaml")
        observed = {s["id"] for s in advanced["skills"] + classic["skills"]}
        self.assertEqual(observed, SPECIALISTS)

    def test_production_contracts_and_executable_checker(self):
        markers = {
            "time-series-forecast-backtesting": ["rolling_origin_splits", "label", "gap"],
            "ds-probabilistic-forecasting": ["quantile_forecast_report", "pinball", "crossing"],
            "ds-hierarchical-forecasting": ["hierarchy_coherence_report", "summing matrix", "probabilistic"],
            "ds-intermittent-demand-forecasting": ["intermittent_demand_profile", "stockout", "lead-time"],
        }
        for skill_id, required in markers.items():
            with self.subTest(skill=skill_id):
                content = (ROOT / ".agents" / "skills" / skill_id / "SKILL.md").read_text(encoding="utf-8").casefold()
                for phrase in required:
                    self.assertIn(phrase.casefold(), content)
                self.assertIn("## Failure modes and abstention".casefold(), content)
                self.assertIn("## Output contract".casefold(), content)
        self.assertTrue((ROOT / "examples/data_science/forecast_integrity.py").is_file())


if __name__ == "__main__":
    unittest.main()
