import json
import os
import tempfile
import unittest
from unittest import mock
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

    def test_related_capabilities(self):
        graph = Router(ROOT)
        result = graph.related("data/data-engineering/distributed-processing/spark/pyspark")
        self.assertEqual(result["status"], "ok")
        self.assertTrue(any(e["relation"] == "runs_on" for e in result["relations"]))

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
            report = Router(ROOT, project=p, home=p).validate()
            self.assertEqual(report["registered_user_skills"], 1)
            result = Router(ROOT, project=p, home=p).resolve("Create an enterprise PySpark project")
            self.assertEqual(result.get("selected_skill"), "enterprise-spark", result)
            self.assertEqual(result.get("source"), "project")

    def test_registered_overlay_rejects_path_escape_even_when_not_selected(self):
        with tempfile.TemporaryDirectory() as workspace:
            p = Path(workspace)
            (p / "AGENTS.md").write_text(
                "<!-- capability-map: overlay=.capability-map.yaml -->", encoding="utf-8"
            )
            (p / ".capability-map.yaml").write_text(
                "schema_version: 1\nskills:\n"
                "  - id: unsafe-skill\n"
                "    path: ../outside/SKILL.md\n"
                "    route: [data]\n"
                "    triggers: [unsafe task]\n"
                "    status: active\n",
                encoding="utf-8",
            )
            with self.assertRaises(RouterError):
                Router(ROOT, project=p, home=p).validate()

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

    def test_claude_install_configures_readonly_skill_access_and_preserves_settings(self):
        with tempfile.TemporaryDirectory() as workspace:
            base = Path(workspace)
            home = base / "home"
            root = base / "master"
            config = home / ".claude"
            skills = root / ".agents" / "skills"
            skills.mkdir(parents=True)
            config.mkdir(parents=True)
            settings_path = config / "settings.json"
            settings_path.write_text(
                json.dumps({
                    "model": "existing-model",
                    "permissions": {
                        "allow": ["Bash(git status)"],
                        "deny": ["Bash(rm *)"],
                        "additionalDirectories": ["/existing/docs"],
                    },
                    "otherSetting": {"keep": True},
                }),
                encoding="utf-8",
            )

            result = install(["claude"], home, root=root, apply=True)[0]
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
            rule = f"Edit(//{skills.resolve().as_posix().lstrip('/')}/**)"
            self.assertIn(str(skills.resolve()), settings["permissions"]["additionalDirectories"])
            self.assertIn(rule, settings["permissions"]["deny"])
            self.assertEqual(settings["permissions"]["allow"], ["Bash(git status)"])
            self.assertIn("Bash(rm *)", settings["permissions"]["deny"])
            self.assertEqual(settings["model"], "existing-model")
            self.assertEqual(settings["otherSetting"], {"keep": True})
            self.assertTrue(result["permissions"]["applied"])
            self.assertTrue((config / "CLAUDE.md").is_file())

            repeated = install(["claude"], home, root=root, apply=True)[0]
            self.assertFalse(repeated["permissions"]["changed"])
            self.assertEqual(settings["permissions"]["additionalDirectories"].count(str(skills.resolve())), 1)
            self.assertEqual(settings["permissions"]["deny"].count(rule), 1)

    def test_claude_dry_run_does_not_create_files(self):
        with tempfile.TemporaryDirectory() as workspace:
            base = Path(workspace)
            home = base / "home"
            root = base / "master"
            (root / ".agents" / "skills").mkdir(parents=True)
            result = install(["claude"], home, root=root, apply=False)[0]
            self.assertTrue(result["changed"])
            self.assertTrue(result["permissions"]["changed"])
            self.assertFalse((home / ".claude").exists())

    def test_claude_invalid_settings_fail_before_any_write(self):
        with tempfile.TemporaryDirectory() as workspace:
            base = Path(workspace)
            home = base / "home"
            root = base / "master"
            config = home / ".claude"
            (root / ".agents" / "skills").mkdir(parents=True)
            config.mkdir(parents=True)
            (config / "settings.json").write_text("{ invalid", encoding="utf-8")
            with self.assertRaises(RouterError):
                install(["claude"], home, root=root, apply=True)
            self.assertFalse((config / "CLAUDE.md").exists())

    def test_claude_config_dir_environment_override(self):
        with tempfile.TemporaryDirectory() as workspace:
            base = Path(workspace)
            home = base / "home"
            config = base / "custom-claude-config"
            root = base / "master"
            (root / ".agents" / "skills").mkdir(parents=True)
            with mock.patch.dict(os.environ, {"CLAUDE_CONFIG_DIR": str(config)}):
                result = install(["claude"], home, root=root, apply=True)[0]
            self.assertEqual(result["path"], str(config.resolve() / "CLAUDE.md"))
            self.assertTrue((config / "settings.json").is_file())

    def test_claude_rejects_symlinked_skill_root(self):
        with tempfile.TemporaryDirectory() as workspace:
            base = Path(workspace)
            home = base / "home"
            root = base / "master"
            outside = base / "outside"
            outside.mkdir()
            (root / ".agents").mkdir(parents=True)
            (root / ".agents" / "skills").symlink_to(outside, target_is_directory=True)
            with self.assertRaises(RouterError):
                install(["claude"], home, root=root, apply=False)

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
