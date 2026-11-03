import unittest

from scripts.inspect_skill_graph import describe, load_records


class GraphInspectorTests(unittest.TestCase):
    def test_real_pyspark_ancestry(self):
        records = load_records()
        result = describe("pyspark-skew-diagnostics", records)
        self.assertEqual(result["domain"], "data")
        self.assertEqual(
            result["ancestry"],
            ["data-engineering-implementation", "pyspark-pipelines", "pyspark-joins"],
        )
        self.assertIn("platform-operations", result["related_skills"])

    def test_real_pyspark_children(self):
        records = load_records()
        result = describe("pyspark-pipelines", records)
        self.assertIn("pyspark-joins", result["children"])

    def test_unknown_skill_fails(self):
        with self.assertRaisesRegex(ValueError, "Unknown skill"):
            describe("not-a-skill", load_records())


if __name__ == "__main__":
    unittest.main()
