import json
import tempfile
import unittest
from pathlib import Path

from capability_map import Router, RouterError
from capability_map.install import install

ROOT = Path(__file__).resolve().parents[1]


class GraphRoutingTests(unittest.TestCase):
    def test_graph_validation(self):
        report = Router(ROOT).validate()
        self.assertEqual(report["status"], "valid")
        self.assertGreaterEqual(report["maps"], 35)
        self.assertGreaterEqual(report["unique_active_skills"], 18)

    def test_pyspark_project_routing(self):
        result = Router(ROOT).resolve("Create a new PySpark project")
        self.assertEqual(result["status"], "matched", result)
        self.assertEqual(result["selected_skill"], "pyspark-project-bootstrap")
        self.assertEqual(result["route"], ["data", "data-engineering", "distributed-processing", "spark", "pyspark"])
        self.assertLessEqual(len(result["inspected_files"]), 6)

    def test_pyspark_transformations(self):
        result = Router(ROOT).resolve("Write PySpark DataFrame joins")
        self.assertEqual(result.get("selected_skill"), "pyspark-transformations", result)

    def test_pyspark_performance(self):
        result = Router(ROOT).resolve("Diagnose PySpark shuffle and spill")
        self.assertEqual(result.get("selected_skill"), "spark-performance-diagnostics", result)

    def test_airflow(self):
        result = Router(ROOT).resolve("Create an Airflow DAG with retries")
        self.assertEqual(result.get("selected_skill"), "airflow-dag-engineering", result)

    def test_kafka(self):
        result = Router(ROOT).resolve("Review Kafka consumer offsets and ordering")
        self.assertEqual(result.get("selected_skill"), "kafka-streaming-reliability", result)

    def test_other_domains(self):
        cases = [
            ("Write a product PRD", "product-discovery-prd"),
            ("Audit technical SEO canonical tags", "seo-audit-strategy"),
            ("Create marketing campaign strategy", "marketing-strategy-campaign"),
            ("Review a Kubernetes Helm upgrade", "platform-operations"),
        ]
        for task, skill_id in cases:
            with self.subTest(task=task):
                result = Router(ROOT).resolve(task)
                self.assertEqual(result.get("selected_skill"), skill_id, result)

    def test_unavailable_not_invented(self):
        result = Router(ROOT).resolve("Analyze modern chemistry experiments")
        self.assertIn(result["status"], ["unavailable", "needs_clarification"], result)
        self.assertNotIn("skill_path", result)

    def test_ambiguous_spark_api(self):
        result = Router(ROOT).resolve("Create a Spark project")
        self.assertEqual(result["status"], "needs_clarification", result)
        self.assertNotIn("skill_path", result)

    def test_unmatched_abstains(self):
        result = Router(ROOT).resolve("Random unknown zqvx speciality")
        self.assertEqual(result["status"], "unmatched")
        self.assertNotIn("skill_path", result)

    def test_registered_project_skill_coexists(self):
        with tempfile.TemporaryDirectory() as workspace:
            p = Path(workspace)
            (p / "AGENTS.md").write_text("<!-- capability-map: overlay=.capability-map.yaml -->", encoding="utf-8")
            (p / ".capability-map.yaml").write_text(
                "schema_version: 1\nskills:\n"
                "  - id: enterprise-spark\n"
                "    path: skills/enterprise-spark/SKILL.md\n"
                "    triggers: [enterprise pyspark project]\n"
                "    route: [data, data-engineering, spark, pyspark]\n"
                "    status: active\n",
                encoding="utf-8",
            )
            s = p / "skills" / "enterprise-spark" / "SKILL.md"
            s.parent.mkdir(parents=True)
            s.write_text(
                "---\nname: enterprise-spark\n"
                "description: Use for enterprise PySpark projects with organization-specific requirements.\n"
                "---\n\nInspect company constraints before code generation.\n",
                encoding="utf-8",
            )
            result = Router(ROOT, project=p, home=p).resolve("Create an enterprise PySpark project")
            self.assertEqual(result.get("selected_skill"), "enterprise-spark", result)
            self.assertEqual(result.get("source"), "project")

    def test_unregistered_project_skill_is_ignored(self):
        with tempfile.TemporaryDirectory() as workspace:
            p = Path(workspace)
            (p / ".capability-map.yaml").write_text(
                "skills:\n  - id: enterprise-spark\n    path: bad/SKILL.md\n    triggers: [enterprise pyspark project]\n",
                encoding="utf-8",
            )
            result = Router(ROOT, project=p, home=p).resolve("Create an enterprise PySpark project")
            self.assertNotEqual(result.get("selected_skill"), "enterprise-spark")

    def test_project_path_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as workspace:
            p = Path(workspace)
            (p / "AGENTS.md").write_text(
                "<!-- capability-map: overlay=../../secret.yaml -->", encoding="utf-8"
            )
            with self.assertRaises(RouterError):
                Router(ROOT, project=p, home=p).resolve("Create a new PySpark project")

    def test_global_install_preview_preserves_files(self):
        with tempfile.TemporaryDirectory() as workspace:
            p = Path(workspace)
            target = p / ".codex" / "AGENTS.md"
            target.parent.mkdir(parents=True)
            target.write_text("# Existing user instructions\n", encoding="utf-8")
            dry = install(["codex", "cursor"], p, apply=False)
            self.assertTrue(dry[0]["changed"])
            self.assertEqual(target.read_text(encoding="utf-8"), "# Existing user instructions\n")
            self.assertFalse((p / ".cursor").exists())
            install(["codex", "cursor"], p, apply=True)
            self.assertIn("# Existing user instructions", target.read_text(encoding="utf-8"))
            cursor = p / ".cursor" / "skills" / "master-capability-router" / "SKILL.md"
            self.assertTrue(cursor.read_text(encoding="utf-8").startswith("---\n"))
            install(["codex", "cursor"], p, apply=True)
            self.assertEqual(target.read_text(encoding="utf-8").count("<!-- capability-map:managed:start -->"), 1)


if __name__ == "__main__":
    unittest.main()
