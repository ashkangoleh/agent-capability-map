import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from capability_map import Router, RouterError
from capability_map.cli import main
from capability_map.domain_selection import (
    MAX_SELECTED_DOMAINS,
    discover_domains,
    domain_status,
    update_domain_selection,
)

ROOT = Path(__file__).resolve().parents[1]


class DomainSelectionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.home = Path(self.temporary.name)

    def tearDown(self):
        self.temporary.cleanup()

    def apply(self, domains):
        return update_domain_selection(ROOT, self.home, domains, apply=True)

    def test_domain_catalog_exposes_requested_scopes(self):
        routes = {item["route"] for item in discover_domains(ROOT)}
        self.assertIn("data/data-engineering", routes)
        self.assertIn("data/data-science", routes)
        self.assertIn("infrastructure", routes)

    def test_dry_run_does_not_write_profile(self):
        result = update_domain_selection(
            ROOT, self.home, ["data/data-engineering", "infrastructure"], apply=False
        )
        self.assertEqual(result["status"], "dry_run")
        self.assertTrue(result["changed"])
        self.assertFalse(Path(result["profile_path"]).exists())
        self.assertEqual(domain_status(ROOT, self.home)["mode"], "all")

    def test_apply_restricts_router_to_selected_domain(self):
        self.apply(["data/data-engineering"])
        result = Router(ROOT, home=self.home).resolve("Create a new PySpark project")
        self.assertEqual(result["status"], "matched", result)
        self.assertEqual(result["selected_skill"], "pyspark-project-bootstrap")
        self.assertEqual(result["enabled_domains"], ["data/data-engineering"])

        disabled = Router(ROOT, home=self.home).resolve("Data scientist: bayesian modeling pymc stan")
        self.assertEqual(disabled["status"], "domain_not_enabled", disabled)
        self.assertNotIn("skill_path", disabled)

        disabled_infra = Router(ROOT, home=self.home).resolve("Review a Kubernetes Helm upgrade")
        self.assertEqual(disabled_infra["status"], "domain_not_enabled", disabled_infra)

    def test_parent_domain_scope_enables_all_descendants(self):
        self.apply(["data"])
        engineering = Router(ROOT, home=self.home).resolve("Create a new PySpark project")
        science = Router(ROOT, home=self.home).resolve("Data scientist: bayesian modeling pymc stan")
        self.assertEqual(engineering["status"], "matched", engineering)
        self.assertEqual(science["status"], "matched", science)

    def test_multiple_selected_scopes_are_available(self):
        selected = ["data/data-engineering", "data/data-science", "infrastructure"]
        self.apply(selected)
        requests = [
            ("Create a new PySpark project", "pyspark-project-bootstrap"),
            ("Data scientist: bayesian modeling pymc stan", "ds-bayesian-pymc-stan"),
            ("Review a Kubernetes Helm upgrade", "platform-operations"),
        ]
        for request, expected in requests:
            with self.subTest(request=request):
                result = Router(ROOT, home=self.home).resolve(request)
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], expected, result)

    def test_maximum_is_five_non_overlapping_scopes(self):
        self.assertEqual(MAX_SELECTED_DOMAINS, 5)
        five = [
            "data/data-engineering",
            "data/data-science",
            "infrastructure",
            "software-engineering",
            "ai-ml",
        ]
        self.apply(five)
        with self.assertRaisesRegex(RouterError, "At most 5"):
            update_domain_selection(
                ROOT, self.home, five + ["security"], apply=True
            )
        self.assertEqual(domain_status(ROOT, self.home)["registered_domains"], five)

    def test_parent_child_scope_overlap_is_rejected(self):
        with self.assertRaisesRegex(RouterError, "Overlapping"):
            update_domain_selection(
                ROOT, self.home, ["data", "data/data-engineering"], apply=True
            )
        self.assertFalse((self.home / ".config/agent-capability-map/domains.yaml").exists())

    def test_unknown_scope_is_rejected_without_write(self):
        with self.assertRaisesRegex(RouterError, "Unknown or non-selectable"):
            update_domain_selection(ROOT, self.home, ["data/not-a-domain"], apply=True)
        self.assertFalse((self.home / ".config/agent-capability-map/domains.yaml").exists())

    def test_add_is_idempotent_and_remove_is_explicit(self):
        self.apply(["data/data-engineering"])
        added = update_domain_selection(
            ROOT, self.home, ["data/data-engineering", "infrastructure"],
            operation="add", apply=True,
        )
        self.assertEqual(
            added["after_domains"], ["data/data-engineering", "infrastructure"]
        )
        removed = update_domain_selection(
            ROOT, self.home, ["infrastructure"], operation="remove", apply=True
        )
        self.assertEqual(removed["after_domains"], ["data/data-engineering"])
        with self.assertRaisesRegex(RouterError, "At least one domain must remain"):
            update_domain_selection(
                ROOT, self.home, ["data/data-engineering"], operation="remove", apply=True
            )

    def test_clear_restores_unrestricted_mode(self):
        self.apply(["data/data-engineering"])
        result = update_domain_selection(
            ROOT, self.home, operation="clear", apply=True
        )
        self.assertEqual(result["after_mode"], "all")
        self.assertFalse(Path(result["profile_path"]).exists())
        self.assertEqual(domain_status(ROOT, self.home)["mode"], "all")
        self.assertEqual(
            Router(ROOT, home=self.home).resolve("Review a Kubernetes Helm upgrade")["status"],
            "matched",
        )

    def test_corrupt_profile_fails_closed(self):
        target = self.home / ".config/agent-capability-map/domains.yaml"
        target.parent.mkdir(parents=True)
        target.write_text("schema_version: 99\ndomains: [infrastructure]\n", encoding="utf-8")
        with self.assertRaisesRegex(RouterError, "Unsupported domain selection schema"):
            Router(ROOT, home=self.home)

    def test_symlinked_profile_is_rejected(self):
        target = self.home / ".config/agent-capability-map/domains.yaml"
        target.parent.mkdir(parents=True)
        outside = self.home / "outside.yaml"
        outside.write_text("schema_version: 1\ndomains: [infrastructure]\n", encoding="utf-8")
        target.symlink_to(outside)
        with self.assertRaisesRegex(RouterError, "symlinked domain selection profile"):
            Router(ROOT, home=self.home)

    def test_cli_domain_apply_defaults_to_preview(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            main([
                "--root", str(ROOT),
                "domains", "apply",
                "--domains", "data/data-engineering", "infrastructure",
                "--home", str(self.home),
            ])
        result = json.loads(output.getvalue())
        self.assertEqual(result["status"], "dry_run")
        self.assertFalse(Path(result["profile_path"]).exists())


if __name__ == "__main__":
    unittest.main()
