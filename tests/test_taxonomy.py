import unittest

from scripts.validate_taxonomy import (
    TaxonomyValidationError,
    validate,
    validate_tree,
)


class CoverageTaxonomyTests(unittest.TestCase):
    def test_coverage_taxonomy_matches_domain_catalog(self):
        validate()

    def test_rejects_empty_branch(self):
        with self.assertRaises(TaxonomyValidationError):
            validate_tree({"data-engineering": {}})

    def test_rejects_duplicate_leaf(self):
        with self.assertRaises(TaxonomyValidationError):
            validate_tree({"spark": ["pyspark", "pyspark"]})

    def test_rejects_invalid_name(self):
        with self.assertRaises(TaxonomyValidationError):
            validate_tree({"some invalid name": ["test"]})


if __name__ == "__main__":
    unittest.main()
