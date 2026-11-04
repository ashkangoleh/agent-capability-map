import unittest
from pathlib import Path

from capability_map import Router
from capability_map.domain_selection import discover_domains
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]

NEW_DATA_SCIENCE_SKILLS = {
    "ds-robust-nonparametric-inference",
    "ds-multiple-testing-control",
    "ds-survey-sampling-design",
    "ds-conformal-prediction-uncertainty",
    "ds-fairness-subgroup-evaluation",
    "ds-doubleml-causal-estimation",
    "ds-panel-econometrics",
    "ds-sequential-experimentation",
    "ds-probabilistic-forecasting",
    "ds-intermittent-demand-forecasting",
    "ds-multilingual-nlp-evaluation",
}


class DataScienceCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = Router(ROOT)
        cls.cases = load_yaml(ROOT, "tests/fixtures/yaml-routing-cases.yaml")["cases"]

    def test_new_specialists_have_positive_routes(self):
        cases = [case for case in self.cases if case["id"].startswith("ds-specialist-")]
        self.assertEqual(len(cases), len(NEW_DATA_SCIENCE_SKILLS))
        actual = set()
        for case in cases:
            with self.subTest(case=case["id"]):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], case["skill"], result)
                actual.add(result["selected_skill"])
        self.assertEqual(actual, NEW_DATA_SCIENCE_SKILLS)

    def test_near_misses_route_to_their_own_domain_specialist(self):
        cases = [case for case in self.cases if case["id"].startswith("ds-near-miss-")]
        self.assertEqual(len(cases), 5)
        for case in cases:
            with self.subTest(case=case["id"]):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], case["status"], result)
                self.assertEqual(result.get("selected_skill"), case["skill"], result)
                self.assertNotIn(result.get("selected_skill"), NEW_DATA_SCIENCE_SKILLS)

    def test_data_science_is_a_first_class_data_subdomain(self):
        scopes = discover_domains(ROOT, prefix="data")
        science = next(item for item in scopes if item["route"] == "data/data-science")
        self.assertEqual(science["kind"], "subdomain")
        self.assertEqual(science["active_skill_count"], 42)
        self.assertEqual(science["mapped_nodes"], 0)

    def test_data_root_scopes_and_distinct_science_triggers(self):
        graph = load_yaml(ROOT, "domains/data/map.yaml")
        children = graph["children"]
        self.assertEqual(len(children), 9)
        by_id = {child["id"]: child for child in children}
        self.assertEqual(len(by_id), len(children))
        science = by_id["data-science"]
        self.assertEqual(science["status"], "active")
        self.assertEqual(science["map"], "domains/data/data-science/map.yaml")
        self.assertEqual(len(science["triggers"]), len(set(science["triggers"])))

    def test_master_index_includes_all_new_specialists(self):
        index = set(load_yaml(ROOT, "catalog/master-skill-ids.yaml")["ids"])
        self.assertTrue(NEW_DATA_SCIENCE_SKILLS.issubset(index))
        self.assertGreaterEqual(len(index), 322)


if __name__ == "__main__":
    unittest.main()
