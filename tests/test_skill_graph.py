import unittest

from scripts.validate_registry import validate_skill_relations


class SkillGraphTests(unittest.TestCase):
    def setUp(self):
        self.records = {
            "data": ("data", {"status": "active"}),
            "spark": ("data", {"status": "active", "parent_skill": "data"}),
            "joins": ("data", {"status": "active", "parent_skill": "spark"}),
            "skew": ("data", {
                "status": "active",
                "parent_skill": "joins",
                "related_skills": ["platform"],
            }),
            "platform": ("technology", {"status": "active"}),
        }

    def test_valid_deep_hierarchy_and_cross_domain_relation(self):
        self.assertEqual(validate_skill_relations(self.records), [])

    def test_rejects_parent_cycle(self):
        self.records["data"][1]["parent_skill"] = "skew"
        self.assertTrue(any("cycle" in item for item in validate_skill_relations(self.records)))

    def test_rejects_dangling_parent(self):
        self.records["spark"][1]["parent_skill"] = "does-not-exist"
        self.assertTrue(any("unknown parent_skill" in item for item in validate_skill_relations(self.records)))

    def test_rejects_cross_domain_parent(self):
        self.records["spark"][1]["parent_skill"] = "platform"
        self.assertTrue(any("same domain" in item for item in validate_skill_relations(self.records)))

    def test_rejects_inactive_parent(self):
        self.records["data"][1]["status"] = "draft"
        self.assertTrue(any("parent_skill is not active" in item for item in validate_skill_relations(self.records)))

    def test_rejects_dangling_related_edge(self):
        self.records["skew"][1]["related_skills"] = ["unknown"]
        self.assertTrue(any("unknown related skill" in item for item in validate_skill_relations(self.records)))

    def test_rejects_duplicate_related_edge(self):
        self.records["skew"][1]["related_skills"] = ["platform", "platform"]
        self.assertTrue(any("duplicate related skill" in item for item in validate_skill_relations(self.records)))

    def test_rejects_self_link(self):
        self.records["skew"][1]["related_skills"] = ["skew"]
        self.assertTrue(any("cannot relate to itself" in item for item in validate_skill_relations(self.records)))


if __name__ == "__main__":
    unittest.main()
