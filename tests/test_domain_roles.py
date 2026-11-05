"""Domain role contracts are single-domain, matched-only output-review guidance."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from capability_map import Router
from capability_map.install import instruction_text
from capability_map.router import RouterError, role_contract_path, load_yaml

ROOT = Path(__file__).resolve().parents[1]


class DomainRoleTests(unittest.TestCase):
    def test_every_active_top_level_domain_has_one_valid_role(self):
        catalog = load_yaml(ROOT, "catalog/root.yaml")
        domains = [node["id"] for node in catalog["children"] if node["status"] == "active"]
        self.assertEqual(len(domains), 41)
        self.assertEqual(len(set(domains)), 41)
        for domain in domains:
            with self.subTest(domain=domain):
                path = role_contract_path(ROOT, domain)
                self.assertEqual(path, (ROOT / "domains" / domain / "ROLE.md").resolve())
                self.assertLessEqual(path.stat().st_size, 4096)
        self.assertEqual(
            {p.parent.name for p in (ROOT / "domains").glob("*/ROLE.md")},
            set(domains),
        )
        self.assertEqual(Router(ROOT).validate()["status"], "valid")

    def test_master_matched_roles_are_scoped(self):
        cases = [
            ("Create a new PySpark project", "data"),
            ("Infrastructure: falco runtime security detection", "infrastructure"),
            ("Write a product PRD", "product"),
            ("Audit technical SEO canonical tags", "seo"),
            ("Create marketing campaign strategy", "marketing"),
        ]
        for request, domain in cases:
            with self.subTest(domain=domain):
                with patch("capability_map.router.role_contract_path", wraps=role_contract_path) as called:
                    result = Router(ROOT).resolve(request)
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["source"], "master")
                self.assertEqual(result["route"][0], domain)
                self.assertEqual(Path(result["role_path"]), ROOT / "domains" / domain / "ROLE.md")
                self.assertGreaterEqual(called.call_count, 1)
                self.assertEqual(called.call_args_list[0].args[1], (domain,))
                self.assertEqual(Path(result["role_paths"][0]), Path(result["role_path"]))
                self.assertTrue(all(Path(path).is_file() for path in result["role_paths"]))
                self.assertNotIn(result["role_path"], result["inspected_files"])

    def test_denied_and_unmatched_return_no_role(self):
        result = Router(ROOT).resolve("Random unknown zqvx speciality")
        self.assertNotIn("role_path", result)
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            folder = home / ".config" / "agent-capability-map"
            folder.mkdir(parents=True)
            (folder / "domains.yaml").write_text(
                "schema_version: 1\ndomains:\n  - data/data-engineering\n", encoding="utf-8"
            )
            denied = Router(ROOT, home=home).resolve("Audit technical SEO canonical tags")
            self.assertEqual(denied["status"], "domain_not_enabled")
            self.assertNotIn("role_path", denied)
            self.assertNotIn("role_paths", denied)
            allowed = Router(ROOT, home=home).resolve("Create a new PySpark project")
            self.assertEqual(allowed["status"], "matched")
            self.assertEqual(Path(allowed["role_path"]).parent.name, "data")

    def test_personal_overlay_does_not_inherit_role(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            app = home / ".config" / "agent-capability-map"
            skill = app / "custom-overlay"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                "---\nname: custom-overlay\ndescription: A narrow user-owned workflow.\n---\n"
                "# Custom overlay\nThis is user-owned.\n", encoding="utf-8"
            )
            (app / "personal.yaml").write_text(
                "schema_version: 1\nskills:\n  - id: custom-overlay\n"
                "    path: custom-overlay/SKILL.md\n"
                "    triggers:\n      - unique private overlay marker yak\n"
                "    status: active\n    route:\n      - personal\n", encoding="utf-8"
            )
            result = Router(ROOT, home=home).resolve("unique private overlay marker yak")
            self.assertEqual(result["status"], "matched", result)
            self.assertEqual(result["source"], "personal")
            self.assertNotIn("role_path", result)
            self.assertNotIn("role_paths", result)

    def test_invalid_role_rejected(self):
        valid = (
            "---\nrole_id: data\nversion: \"1.0.0\"\ntitle: \"Data Reliability Review\"\n---\n"
            "## Decision lens\nA\n## Required evidence\nB\n## Review gates\nC\n"
            "## Rejection signals\nD\n## Output contract\nE\n## Authority boundary\nF\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "domains" / "data" / "ROLE.md"
            path.parent.mkdir(parents=True)
            path.write_text(valid, encoding="utf-8")
            self.assertEqual(role_contract_path(root, "data"), path.resolve())
            for content in (
                valid.replace("role_id: data", "role_id: security"),
                valid.replace("version: \"1.0.0\"", "version: \"2.0.0\""),
                valid.replace("## Review gates", "## Other gates"),
                valid.replace("title: \"Data Reliability Review\"", "role_id: wrong\ntitle: \"Data Reliability Review\""),
                "x" * 4097,
            ):
                with self.subTest(content=content[:35]):
                    path.write_text(content, encoding="utf-8")
                    with self.assertRaises(RouterError):
                        role_contract_path(root, "data")
            path.unlink()
            target = root / "safe.md"
            target.write_text(valid, encoding="utf-8")
            path.symlink_to(target)
            with self.assertRaises(RouterError):
                role_contract_path(root, "data")


    def test_data_engineering_pyspark_role_inheritance(self):
        expected = [
            "data",
            "data/data-engineering",
            "data/data-engineering/distributed-processing",
            "data/data-engineering/distributed-processing/spark",
            "data/data-engineering/distributed-processing/spark/pyspark",
        ]
        matched = Router(ROOT).resolve("Create a new PySpark project")
        self.assertEqual(matched["status"], "matched")
        self.assertEqual(matched["route"], expected[-1].split("/"))
        self.assertEqual(
            matched["role_paths"],
            [str(ROOT / "domains" / path / "ROLE.md") for path in expected],
        )
        self.assertEqual(matched["role_path"], matched["role_paths"][0])
        self.assertLessEqual(sum(Path(p).stat().st_size for p in matched["role_paths"]), 8192)

    def test_specialized_data_science_and_backfill_roles(self):
        cases = [
            ("Plan a pipeline backfill recovery for missing dates",
             "data/data-engineering/batch-ingestion/recovery"),
            ("Create an Airflow DAG with retries",
             "data/data-engineering/orchestration/airflow"),
            ("Review Kafka consumer offsets and ordering",
             "data/data-engineering/messaging/kafka"),
        ]
        for request, expected in cases:
            with self.subTest(request=request):
                result = Router(ROOT).resolve(request)
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["role_paths"][-1],
                                 str(ROOT / "domains" / expected / "ROLE.md"))
                self.assertEqual(result["role_paths"][0],
                                 str(ROOT / "domains/data/ROLE.md"))

    def test_role_scope_validation_and_symlinked_nested_parent(self):
        from capability_map.router import role_paths_for_route
        with self.assertRaises(RouterError):
            role_paths_for_route(ROOT, ("data", "..", "ROLE.md"))
        with self.assertRaises(RouterError):
            role_contract_path(ROOT, "data/../security")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "domains").mkdir()
            target = root / "outside"
            target.mkdir()
            (root / "domains/data").symlink_to(target, target_is_directory=True)
            with self.assertRaises(RouterError):
                role_contract_path(root, "data")

    def test_role_inheritance_does_not_override_profile(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            config = home / ".config/agent-capability-map"
            config.mkdir(parents=True)
            (config / "domains.yaml").write_text(
                "schema_version: 1\ndomains:\n  - data/data-engineering\n",
                encoding="utf-8",
            )
            allowed = Router(ROOT, home=home).resolve("Create a new PySpark project")
            self.assertEqual(allowed["status"], "matched")
            self.assertEqual(allowed["route"][:2], ["data", "data-engineering"])
            self.assertIn("data-engineering/ROLE.md", allowed["role_paths"][1])
            denied = Router(ROOT, home=home).resolve("Audit technical SEO canonical tags")
            self.assertEqual(denied["status"], "domain_not_enabled")
            self.assertNotIn("role_paths", denied)


    def test_complete_data_graph_role_inventory(self):
        """Every active logical Data route has one independently reviewable contract."""
        from capability_map.router import role_paths_for_route
        expected = {"data"}
        visited = set()

        def walk(map_path, route):
            if map_path in visited:
                self.fail(f"Data graph map visited twice without scoped contract: {map_path}")
            visited.add(map_path)
            graph = load_yaml(ROOT, map_path)
            for node in graph["children"]:
                if node.get("status") != "active":
                    continue
                scope = route + (node["id"],)
                name = "/".join(scope)
                expected.add(name)
                with self.subTest(route=name):
                    candidate = role_contract_path(ROOT, scope)
                    self.assertEqual(candidate, ROOT / "domains" / name / "ROLE.md")
                    self.assertLessEqual(candidate.stat().st_size, 4096)
                if node.get("map"):
                    walk(node["map"], scope)

        role_contract_path(ROOT, "data")
        walk("domains/data/map.yaml", ("data",))
        actual = {
            path.parent.relative_to(ROOT / "domains").as_posix()
            for path in (ROOT / "domains/data").rglob("ROLE.md")
        }
        self.assertEqual(actual, expected)
        self.assertEqual(len(expected), 127)
        self.assertEqual(len(visited), 21)
        deepest = Router(ROOT).resolve("Create a new PySpark project")
        self.assertEqual(len(deepest["role_paths"]), len(deepest["route"]))
        self.assertEqual(
            role_paths_for_route(ROOT, deepest["route"]), deepest["role_paths"]
        )

    def test_other_domains_still_inherit_root_without_sibling_roles(self):
        match = Router(ROOT).resolve("Write a product PRD")
        self.assertEqual(match["status"], "matched")
        self.assertEqual(match["route"][0], "product")
        self.assertEqual(match["role_paths"], [str(ROOT / "domains/product/ROLE.md")])

    def test_installer_mentions_roles_conditionally(self):
        instructions = instruction_text()
        self.assertIn("role_paths", instructions)
        self.assertIn("role_path", instructions)
        self.assertIn("skill_path", instructions)
        self.assertIn("domain_not_enabled", instructions)
        self.assertIn("no domain role", instructions)


if __name__ == "__main__":
    unittest.main()
