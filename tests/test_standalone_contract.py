"""Static and simulated frozen-mode safeguards for the standalone package."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from capability_map.cli import root_location
from capability_map.install import instruction_text

ROOT = Path(__file__).resolve().parents[1]


class StandaloneContractTests(unittest.TestCase):
    def test_frozen_default_uses_executable_directory_not_temporary_pyinstaller_root(self):
        with tempfile.TemporaryDirectory(prefix="capability map frozen ") as directory:
            root = Path(directory).resolve()
            binary = root / ("capability-map.exe" if sys.platform == "win32" else "capability-map")
            with patch.dict("os.environ", {"CAPABILITY_MAP_HOME": ""}):
                with patch.object(sys, "frozen", True, create=True):
                    with patch.object(sys, "executable", str(binary)):
                        self.assertEqual(root_location(), root)
                        command = instruction_text(root)
            self.assertIn(str(binary), command)
            self.assertIn(str(root), command)
            self.assertIn(" --root ", command)
            self.assertIn(" resolve", command)
            self.assertNotIn("-m capability_map", command)

    def test_source_instruction_keeps_python_module_invocation(self):
        self.assertIn("-m capability_map --root", instruction_text(ROOT))

    def test_build_and_smoke_scripts_are_in_repository(self):
        for relative in (
            "scripts/build_standalone.py",
            "scripts/smoke_standalone.py",
            "scripts/standalone_entry.py",
        ):
            self.assertTrue((ROOT / relative).is_file())


if __name__ == "__main__":
    unittest.main()
