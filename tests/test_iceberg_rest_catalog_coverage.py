import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = "iceberg-rest-catalog-operations"
CASE_IDS = {
    "de-iceberg-rest-basic",
    "de-iceberg-rest-vending",
    "de-iceberg-rest-timeout",
    "de-iceberg-rest-discovery",
    "de-iceberg-rest-persian",
    "de-iceberg-rest-polaris",
    "de-iceberg-rest-lakekeeper",
    "de-iceberg-rest-schema-near-miss",
}


class IcebergRestCatalogCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = Router(ROOT)
        cls.cases = load_yaml(ROOT, "tests/fixtures/yaml-routing-cases.yaml")["cases"]

    def test_registered_once_in_master_index(self):
        ids = load_yaml(ROOT, "catalog/master-skill-ids.yaml")["ids"]
        self.assertEqual(ids.count(SKILL), 1)
        catalog = load_yaml(ROOT, "domains/data/data-engineering/lakehouse/catalogs/map.yaml")
        generic = next(item for item in catalog["children"] if item["id"] == "iceberg-rest")
        self.assertEqual(generic["status"], "active")
        self.assertEqual(generic["excludes"], ["polaris", "lakekeeper", "nessie", "gravitino"])
        registry = load_yaml(ROOT, generic["skills"])
        self.assertEqual([item["id"] for item in registry["skills"]], [SKILL])
        self.assertEqual(registry["skills"][0]["excludes"], ["polaris", "lakekeeper", "nessie", "gravitino"])

    def test_positive_and_boundary_cases(self):
        selected = [case for case in self.cases if case["id"].startswith("de-iceberg-rest-")]
        self.assertEqual({case["id"] for case in selected}, CASE_IDS)
        for case in selected:
            with self.subTest(case=case["id"]):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], case["status"], result)
                self.assertEqual(result.get("selected_skill"), case["skill"], result)
                self.assertLessEqual(len(result["inspected_files"]), 12, result)
                if case["skill"] == SKILL:
                    self.assertEqual(
                        result["route"],
                        ["data", "data-engineering", "lakehouse", "catalogs", "iceberg-rest"],
                        result,
                    )

    def test_generic_skill_has_operational_boundaries(self):
        catalog = load_yaml(ROOT, "domains/data/data-engineering/lakehouse/catalogs/map.yaml")
        generic = next(item for item in catalog["children"] if item["id"] == "iceberg-rest")
        registry = load_yaml(ROOT, generic["skills"])
        content = (ROOT / registry["skills"][0]["path"]).read_text(encoding="utf-8")
        for heading in (
            "## Activation boundary",
            "## Required inputs",
            "## Production workflow",
            "## Failure modes and recovery",
            "## Validation and evidence",
            "## Official references",
        ):
            self.assertIn(heading, content)
        for requirement in ("credential", "commit", "timeout", "401/403", "concurrent", "iceberg.apache.org"):
            self.assertIn(requirement, content.casefold())


if __name__ == "__main__":
    unittest.main()
