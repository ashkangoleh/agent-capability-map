"""Role-contract specificity and inheritance checks for four expanded domains.

Structural guards only: not an evaluation of model adherence or source truth.
"""
import re
import unittest
from pathlib import Path

from capability_map.router import (
    MAX_ROLE_CHAIN_BYTES,
    MAX_ROLE_CHAIN_FILES,
    load_yaml,
    role_paths_for_route,
)

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "marketing": (7, 17),
    "seo": (9, 22),
    "content": (9, 22),
    "research": (8, 22),
}
LEVEL_MARKERS = {
    1: "## Cross-domain governance",
    2: "## Delegation and scope",
    3: "## Specialist acceptance contract",
}


def read_role(scope):
    rel = Path("domains", *scope, "ROLE.md")
    text = (ROOT / rel).read_text(encoding="utf-8")
    role_id = re.search(r"(?m)^role_id:\s*(\S+)\s*$", text)
    assert role_id is not None, f"Missing role_id: {rel}"
    assert role_id.group(1) == "/".join(scope), f"Wrong role_id: {rel}"
    marker = LEVEL_MARKERS[len(scope)]
    assert text.count(marker) == 1, f"Missing or repeated {marker}: {rel}"
    section = text.split(marker, 1)[1].split("\n## ", 1)[0]
    evidence = re.findall(r"(?m)^- Evidence:\s*(\S.*)$", section)
    accepted = re.findall(r"(?m)^- Acceptance and ownership:\s*(\S.*)$", section)
    stop = re.findall(r"(?m)^- Stop or escalate:\s*(\S.*)$", section)
    assert len(evidence) == len(accepted) == len(stop) == 1, f"Incomplete acceptance contract: {rel}"
    assert all(len(x[0]) >= 40 for x in (evidence, accepted, stop)), f"Generic acceptance contract: {rel}"
    assert "## Authority boundary" in text, f"Missing authority boundary: {rel}"
    return (ROOT / rel), (evidence[0], accepted[0], stop[0])


class ExpandedDomainRoleQualityTests(unittest.TestCase):
    def test_exact_hierarchical_coverage_and_distinct_specialists(self):
        all_evidence = []
        totals = [0, 0, 0]
        for domain, (expected_groups, expected_leaves) in EXPECTED.items():
            read_role([domain])
            totals[0] += 1
            graph = load_yaml(ROOT, f"domains/{domain}/map.yaml")
            self.assertEqual(len(graph["children"]), expected_groups, domain)
            leaf_count = 0
            for group in graph["children"]:
                self.assertEqual(group["status"], "active")
                gid = group["id"]
                read_role([domain, gid])
                totals[1] += 1
                sub = load_yaml(ROOT, group["map"])
                for leaf in sub["children"]:
                    self.assertEqual(leaf["status"], "active")
                    self.assertTrue(leaf.get("skills"))
                    lid = leaf["id"]
                    leaf_count += 1
                    totals[2] += 1
                    _, contract = read_role([domain, gid, lid])
                    all_evidence.append(contract)
                    route = [domain, gid, lid]
                    paths = role_paths_for_route(ROOT, route)
                    self.assertEqual(
                        paths,
                        [str(ROOT / "domains" / Path(*route[:n]) / "ROLE.md") for n in (1, 2, 3)],
                    )
                    self.assertLessEqual(len(paths), MAX_ROLE_CHAIN_FILES)
                    self.assertLessEqual(
                        sum(Path(path).stat().st_size for path in paths),
                        MAX_ROLE_CHAIN_BYTES,
                        f"Role inheritance budget exceeded: {'/'.join(route)}",
                    )
            self.assertEqual(leaf_count, expected_leaves, domain)
        self.assertEqual(totals, [4, 33, 83])
        self.assertEqual(len(all_evidence), len(set(all_evidence)))

    def test_role_contract_is_read_only_and_never_an_authorization(self):
        for domain, (groups, leaves) in EXPECTED.items():
            root, _ = read_role([domain])
            body = root.read_text(encoding="utf-8")
            self.assertIn("## Authority boundary", body)
            self.assertIn("approval", body.lower())
            self.assertNotIn("## Privilege escalation", body)


if __name__ == "__main__":
    unittest.main()
