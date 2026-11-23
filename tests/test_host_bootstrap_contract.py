"""Simulated host-bootstrap contract; not a real host-agent execution test."""
import tempfile
import unittest
from pathlib import Path

from capability_map import Router
from capability_map.install import install

ROOT = Path(__file__).resolve().parents[1]
HOSTS = ("codex", "claude", "opencode", "copilot", "cursor")


class HostBootstrapContractTests(unittest.TestCase):
    def test_all_host_installers_publish_only_the_small_router_bootstrap(self):
        for host in HOSTS:
            with self.subTest(host=host), tempfile.TemporaryDirectory() as directory:
                home = Path(directory)
                results = install([host], home, root=ROOT, apply=True)
                self.assertEqual(len(results), 1)
                path = Path(results[0]["path"])
                self.assertTrue(path.is_file())
                text = path.read_text(encoding="utf-8")
                self.assertIn("Global Master Capability Router", text)
                self.assertIn("-m capability_map --root", text)
                self.assertIn(str(ROOT.resolve()), text)
                self.assertIn("role_paths", text)
                self.assertIn("read only the returned skill_path", text)
                self.assertIn("domain_not_enabled", text)
                installed_skills = list(home.rglob("SKILL.md"))
                if host == "cursor":
                    self.assertEqual(installed_skills, [home / ".cursor/skills/master-capability-router/SKILL.md"])
                else:
                    self.assertEqual(installed_skills, [])
                # The full 344-skill library must not be copied to a user's host.
                self.assertFalse((home / ".agents/skills").exists())

    def test_installed_router_contract_resolves_the_nested_recovery_skill(self):
        result = Router(ROOT).resolve("Plan a pipeline backfill recovery for missing dates")
        self.assertEqual(result["status"], "matched", result)
        self.assertEqual(result["selected_skill"], "pipeline-backfill-recovery", result)
        expected = ROOT / ".agents/skills/data/data-engineering/batch-ingestion/recovery/pipeline-backfill-recovery/SKILL.md"
        self.assertEqual(Path(result["skill_path"]).resolve(), expected.resolve())
        self.assertTrue(expected.is_file())


if __name__ == "__main__":
    unittest.main()
