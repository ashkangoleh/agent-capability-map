"""AI/ML natural language, domain boundaries, and specialist gate integrity."""
import unittest
from pathlib import Path

from capability_map.router import load_yaml
from scripts.evaluate_ai_ml_quality import evaluate

ROOT = Path(__file__).resolve().parents[1]


class AIMLQualityTests(unittest.TestCase):
    def test_natural_language_and_boundary_regressions(self):
        actual = evaluate()
        self.assertEqual(actual["status"], "PASS", actual["failures"])
        self.assertEqual(actual["summary"]["natural-intent"], {"total": 43, "passed": 43})
        self.assertEqual(actual["summary"]["cross-domain-boundary"], {"total": 12, "passed": 12})
        self.assertEqual(actual["summary"]["scope-isolation"], {"total": 1, "passed": 1})

    def test_specialists_have_distinct_falsification_gates(self):
        cases = load_yaml(ROOT, "tests/fixtures/ai-ml-quality-cases.yaml")["cases"]
        natural = [case for case in cases if case["category"] == "natural-intent"]
        self.assertEqual(len(natural), 43)
        gates = set()
        for case in natural:
            branch, leaf = case["route"][1:]
            directory = {"llm-engineering": "llm", "rag-retrieval": "rag"}.get(branch, branch)
            skill = (ROOT / ".agents/skills/ai-ml" / directory / leaf
                     / case["skill"] / "SKILL.md")
            text = skill.read_text(encoding="utf-8")
            header = "## Specialist acceptance and falsification gates"
            self.assertEqual(text.count(header), 1, skill)
            section = text.split(header, 1)[1].split("## Authoritative references", 1)[0]
            for term in ("**Measured test:**", "**Rejection test:**", "rollback"):
                self.assertIn(term, section, skill)
            self.assertNotIn(section, gates, skill)
            gates.add(section)


if __name__ == "__main__":
    unittest.main()
