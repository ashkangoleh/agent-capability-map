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

    def test_pyspark_bootstrap_evidence_guardrails_exist(self):
        text = (ROOT / ".agents" / "skills" / "pyspark-project-bootstrap" / "SKILL.md").read_text(encoding="utf-8")
        for required in (
            "latest stable",
            "cluster release",
            "S3A rename",
            "idempotency",
            "atomic",
            "structure-only",
        ):
            with self.subTest(required=required):
                self.assertIn(required, text)

    def test_specialized_skills_have_routing_fixtures(self):
        import yaml

        fixtures = yaml.safe_load(
            (ROOT / "tests" / "fixtures" / "yaml-routing-cases.yaml").read_text(encoding="utf-8")
        )["cases"]
        specialized_ids = {
            "dbt-incremental-modeling",
            "data-quality-contracts",
            "pipeline-backfill-recovery",
            "spark-structured-streaming",
            "kubernetes-rollout-safety",
            "product-experiment-design",
            "product-metrics-instrumentation",
            "marketing-measurement-attribution",
            "seo-indexability-diagnostics",
            "seo-structured-data-validation",
            "agent-evaluation-suite",
            "content-editorial-brief",
        }
        covered = {case.get("skill") for case in fixtures}
        self.assertTrue(specialized_ids.issubset(covered), specialized_ids - covered)
        for case in fixtures:
            if case.get("skill") not in specialized_ids:
                continue
            with self.subTest(case=case["id"]):
                result = Router(ROOT).resolve(case["request"])
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], case["skill"], result)
                self.assertEqual(result["source"], "master")
                self.assertLessEqual(len(result["inspected_files"]), 7)
                skill = Path(result["skill_path"])
                self.assertTrue(skill.is_file())
                self.assertIn("## Authoritative references", skill.read_text(encoding="utf-8"))

    def test_cross_domain_specialists_and_mapped_abstentions(self):
        import yaml

        cases = yaml.safe_load(
            (ROOT / "tests" / "fixtures" / "yaml-routing-cases.yaml").read_text(encoding="utf-8")
        )["cases"]
        selected = [
            case for case in cases
            if case["id"] in {
                "security-threat-model",
                "recruiting-scorecard",
                "curriculum-outcomes",
                "budget-scenarios",
                "legal-evidence",
                "public-health-evidence",
                "science-experiment",
                "ecommerce-catalog",
                "sales-forecast",
                "customer-support-kb",
                "podcast-brief",
                "game-design",
                "manufacturing-quality",
                "supply-demand",
                "bim-coordination",
                "carbon-inventory",
                "agri-data",
                "public-policy",
                "travel-planning",
                "fitness-training",
                "personal-productivity",
                "robotics-mapped",
                "telecom-mapped",
                "aerospace-mapped",
                "social-science-mapped",
                "humanities-mapped",
                "environment-mapped",
                "real-estate-mapped",
                "nonprofit-mapped",
                "robotics-ros2",
                "telecom-network-change",
                "aerospace-requirements",
                "social-survey",
                "humanities-history",
                "environment-biodiversity",
                "real-estate-due-diligence",
                "nonprofit-grant",
            }
        ]
        self.assertEqual(len(selected), 37)
        for case in selected:
            with self.subTest(case=case["id"]):
                result = Router(ROOT).resolve(case["request"])
                self.assertEqual(result["status"], case["status"], result)
                if case["status"] == "matched":
                    self.assertEqual(result["selected_skill"], case["skill"], result)
                    self.assertLessEqual(len(result["inspected_files"]), 8)
                    text = Path(result["skill_path"]).read_text(encoding="utf-8")
                    self.assertIn("## Required context", text)
                    self.assertIn("## Abstention and failure handling", text)
                    self.assertIn("## Evidence requirements", text)
                else:
                    self.assertNotIn("skill_path", result)


    def test_data_engineering_deep_skills(self):
        import yaml

        fixtures = yaml.safe_load(
            (ROOT / "tests" / "fixtures" / "yaml-routing-cases.yaml").read_text(encoding="utf-8")
        )["cases"]
        selected = [case for case in fixtures if case["id"].startswith("de-deep-") or case["id"].startswith("de-nearmiss-")]
        self.assertEqual(len(selected), 30)
        self.assertEqual(len({case["id"] for case in selected}), 30)
        self.assertEqual(len([case for case in selected if case["id"].startswith("de-deep-")]), 24)
        for case in selected:
            with self.subTest(case=case["id"]):
                result = Router(ROOT).resolve(case["request"])
                self.assertEqual(result["status"], case["status"], result)
                if case["status"] == "matched":
                    self.assertEqual(result.get("selected_skill"), case["skill"], result)
                    self.assertLessEqual(len(result["inspected_files"]), 9)
                    path = Path(result["skill_path"])
                    self.assertTrue(path.is_file())
                    if case["id"].startswith("de-deep-"):
                        text = path.read_text(encoding="utf-8")
                        self.assertIn("## Production procedure", text)
                        self.assertIn("## Evidence and", text)
                        self.assertIn("## ", text)
                else:
                    self.assertNotIn("skill_path", result)

    def test_data_engineering_remaining_engines(self):
        import yaml

        fixtures = yaml.safe_load(
            (ROOT / "tests" / "fixtures" / "yaml-routing-cases.yaml").read_text(encoding="utf-8")
        )["cases"]
        selected = [case for case in fixtures if case["id"].startswith("de-engine-")]
        self.assertEqual(len(selected), 5)
        for case in selected:
            with self.subTest(case=case["id"]):
                result = Router(ROOT).resolve(case["request"])
                self.assertEqual(result["status"], case["status"], result)
                self.assertEqual(result.get("selected_skill"), case["skill"], result)
                self.assertLessEqual(len(result["inspected_files"]), 9)
                path = Path(result["skill_path"])
                self.assertTrue(path.is_file())
                content = path.read_text(encoding="utf-8")
                self.assertIn("## Production procedure", content)
                self.assertIn("## Official or primary references", content)

    def test_reference_expansion_routing_coverage(self):
        import yaml

        fixtures = yaml.safe_load(
            (ROOT / "tests" / "fixtures" / "yaml-routing-cases.yaml").read_text(encoding="utf-8")
        )["cases"]
        selected = [case for case in fixtures if case["id"].startswith("ref-")]
        self.assertEqual(len(selected), 63)
        self.assertEqual(len({case["skill"] for case in selected}), 63)
        for case in selected:
            with self.subTest(case=case["id"]):
                actual = Router(ROOT).resolve(case["request"])
                self.assertEqual(actual["status"], "matched", actual)
                self.assertEqual(actual.get("selected_skill"), case["skill"], actual)
                self.assertLessEqual(len(actual["inspected_files"]), 10, actual)
                target = Path(actual["skill_path"])
                self.assertTrue(target.is_file())
                contents = target.read_text(encoding="utf-8")
                self.assertIn("## ", contents)
                self.assertTrue(
                    any(v in contents for v in ["## Procedure", "## Production workflow", "## Specialist procedure",
                                               "## Analysis and engineering workflow"]),
                    target,
                )

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

    def test_deep_data_engineering_graph_edges(self):
        graph = Router(ROOT)
        cases = [
            ("data/data-engineering/warehouse/trino", "iceberg", "uses"),
            ("data/data-engineering/distributed-processing/flink", "kafka", "uses"),
            ("data/analytics-engineering/dbt", "airflow", "orchestrated_by"),
            ("data/data-governance/lineage", "airflow", "related_to"),
        ]
        for route, target, relation in cases:
            with self.subTest(route=route):
                result = graph.related(route)
                self.assertEqual(result["status"], "ok")
                self.assertTrue(any(
                    e["relation"] == relation and target in e["to"]
                    for e in result["relations"]
                ), result)

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
