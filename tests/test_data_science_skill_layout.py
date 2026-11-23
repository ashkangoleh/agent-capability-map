"""Guard canonical domain-nested source paths and explicit resolver behavior."""

import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ".agents/skills/data/data-science/"
MIGRATED = {
    "statistics-advanced": {
        "ds-power-sample-size",
        "ds-bayesian-pymc-stan",
        "ds-missing-data",
        "ds-robust-nonparametric-inference",
        "ds-multiple-testing-control",
        "ds-survey-sampling-design",
    },
    "foundations": {
        "ds-problem-framing",
        "ds-scientific-python",
        "ds-r-statistics",
        "ds-jupyter-reproducibility",
    },
}
ROUTING_REQUESTS = {
    "Data scientist: bayesian modeling pymc stan": "ds-bayesian-pymc-stan",
    "Data scientist: missing data mechanism imputation": "ds-missing-data",
    "Data scientist: complex survey sampling weights stratified cluster survey variance":
        "ds-survey-sampling-design",
    "Data scientist: robust nonparametric inference permutation test bootstrap confidence interval":
        "ds-robust-nonparametric-inference",
    "Data scientist: multiple hypothesis testing fdr false discovery rate correction":
        "ds-multiple-testing-control",
    "Data scientist: statistical power sample size": "ds-power-sample-size",
    "Data scientist: data science problem framing": "ds-problem-framing",
    "Data scientist: scientific python numerical computing": "ds-scientific-python",
    "Data scientist: r statistical computing workflow": "ds-r-statistics",
    "Data scientist: jupyter notebook reproducibility": "ds-jupyter-reproducibility",
}


class DomainSkillLayoutTests(unittest.TestCase):
    def test_migrated_registries_use_canonical_paths_without_flat_duplicates(self):
        for category, expected_ids in MIGRATED.items():
            with self.subTest(category=category):
                registry = load_yaml(
                    ROOT, f"domains/data/data-science/{category}/skills.yaml"
                )
                entries = {item["id"]: item for item in registry["skills"]}
                self.assertEqual(set(entries), expected_ids)
                self.assertEqual(
                    len({item["path"] for item in entries.values()}),
                    len(entries),
                )
                for skill_id, entry in entries.items():
                    with self.subTest(skill=skill_id):
                        expected = f"{PREFIX}{category}/{skill_id}/SKILL.md"
                        self.assertEqual(entry["path"], expected)
                        target = ROOT / expected
                        self.assertTrue(target.is_file())
                        self.assertFalse(target.is_symlink())
                        self.assertFalse(
                            (ROOT / ".agents" / "skills" / skill_id / "SKILL.md").exists()
                        )
                        body = target.read_text(encoding="utf-8")
                        self.assertTrue(body.startswith("---\n"))
                        self.assertIn(f"name: {skill_id}\n", body)

    def test_hierarchical_router_reaches_all_ten_migrated_skills(self):
        router = Router(ROOT)
        expected_paths = {
            skill_id: f"{PREFIX}{category}/{skill_id}/SKILL.md"
            for category, skill_ids in MIGRATED.items()
            for skill_id in skill_ids
        }
        self.assertEqual(set(ROUTING_REQUESTS.values()), set(expected_paths))
        for request, skill_id in ROUTING_REQUESTS.items():
            with self.subTest(skill=skill_id):
                result = router.resolve(request)
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], skill_id, result)
                self.assertEqual(
                    Path(result["skill_path"]),
                    ROOT / expected_paths[skill_id],
                )

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
        for category_ids in MIGRATED.values():
            self.assertTrue(category_ids.issubset(index))


if __name__ == "__main__":
    unittest.main()
