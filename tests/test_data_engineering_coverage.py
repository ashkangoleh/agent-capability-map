import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "apache-seatunnel-data-integration",
    "dask-distributed-data-engineering",
    "datafusion-arrow-query-engine",
    "apache-spark-declarative-pipelines",
    "risingwave-streaming-sql-engineering",
    "materialize-streaming-sql-engineering",
    "apache-fluss-streaming-storage",
    "ducklake-lakehouse-format-engineering",
    "starrocks-olap-warehouse-engineering",
    "nats-jetstream-data-streaming",
    "data-migration-cutover-reconciliation",
    "unstructured-data-ingestion-engineering",
    "snowflake-data-platform-engineering",
    "bigquery-data-platform-engineering",
    "redshift-data-platform-engineering",
    "databricks-lakeflow-data-engineering",
    "oci-data-platform-engineering",
    "data-orchestration-platform-selection",
    "openmetadata-catalog-operations",
}
EXPECTED_SCOPES = {
    "foundations", "ingestion", "batch-ingestion", "messaging", "streaming",
    "distributed-processing", "orchestration", "transformation", "formats",
    "storage", "lakehouse", "warehouse", "data-observability", "quality",
    "governance", "dataops", "reliability", "performance", "cloud", "serving",
    "data-migration", "unstructured-data", "architecture",
}


class DataEngineeringCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = Router(ROOT)
        cls.cases = load_yaml(ROOT, "tests/fixtures/yaml-routing-cases.yaml")["cases"]

    def test_data_engineering_has_canonical_first_class_scopes(self):
        graph = load_yaml(ROOT, "domains/data/data-engineering/map.yaml")
        self.assertEqual({item["id"] for item in graph["children"]}, EXPECTED_SCOPES)
        for item in graph["children"]:
            self.assertEqual(item["status"], "active")
            self.assertTrue(item.get("map") or item.get("skills"))

    def test_bare_data_engineering_domain_requests_clarification(self):
        result = self.router.resolve("Data Engineering")
        self.assertEqual(result["status"], "needs_clarification", result)

    def test_explicit_data_engineering_overview_uses_foundations(self):
        result = self.router.resolve("Data Engineering overview")
        self.assertEqual(result["status"], "matched", result)
        self.assertEqual(result["selected_skill"], "data-engineering-implementation", result)

    def test_generic_trigger_is_not_owned_by_distributed_processing(self):
        graph = load_yaml(ROOT, "domains/data/data-engineering/map.yaml")
        by_id = {item["id"]: item for item in graph["children"]}
        self.assertIn("data engineering overview", by_id["foundations"]["triggers"])
        self.assertNotIn("data engineering", by_id["distributed-processing"]["triggers"])
        self.assertNotIn("مهندسی داده", by_id["distributed-processing"]["triggers"])

    def test_all_new_data_engineering_specialists_route(self):
        cases = [item for item in self.cases if item["id"].startswith("de-specialist-")]
        self.assertEqual(len(cases), len(EXPECTED_SKILLS))
        selected = set()
        for case in cases:
            with self.subTest(case=case["id"]):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], case["skill"], result)
                self.assertLessEqual(len(result["inspected_files"]), 10)
                selected.add(result["selected_skill"])
        self.assertEqual(selected, EXPECTED_SKILLS)

    def test_new_skills_have_production_sections_and_references(self):
        for skill_id in EXPECTED_SKILLS:
            with self.subTest(skill=skill_id):
                case = next(
                    item for item in self.cases
                    if item["id"].startswith("de-specialist-") and item["skill"] == skill_id
                )
                result = self.router.resolve(case["request"])
                self.assertEqual(result["selected_skill"], skill_id, result)
                content = Path(result["skill_path"]).read_text(encoding="utf-8")
                for heading in ("## Activation boundary", "## Required inputs", "## Production workflow",
                                "## Failure modes and recovery", "## Validation and evidence", "## Official references"):
                    self.assertIn(heading, content)
                self.assertRegex(content, r"https://")

    def test_analytics_modeling_is_not_owned_by_data_engineering_warehouse(self):
        graph = load_yaml(ROOT, "domains/data/data-engineering/warehouse/map.yaml")
        self.assertNotIn("warehouse-modeling", {item["id"] for item in graph["children"]})
        result = self.router.resolve("Design dimensional modeling with fact table grain")
        self.assertEqual(result["selected_skill"], "dimensional-modeling-grain", result)

    def test_trino_generic_request_abstains_without_task_semantics(self):
        result = self.router.resolve("Design a Trino data pipeline")
        self.assertEqual(result["status"], "needs_clarification", result)
        self.assertNotIn("skill_path", result)


if __name__ == "__main__":
    unittest.main()
