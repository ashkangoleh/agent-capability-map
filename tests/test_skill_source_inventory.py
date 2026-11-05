"""Enforce a single domain-owned canonical source for every registered skill."""
import unittest
from collections import defaultdict
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / ".agents" / "skills"


class SkillSourceInventoryTests(unittest.TestCase):
    def test_registered_sources_match_physical_manifests(self):
        # Router.validate checks frontmatter, route graphs and registry identifiers.
        validated = Router(ROOT).validate()
        self.assertEqual(validated["status"], "valid")

        registered = defaultdict(set)
        owners = defaultdict(set)
        visited = set()

        def visit(map_path, domain):
            key = (map_path, domain)
            if key in visited:
                return
            visited.add(key)
            document = load_yaml(ROOT, map_path)
            for node in document.get("children", []):
                if node.get("map"):
                    visit(node["map"], domain)
                if not node.get("skills"):
                    continue
                registry = load_yaml(ROOT, node["skills"])
                for item in registry.get("skills", []):
                    if item.get("status") != "active":
                        continue
                    skill_id = item["id"]
                    path = Path(item["path"])
                    registered[skill_id].add(path.as_posix())
                    owners[skill_id].add(domain)

        top = load_yaml(ROOT, "catalog/root.yaml")
        for node in top["children"]:
            domain = node["id"]
            if node.get("map"):
                visit(node["map"], domain)
            if node.get("skills"):
                registry = load_yaml(ROOT, node["skills"])
                for item in registry.get("skills", []):
                    if item.get("status") == "active":
                        registered[item["id"]].add(Path(item["path"]).as_posix())
                        owners[item["id"]].add(domain)

        expected_files = set()
        for skill_id, paths in registered.items():
            with self.subTest(skill=skill_id):
                self.assertEqual(len(paths), 1, f"Conflicting source paths: {paths}")
                self.assertEqual(len(owners[skill_id]), 1, f"Cross-domain ownership: {owners[skill_id]}")
                relative = Path(next(iter(paths)))
                domain = next(iter(owners[skill_id]))
                self.assertEqual(relative.parts[:3], (".agents", "skills", domain))
                self.assertGreaterEqual(len(relative.parts), 6, f"Non-nested path: {relative}")
                self.assertEqual(relative.parts[-2:], (skill_id, "SKILL.md"))
                expected_files.add(relative.as_posix())

        manifests = [path.relative_to(ROOT).as_posix() for path in SKILL_ROOT.rglob("SKILL.md")]
        self.assertEqual(len(manifests), len(set(manifests)))
        self.assertEqual(set(manifests), expected_files, "Orphan or missing canonical SKILL.md")
        catalog = load_yaml(ROOT, "catalog/master-skill-ids.yaml")
        self.assertEqual(set(registered), set(catalog["ids"]))
        self.assertEqual(len(manifests), len(catalog["ids"]))


if __name__ == "__main__":
    unittest.main()
