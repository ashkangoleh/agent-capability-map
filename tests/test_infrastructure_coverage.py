import unittest
from pathlib import Path

from capability_map import Router
from capability_map.domain_selection import discover_domains
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ROOT_SCOPES = {"compute-os","networking","cloud-engineering","iac-configuration","virtualization-private-cloud","containers-orchestration","devops-delivery","platform-engineering","sre-reliability","observability-engineering","infrastructure-security","storage-engineering","database-infrastructure","edge-infrastructure","hardware-datacenter","architecture-governance"}
EXPECTED_NEW_SKILLS = {
    "hpc-gpu-compute-scheduling",
    "os-fleet-patching-compliance",
    "unix-bsd-systems-operations",
    "dhcp-ipam-network-services",
    "network-automation-sdn",
    "network-switching-enterprise-routing",
    "wireless-lan-network-engineering",
    "cloud-architecture-reference-design",
    "aws-infrastructure-operations",
    "azure-infrastructure-operations",
    "gcp-infrastructure-operations",
    "oci-infrastructure-operations",
    "cloud-serverless-managed-runtime",
    "cloud-security-posture-governance",
    "configuration-management-puppet-chef-salt",
    "openstack-private-cloud-operations",
    "container-runtime-operations",
    "kubernetes-multicluster-tenancy",
    "kubernetes-gateway-api-ingress",
    "service-discovery-control-plane-operations",
    "infrastructure-observability-profiling",
    "infrastructure-capacity-performance",
    "identity-access-privileged-infrastructure",
    "zero-trust-network-access-engineering",
    "storage-san-nas-nvmeof",
    "object-storage-infrastructure-operations",
    "database-ha-replication-recovery",
    "database-nosql-cache-operations",
    "edge-compute-fleet-operations",
    "cdn-edge-delivery-operations",
    "bare-metal-provisioning-lifecycle",
    "server-hardware-firmware-management",
    "datacenter-power-cooling-dcim",
    "infrastructure-architecture-decision-review",
    "infrastructure-asset-configuration-inventory",
}


class InfrastructureCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = Router(ROOT)
        cls.cases = load_yaml(ROOT, "tests/fixtures/yaml-routing-cases.yaml")["cases"]

    def test_infrastructure_has_all_first_class_scopes(self):
        graph = load_yaml(ROOT, "domains/infrastructure/map.yaml")
        self.assertEqual({node["id"] for node in graph["children"]}, EXPECTED_ROOT_SCOPES)
        for node in graph["children"]:
            self.assertEqual(node["status"], "active")
            self.assertIn("map", node)

    def test_all_new_infrastructure_specialists_route(self):
        cases = [case for case in self.cases if case["id"].startswith("infra-specialist-")]
        self.assertEqual(len(cases), len(EXPECTED_NEW_SKILLS))
        selected = set()
        for case in cases:
            with self.subTest(case=case["id"]):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], case["skill"], result)
                self.assertLessEqual(len(result["inspected_files"]), 10)
                content = Path(result["skill_path"]).read_text(encoding="utf-8")
                for heading in ("## Production procedure", "## Failure modes and recovery",
                                "## Validation and evidence", "## Official references"):
                    self.assertIn(heading, content)
                selected.add(result["selected_skill"])
        self.assertEqual(selected, EXPECTED_NEW_SKILLS)

    def test_infrastructure_active_skill_ids_are_registered_once(self):
        seen_maps = set()
        registrations = []
        def walk(path):
            if path in seen_maps:
                return
            seen_maps.add(path)
            doc = load_yaml(ROOT, path)
            for child in doc["children"]:
                if child.get("map"):
                    walk(child["map"])
                elif child.get("skills"):
                    registry = load_yaml(ROOT, child["skills"])
                    registrations.extend(item["id"] for item in registry["skills"]
                                         if item.get("status") == "active")
        walk("domains/infrastructure/map.yaml")
        self.assertEqual(len(registrations), len(set(registrations)))
        self.assertEqual(len(registrations), 95)

    def test_advanced_storage_has_canonical_domain_paths(self):
        registry = load_yaml(ROOT, "domains/infrastructure/storage/new-specialists.yaml")
        expected = {
            "storage-san-nas-nvmeof",
            "object-storage-infrastructure-operations",
        }
        entries = {entry["id"]: entry for entry in registry["skills"]}
        self.assertEqual(set(entries), expected)
        for skill_id in expected:
            with self.subTest(skill=skill_id):
                expected_path = (
                    ".agents/skills/infrastructure/storage-engineering/"
                    f"advanced-storage/{skill_id}/SKILL.md"
                )
                self.assertEqual(entries[skill_id]["path"], expected_path)
                source = ROOT / expected_path
                self.assertTrue(source.is_file())
                self.assertFalse(source.is_symlink())
                self.assertFalse(
                    (ROOT / ".agents" / "skills" / skill_id / "SKILL.md").exists()
                )
                self.assertIn(
                    f"name: {skill_id}\n",
                    source.read_text(encoding="utf-8"),
                )

    def test_advanced_networking_has_distinct_canonical_routes(self):
        expected = {
            "network-routing-bgp": "routing-delivery",
            "network-load-balancing-proxy": "routing-delivery",
            "network-firewall-segmentation": "secure-connectivity",
            "network-vpn-wireguard": "secure-connectivity",
            "network-ebpf-observability": "telemetry",
            "dns-authoritative-infrastructure": "dns",
            "tls-pki-certificate-lifecycle": "pki",
        }
        graph = load_yaml(ROOT, "domains/infrastructure/networking/map.yaml")
        advanced = next(item for item in graph["children"] if item["id"] == "network-advanced")
        self.assertEqual(advanced["map"], "domains/infrastructure/networking/network-advanced/map.yaml")
        self.assertNotIn("skills", advanced)
        nested = load_yaml(ROOT, advanced["map"])
        self.assertEqual({node["id"] for node in nested["children"]}, set(expected.values()))
        fixtures = [
            case for case in self.cases
            if case.get("skill") in expected and case["id"].startswith("infra-expanded-")
        ]
        self.assertEqual({case["skill"] for case in fixtures}, set(expected))
        for case in fixtures:
            skill_id = case["skill"]
            category = expected[skill_id]
            with self.subTest(skill=skill_id):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], skill_id)
                self.assertEqual(result["route"], [
                    "infrastructure", "networking", "network-advanced", category,
                ])
                self.assertLessEqual(len(result["inspected_files"]), 10)
                expected_path = ROOT / (
                    f".agents/skills/infrastructure/networking/network-advanced/"
                    f"{category}/{skill_id}/SKILL.md"
                )
                self.assertEqual(Path(result["skill_path"]).resolve(), expected_path.resolve())
                self.assertTrue(expected_path.is_file())
                self.assertFalse((ROOT / ".agents" / "skills" / "infrastructure" /
                                  "network-advanced" / skill_id / "SKILL.md").exists())

    def test_devsecops_has_separate_security_capability_routes(self):
        expected = {
            "devsecops-security-gates": "policy-gates",
            "policy-as-code-opa-kyverno": "policy-gates",
            "container-image-signing-sigstore": "supply-chain",
            "software-supply-chain-slsa-sbom": "supply-chain",
            "runtime-security-falco": "runtime-security",
            "secrets-workload-identity-spiffe": "workload-identity",
        }
        root = load_yaml(ROOT, "domains/infrastructure/infrastructure-security/map.yaml")
        node = next(item for item in root["children"] if item["id"] == "devsecops")
        self.assertEqual(
            node["map"], "domains/infrastructure/infrastructure-security/devsecops/map.yaml"
        )
        self.assertNotIn("skills", node)
        graph = load_yaml(ROOT, node["map"])
        self.assertEqual({item["id"] for item in graph["children"]}, set(expected.values()))
        registry_ids = []
        for child in graph["children"]:
            registry = load_yaml(ROOT, child["skills"])
            registry_ids.extend(item["id"] for item in registry["skills"])
        self.assertEqual(set(registry_ids), set(expected))
        self.assertEqual(len(registry_ids), len(expected))
        fixtures = [
            case for case in self.cases
            if case.get("skill") in expected and case["id"].startswith("infra-expanded-")
        ]
        self.assertEqual({case["skill"] for case in fixtures}, set(expected))
        for case in fixtures:
            skill_id = case["skill"]
            category = expected[skill_id]
            with self.subTest(skill=skill_id):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], skill_id)
                self.assertEqual(result["route"], [
                    "infrastructure", "infrastructure-security", "devsecops", category,
                ])
                self.assertLessEqual(len(result["inspected_files"]), 10)
                expected_path = ROOT / (
                    f".agents/skills/infrastructure/infrastructure-security/"
                    f"devsecops/{category}/{skill_id}/SKILL.md"
                )
                self.assertEqual(Path(result["skill_path"]).resolve(), expected_path.resolve())
                self.assertTrue(expected_path.is_file())
                self.assertFalse(
                    (ROOT / ".agents/skills/infrastructure/devsecops" / skill_id / "SKILL.md").exists()
                )

    def test_kubernetes_cluster_operator_and_cni_routes_are_independent(self):
        categories = {
            "kubernetes-cluster-upgrade-capacity": "cluster-lifecycle",
            "kubernetes-operator-crd-lifecycle": "operators-extensions",
            "kubernetes-cni-ebpf-operations": "cni-datapath",
        }
        graph = load_yaml(ROOT, "domains/infrastructure/kubernetes/map.yaml")
        nodes = {item["id"]: item for item in graph["children"]}
        self.assertTrue(set(categories.values()).issubset(nodes))
        for category in categories.values():
            self.assertIn("skills", nodes[category])
            registry = load_yaml(ROOT, nodes[category]["skills"])
            self.assertEqual(len(registry["skills"]), 1)
        fixtures = [
            case for case in self.cases
            if case.get("skill") in categories and case["id"].startswith("infra-expanded-")
        ]
        self.assertEqual({case["skill"] for case in fixtures}, set(categories))
        for case in fixtures:
            skill_id = case["skill"]
            category = categories[skill_id]
            with self.subTest(skill=skill_id):
                result = self.router.resolve(case["request"])
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result["selected_skill"], skill_id)
                self.assertEqual(result["route"], [
                    "infrastructure", "containers-orchestration", "kubernetes", category
                ])
                self.assertLessEqual(len(result["inspected_files"]), 10)
                expected_path = ROOT / (
                    f".agents/skills/infrastructure/containers-orchestration/"
                    f"kubernetes/{category}/{skill_id}/SKILL.md"
                )
                self.assertEqual(Path(result["skill_path"]).resolve(), expected_path.resolve())
                self.assertTrue(expected_path.is_file())
                self.assertFalse(
                    (ROOT / ".agents/skills/infrastructure/kubernetes" / skill_id / "SKILL.md").exists()
                )
        # The CNI specialist must not capture higher-level NetworkPolicy troubleshooting.
        network_policy = self.router.resolve("Review kubernetes networkpolicy")
        self.assertEqual(network_policy["status"], "matched", network_policy)
        self.assertEqual(network_policy["selected_skill"], "kubernetes-networking-triage")

    def test_all_active_infrastructure_skills_have_routing_fixtures(self):
        seen_maps = set()
        active = set()

        def visit(path):
            if path in seen_maps:
                return
            seen_maps.add(path)
            document = load_yaml(ROOT, path)
            for child in document["children"]:
                if child.get("map"):
                    visit(child["map"])
                elif child.get("skills"):
                    registry = load_yaml(ROOT, child["skills"])
                    active.update(entry["id"] for entry in registry["skills"]
                                  if entry.get("status") == "active")

        visit("domains/infrastructure/map.yaml")
        covered = {
            case.get("skill") for case in self.cases
            if case.get("status") == "matched"
        }
        self.assertEqual(len(active), 95)
        self.assertFalse(active - covered,
                         f"Infrastructure skills without deterministic routing fixtures: {sorted(active - covered)}")

    def test_infrastructure_scopes_are_selectable(self):
        scopes = {item["route"] for item in discover_domains(ROOT, prefix="infrastructure")}
        for route in ("infrastructure/networking",
                      "infrastructure/cloud-engineering",
                      "infrastructure/containers-orchestration/kubernetes",
                      "infrastructure/observability-engineering",
                      "infrastructure/hardware-datacenter"):
            self.assertIn(route, scopes)

    def test_master_index_contains_all_new_specialists(self):
        index = set(load_yaml(ROOT, "catalog/master-skill-ids.yaml")["ids"])
        self.assertTrue(EXPECTED_NEW_SKILLS.issubset(index))
        self.assertGreaterEqual(len(index), 322)


if __name__ == "__main__":
    unittest.main()
