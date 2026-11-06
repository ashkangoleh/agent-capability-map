"""Structural and truth-in-advertising tests for all 41 domains."""
import unittest
from scripts.audit_all_skill_evidence import audit


class AllSkillEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary = audit()

    def test_all_canonical_skills_have_independent_review_contract(self):
        r = self.summary
        self.assertEqual(r["domains"], 41)
        self.assertEqual(r["skills"], 513)
        self.assertEqual(r["canonical_ids"], 513)
        self.assertEqual(r["referenced_skills"], 513)
        self.assertEqual(r["problems"], [], r["problems"][:20])

    def test_hierarchical_ownership_is_not_bypassed(self):
        self.assertEqual(self.summary["roles"], 524)
        self.assertEqual(self.summary["per_domain"]["data"]["skills"], 186)
        self.assertEqual(self.summary["per_domain"]["infrastructure"]["skills"], 95)
        self.assertEqual(self.summary["per_domain"]["software-engineering"]["skills"], 52)
        self.assertEqual(self.summary["per_domain"]["ai-ml"]["skills"], 61)

    def test_no_false_production_certification(self):
        self.assertEqual(self.summary["host_task_quality"], "NOT_VERIFIED")
        self.assertEqual(self.summary["all_release_specific_sources"], "NOT_VERIFIED")
        self.assertEqual(self.summary["integration_and_regulatory_qualification"], "NOT_VERIFIED")


if __name__ == "__main__":
    unittest.main()
