"""Validate the domain-nested canonical skill layout without implicit scans."""

import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = "domains/data/data-science/statistics-advanced/skills.yaml"
PREFIX = ".agents/skills/data/data-science/statistics-advanced/"
SKILLS = {
    "ds-power-sample-size",
    "ds-bayesian-pymc-stan",
    "ds-missing-data",
    "ds-robust-nonparametric-inference",
    "ds-multiple-testing-control",
    "ds-survey-sampling-design",
}


class DomainSkillLayoutTests(unittest.TestCase):
    def test_authoritative_registry_uses_nested_canonical_paths(self):
        document = load_yaml(ROOT, REGISTRY)
        entries = {item["id"]: item for item in document["skills"]}
        self.assertEqual(set(entries), SKILLS)
        all_paths = [entry["path"] for entry in entries.values()]
        self.assertEqual(len(all_paths), len(set(all_paths)))

        for name, entry in entries.items():
            with self.subTest(skill=name):
                path = entry["path"]
                self.assertEqual(path, f"{PREFIX}{name}/SKILL.md")
                self.assertTrue((ROOT / path).is_file())
                self.assertFalse((ROOT / ".agents" / "skills" / name / "SKILL.md").exists())
                body = (ROOT / path).read_text(encoding="utf-8")
                self.assertTrue(body.startswith("---\n"))
                self.assertIn(f"name: {name}\n", body)

    def test_hierarchical_routing_still_reaches_migrated_skills(self):
        router = Router(ROOT)
        tests = {
            "Data scientist: bayesian modeling pymc stan": "ds-bayesian-pymc-stan",
            "Data scientist: missing data mechanism imputation": "ds-missing-data",
            "Data scientist: complex survey sampling weights stratified cluster survey variance":
                "ds-survey-sampling-design",
            "Data scientist: robust nonparametric inference permutation test bootstrap confidence interval":
                "ds-robust-nonparametric-inference",
            "Data scientist: multiple hypothesis testing fdr false discovery rate correction":
                "ds-multiple-testing-control",
            "Data scientist: statistical power sample size": "ds-power-sample-size",
        }
        for request, skill in tests.items():
            with self.subTest(skill=skill):
                result = router.resolve(request)
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], skill, result)
                self.assertEqual(Path(result["skill_path"]), ROOT / f"{PREFIX}{skill}/SKILL.md")

    def test_every_data_science_registry_path_is_unique_and_owned(self):
        graph = load_yaml(ROOT, "domains/data/data-science/map.yaml")
        ids = set()
        paths = set()
        for node in graph["children"]:
            registry_path = node.get("skills")
            if not registry_path:
                continue
            registry = load_yaml(ROOT, registry_path)
            for entry in registry["skills"]:
                with self.subTest(skill=entry["id"]):
                    identity = entry["id"]
                    relative = entry["path"]
                    self.assertNotIn(identity, ids)
                    self.assertNotIn(relative, paths)
                    ids.add(identity)
                    paths.add(relative)
                    self.assertTrue(relative.startswith(".agents/skills/"))
                    self.assertEqual(Path(relative).name, "SKILL.md")
                    self.assertEqual(Path(relative).parent.name, identity)
                    target = ROOT / relative
                    self.assertTrue(target.is_file())
                    self.assertFalse(target.is_symlink())
        self.assertEqual(len(ids), 42)

    def test_master_ids_remain_unique_and_unchanged(self):
        index = load_yaml(ROOT, "catalog/master-skill-ids.yaml")["ids"]
        self.assertEqual(len(index), len(set(index)))
        self.assertTrue(SKILLS.issubset(index))


if __name__ == "__main__":
    unittest.main()
