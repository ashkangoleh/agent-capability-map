"""OS-portable commands and non-destructive host install integration tests."""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from capability_map.install import install, instruction_text

ROOT = Path(__file__).resolve().parents[1]


def cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "capability_map", "--root", str(ROOT), *map(str, args)],
        capture_output=True, text=True, encoding="utf-8", check=False,
    )


class CrossPlatformCliTests(unittest.TestCase):
    def test_python_resolve_and_validate_are_cwd_independent(self):
        validate = cli("validate")
        self.assertEqual(validate.returncode, 0, validate.stderr)
        self.assertEqual(json.loads(validate.stdout)["status"], "valid")
        matched = cli("resolve", "--request", "Infrastructure: falco runtime security detection")
        self.assertEqual(matched.returncode, 0, matched.stderr)
        result = json.loads(matched.stdout)
        self.assertEqual(result["selected_skill"], "runtime-security-falco")
        self.assertGreaterEqual(len(result["role_paths"]), 4)

    def test_profile_apply_is_explicit_and_shared_across_invocations(self):
        with tempfile.TemporaryDirectory(prefix="capability map windows path ") as workspace:
            home = Path(workspace)
            preview = cli("domains", "apply", "--domains", "infrastructure",
                          "data/data-engineering", "--home", home)
            self.assertEqual(preview.returncode, 0, preview.stderr)
            self.assertFalse((home / ".config/agent-capability-map/domains.yaml").exists())
            applied = cli("domains", "apply", "--domains", "infrastructure",
                          "data/data-engineering", "--home", home, "--apply")
            self.assertEqual(applied.returncode, 0, applied.stderr)
            self.assertEqual(json.loads(applied.stdout)["status"], "applied")
            blocked = cli("resolve", "--request", "Audit technical SEO canonical tags",
                          "--home", home)
            self.assertEqual(json.loads(blocked.stdout)["status"], "domain_not_enabled")
            self.assertNotIn("role_paths", json.loads(blocked.stdout))

    def test_installer_embeds_root_and_uses_native_shell_quoting(self):
        with tempfile.TemporaryDirectory(prefix="capability map quoted home ") as workspace:
            home = Path(workspace)
            installed = install(["codex", "cursor"], home, root=ROOT, apply=True)
            self.assertEqual(len(installed), 2)
            text = (home / ".codex/AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("-m capability_map --root ", text)
            self.assertIn(str(ROOT.resolve()), text)
            self.assertIn("role_paths", text)
            if os.name == "nt":
                self.assertIn("& '", text)
                self.assertIn("'", text)
            else:
                self.assertIn(" -m capability_map --root ", text)
            self.assertEqual(text, (home / ".codex/AGENTS.md").read_text(encoding="utf-8"))
            self.assertEqual(instruction_text(ROOT).count(" -m capability_map "), 1)


if __name__ == "__main__":
    unittest.main()
