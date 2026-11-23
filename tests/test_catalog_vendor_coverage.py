import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"nessie-versioned-catalog-operations", "gravitino-federated-catalog-operations"}
CASE_IDS = {
    "de-catalog-vendor-nessie-branches",
    "de-catalog-vendor-nessie-conflict",
    "de-catalog-vendor-nessie-rest",
    "de-catalog-vendor-gravitino-metalake",
    "de-catalog-vendor-gravitino-federation",
    "de-catalog-vendor-gravitino-rest",
    "de-catalog-vendor-gravitino-persian",
}


class CatalogVendorCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = Router(ROOT)
        cls.cases = load_yaml(ROOT, "tests/fixtures/yaml-routing-cases.yaml")["cases"]

    def test_catalog_vendor_specialists_are_unique_and_registered(self):
        ids = load_yaml(ROOT, "catalog/master-skill-ids.yaml")["ids"]
        self.assertTrue(EXPECTED.issubset(ids))
        for skill in EXPECTED:
            self.assertEqual(ids.count(skill), 1)
        catalog = load_yaml(ROOT, "domains/data/data-engineering/lakehouse/catalogs/map.yaml")
        by_id = {child["id"]: child for child in catalog["children"]}
        for child_id, skill in (("nessie", "nessie-versioned-catalog-operations"),
                                ("gravitino", "gravitino-federated-catalog-operations")):
            with self.subTest(catalog=child_id):
                self.assertEqual(by_id[child_id]["status"], "active")
                registry = load_yaml(ROOT, by_id[child_id]["skills"])
                self.assertEqual([item["id"] for item in registry["skills"]], [skill])

    def test_route_cases(self):
        cases = [case for case in self.cases if case["id"].startswith("de-catalog-vendor-")]
        self.assertEqual({case["id"] for case in cases}, CASE_IDS)
        for case in cases:
            with self.subTest(case=case["id"]):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], case["skill"], result)
                self.assertLessEqual(len(result["inspected_files"]), 12, result)
                self.assertEqual(result["route"][:4],
                                 ["data", "data-engineering", "lakehouse", "catalogs"], result)

    def test_generic_rest_catalog_does_not_shadow_implementations(self):
        for name, skill in (
            ("Project Nessie", "nessie-versioned-catalog-operations"),
            ("Apache Gravitino", "gravitino-federated-catalog-operations"),
            ("Polaris", "polaris-iceberg-catalog-operations"),
            ("Lakekeeper", "lakekeeper-iceberg-catalog-operations"),
        ):
            with self.subTest(name=name):
                result = self.router.resolve(f"Review {name} Iceberg REST catalog credential vending")
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], skill, result)

    def test_production_skill_contracts(self):
        catalog = load_yaml(ROOT, "domains/data/data-engineering/lakehouse/catalogs/map.yaml")
        registered = {}
        for child in catalog["children"]:
            if child.get("skills"):
                for item in load_yaml(ROOT, child["skills"])["skills"]:
                    registered[item["id"]] = ROOT / item["path"]
        for name in EXPECTED:
            with self.subTest(skill=name):
                path = registered[name]
                content = path.read_text(encoding="utf-8")
                for heading in (
                    "## Activation boundary", "## Required inputs", "## Production workflow",
                    "## Failure modes and recovery", "## Validation and evidence",
                    "## Official references",
                ):
                    self.assertIn(heading, content)
                self.assertIn("https://", content)


if __name__ == "__main__":
    unittest.main()
