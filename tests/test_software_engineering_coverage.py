"""Software Engineering hierarchical routing, role contracts and source coverage."""
import tempfile
import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml, role_contract_path, role_paths_for_route

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "software-engineering"


class SoftwareEngineeringHierarchyTests(unittest.TestCase):
    def test_complete_active_graph_has_independent_ancestor_and_leaf_roles(self):
        root = load_yaml(ROOT, "domains/software-engineering/map.yaml")
        self.assertEqual(root["id"], DOMAIN)
        self.assertEqual(len(root["children"]), 15)
        expected = {DOMAIN}
        registered = {}
        leaf_count = 0
        for branch in root["children"]:
            with self.subTest(branch=branch["id"]):
                self.assertEqual(branch["status"], "active")
                self.assertIn("map", branch)
                self.assertNotIn("skills", branch)
                branch_route = f"{DOMAIN}/{branch['id']}"
                expected.add(branch_route)
                path = role_contract_path(ROOT, branch_route)
                self.assertTrue(path.is_file())
                children = load_yaml(ROOT, branch["map"])
                self.assertEqual(children["id"], branch["id"])
                for capability in children["children"]:
                    leaf_count += 1
                    with self.subTest(capability=capability["id"]):
                        self.assertEqual(capability["status"], "active")
                        self.assertIn("skills", capability)
                        self.assertNotIn("map", capability)
                        route = f"{branch_route}/{capability['id']}"
                        expected.add(route)
                        self.assertEqual(len(role_paths_for_route(ROOT, route)), 3)
                        role_contract_path(ROOT, route)
                        registry = load_yaml(ROOT, capability["skills"])
                        self.assertEqual(len(registry["skills"]), 1)
                        item = registry["skills"][0]
                        self.assertEqual(item["status"], "active")
                        self.assertNotIn(item["id"], registered)
                        registered[item["id"]] = item["path"]
                        self.assertTrue((ROOT / item["path"]).is_file())
                        self.assertLessEqual(
                            sum(Path(p).stat().st_size for p in role_paths_for_route(ROOT, route)),
                            8192,
                        )
        actual_roles = {
            file.parent.relative_to(ROOT / "domains").as_posix()
            for file in (ROOT / "domains/software-engineering").rglob("ROLE.md")
        }
        self.assertEqual(actual_roles, expected, "Missing or orphaned domain roles")
        self.assertEqual(len(actual_roles), 68)
        self.assertEqual(leaf_count, 52)
        self.assertEqual(len(registered), 52)
        self.assertEqual(
            registered["software-engineering-implementation"],
            ".agents/skills/software-engineering/core/software-engineering-implementation/SKILL.md",
        )
        self.assertEqual(
            len([file for file in (ROOT / ".agents/skills/software-engineering").rglob("SKILL.md")]),
            52,
        )
        self.assertEqual(Router(ROOT).validate()["status"], "valid")

    def test_every_leaf_has_positive_deterministic_fixture_and_three_role_layers(self):
        cases = load_yaml(ROOT, "tests/fixtures/yaml-routing-cases.yaml")["cases"]
        chosen = [case for case in cases if case["id"].startswith("swe-hier-")]
        self.assertEqual(len(chosen), 52)
        self.assertEqual(len({case["id"] for case in chosen}), 52)
        for case in chosen:
            with self.subTest(case=case["id"]):
                result = Router(ROOT).resolve(case["request"])
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["source"], "master")
                self.assertEqual(result["selected_skill"], case["skill"], result)
                self.assertEqual(len(result["route"]), 3, result)
                self.assertEqual(result["route"][0], DOMAIN, result)
                self.assertEqual(len(result["role_paths"]), 3, result)
                self.assertTrue(all(Path(file).is_file() for file in result["role_paths"]))
                self.assertLessEqual(len(result["inspected_files"]), 6)
                self.assertEqual(result["role_path"], result["role_paths"][0])

    def test_old_api_endpoint_routing_and_skill_content_contract(self):
        result = Router(ROOT).resolve("Implement an API endpoint that emits SEO metadata")
        self.assertEqual(result["status"], "matched", result)
        self.assertEqual(result["selected_skill"], "software-engineering-implementation")
        self.assertEqual(result["route"], [
            "software-engineering", "backend", "api-implementation"
        ])
        source = ROOT / ".agents/skills/software-engineering/core/software-engineering-implementation/SKILL.md"
        self.assertEqual(Path(result["skill_path"]), source)
        self.assertIn("Deliver correct, maintainable software changes", source.read_text("utf-8"))

    def test_security_threat_model_keeps_security_domain_ownership(self):
        result = Router(ROOT).resolve(
            "Review application security threat modeling for an API"
        )
        self.assertEqual(result["status"], "matched", result)
        self.assertEqual(result["selected_skill"], "security-threat-model-review", result)
        self.assertEqual(result["route"][0], "security", result)

    def test_domain_scoping_blocks_sibling_and_keeps_data_in_own_domain(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            config = home / ".config/agent-capability-map"
            config.mkdir(parents=True)
            (config / "domains.yaml").write_text(
                "schema_version: 1\ndomains:\n  - software-engineering/backend\n",
                encoding="utf-8",
            )
            allowed = Router(ROOT, home=home).resolve(
                "software engineering service integration retry budget"
            )
            self.assertEqual(allowed["status"], "matched", allowed)
            self.assertEqual(allowed["route"][1], "backend")
            denied = Router(ROOT, home=home).resolve(
                "software engineering react component state architecture"
            )
            self.assertEqual(denied["status"], "domain_not_enabled", denied)
            self.assertNotIn("role_paths", denied)
        data = Router(ROOT).resolve("Create a new PySpark project")
        self.assertEqual(data["selected_skill"], "pyspark-project-bootstrap")
        self.assertEqual(data["route"][0], "data")


if __name__ == "__main__":
    unittest.main()
