import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RegistryValidationTests(unittest.TestCase):
    def test_registry_is_valid(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_registry.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Validation passed", result.stdout)


if __name__ == "__main__":
    unittest.main()
