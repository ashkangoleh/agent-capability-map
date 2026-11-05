"""Validate AI/ML node ownership and deterministic routing."""
import tempfile
import unittest
from pathlib import Path
from capability_map import Router
from capability_map.router import load_yaml, role_contract_path, role_paths_for_route
ROOT = Path(__file__).resolve().parents[1]

class AIMLHierarchyTests(unittest.TestCase):
    def test_complete_active_inventory(self):
        root = load_yaml(ROOT, "domains/ai-ml/map.yaml")
        self.assertEqual(len(root["children"]), 12)
        actual = {"ai-ml"}
        ids = set()
        leaves = 0
        for branch in root["children"]:
            self.assertEqual(branch["status"], "active")
            self.assertIn("map", branch)
            route = "ai-ml/" + branch["id"]
            actual.add(route)
            role_contract_path(ROOT, route)
            detail = load_yaml(ROOT, branch["map"])
            self.assertEqual(detail["id"], branch["id"])
            for item in detail["children"]:
                if item["status"] != "active":
                    continue
                leaves += 1
                r = route + "/" + item["id"]
                actual.add(r)
                chain = role_paths_for_route(ROOT, r)
                self.assertEqual(len(chain), 3)
                self.assertLessEqual(sum(Path(p).stat().st_size for p in chain), 8192)
                reg = load_yaml(ROOT, item["skills"])
                self.assertEqual(len(reg["skills"]), 1)
                skill = reg["skills"][0]
                self.assertNotIn(skill["id"], ids)
                ids.add(skill["id"])
                self.assertTrue((ROOT / skill["path"]).is_file())
        self.assertEqual(leaves, 66)
        expected = {p.parent.relative_to(ROOT / "domains").as_posix() for p in (ROOT / "domains/ai-ml").rglob("ROLE.md")}
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), 79)
        self.assertEqual(Router(ROOT).validate()["status"], "valid")

    def test_all_positive_specialists_match(self):
        fixtures = load_yaml(ROOT, "tests/fixtures/yaml-routing-cases.yaml")["cases"]
        cases = [x for x in fixtures if x["id"].startswith("ai-hier-")]
        self.assertEqual(len(cases), 43)
        for x in cases:
            with self.subTest(case=x["id"]):
                resolved = Router(ROOT).resolve(x["request"])
                self.assertEqual(resolved["status"], "matched", resolved)
                self.assertEqual(resolved["selected_skill"], x["skill"], resolved)
                self.assertEqual(resolved["route"][0], "ai-ml")
                self.assertEqual(len(resolved["role_paths"]), 3)
                self.assertLessEqual(len(resolved["inspected_files"]), 6)

    def test_non_ai_ownership_and_scope(self):
        pairs = [("Create a new PySpark project", "data", "pyspark-project-bootstrap"),
                 ("Create an agent skill registry", "agent-systems", "skill-authoring-validation"),
                 ("Review application security threat modeling for an API", "security", "security-threat-model-review")]
        for request, domain, skill in pairs:
            with self.subTest(domain=domain):
                r = Router(ROOT).resolve(request)
                self.assertEqual(r["route"][0], domain)
                self.assertEqual(r["selected_skill"], skill)
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            conf = home / ".config/agent-capability-map"
            conf.mkdir(parents=True)
            (conf / "domains.yaml").write_text("schema_version: 1\\ndomains:\\n  - ai-ml/llm-engineering\\n", encoding="utf-8")
            allowed = Router(ROOT, home=home).resolve("Design and evaluate llm json schema constrained decoding")
            self.assertEqual(allowed["status"], "matched", allowed)
            denied = Router(ROOT, home=home).resolve("Design and evaluate rag document level acl enforcement")
            self.assertEqual(denied["status"], "domain_not_enabled", denied)
            self.assertNotIn("role_paths", denied)

if __name__ == "__main__":
    unittest.main()
