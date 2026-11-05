# Infrastructure Engineering Coverage Audit

**Branch:** `pre_release`  
**Status:** Expanded structural taxonomy; production certification remains evidence-gated.

## Scope and boundary

Infrastructure Engineering covers the lifecycle of the compute, network, cloud, storage, virtualization, container, platform and physical foundations on which software and data systems run.

Included:
- Compute, operating systems, kernel, host lifecycle, HPC and accelerators
- Enterprise networking, switching, routing, wireless, DNS, DHCP, IPAM, NTP, VPN, firewalls, load balancing and network automation
- Public, private and hybrid cloud foundations, provider operations, serverless infrastructure, IAM, FinOps and cloud posture
- Infrastructure as Code, configuration management and immutable machine images
- Virtualization, private cloud, containers, Kubernetes, service mesh and service discovery
- CI/CD, GitOps, release engineering and artifact provenance
- Platform engineering, IDPs, control planes, golden paths and secrets operations
- SRE, incident management, SLOs, chaos, capacity, backup and disaster recovery
- Observability, telemetry pipelines, metrics, logs, traces, profiling and cost/cardinality control
- Infrastructure security, privileged access, zero trust, policy as code and software supply-chain controls
- Block, file, distributed and object storage; database platform operations and recovery
- Edge compute, CDN, bare metal, firmware, BMC and data-center facilities
- Infrastructure architecture, asset inventory, CMDB and configuration governance

Explicit boundaries:
- Data pipelines, lakehouse table semantics, analytics, data quality and data governance remain under Data.
- Database schema design, SQL analytics and data modeling remain under Data/Database Engineering; this domain owns database platform availability, replication, backup and operations.
- Application code, API implementation and application security remain under Software Engineering and Security.
- Cellular RAN, 5G core, telecom signaling and carrier network engineering remain under Telecommunications.
- Industrial control systems and OT safety remain under relevant industrial domains.

## First-class selectable scopes

| Scope | Coverage |
|---|---|
| Compute & OS | Linux, Windows, Unix/BSD, kernel, host patching, fleet compliance, HPC/GPU |
| Networking | L2/L3, routing, BGP, OSPF/IS-IS, EVPN/VXLAN, DNS, DHCP, IPAM, NTP, WLAN, VPN, firewalls, proxies, eBPF, SDN |
| Cloud Engineering | AWS, Azure, GCP, OCI, landing zones, network, IAM, FinOps, serverless, cloud posture |
| IaC & Configuration | Terraform, OpenTofu, Pulumi, Packer, Ansible, Puppet, Chef, Salt, Nix-style configuration |
| Virtualization & Private Cloud | KVM, Proxmox, VMware, OpenStack, HCI and VM lifecycle |
| Containers & Orchestration | OCI, Docker, Podman, containerd, CRI-O, Kubernetes, Helm, CNI, CSI, Gateway API, service mesh, discovery |
| DevOps & Delivery | CI/CD, GitOps, Argo CD, Flux, immutable artifacts, release and provenance |
| Platform Engineering | Backstage, Crossplane, Karpenter, KEDA, IDP, golden paths, secrets and platform operations |
| SRE & Reliability | SLI/SLO, error budgets, incident response, chaos, capacity, backup, restore, RPO/RTO |
| Observability Engineering | Prometheus, OpenTelemetry, logs, metrics, traces, profiling, eBPF and telemetry economics |
| Infrastructure Security | IAM, PAM, federation, JIT, zero trust, CSPM/CNAPP, policy as code, runtime and supply-chain security |
| Storage Engineering | Block, file, SAN, NAS, Fibre Channel, iSCSI, NVMe-oF, Ceph, ZFS, LVM, S3-compatible object storage |
| Database Infrastructure | PostgreSQL, MySQL, HA, replication, failover, PITR, MongoDB, Redis, Cassandra |
| Edge Infrastructure | K3s/KubeEdge, remote fleet, offline operation, OTA and CDN |
| Hardware & Data Center | PXE/iPXE, MAAS, Metal3, Redfish, IPMI, UEFI, firmware, rack, UPS/PDU, cooling and DCIM |
| Architecture & Governance | NFRs, topology, failure domains, ADRs, asset inventory, CMDB, ownership and drift |

## Specialist inventory

- Existing unique Infrastructure specialists retained and re-homed: 60.
- New specialist packages added in this expansion: 35.
- Target Infrastructure specialist inventory: 95 unique active skills.
- Duplicate registrations of `platform-operations` and `kubernetes-rollout-safety` are consolidated to one canonical registry location each.

This is structural coverage, not production certification. Existing packages still require per-skill depth review, version-specific verification and independent task evaluation.

## Advanced Networking taxonomy increment — 2026-11-05

Seven existing skills formerly shared one broad `network-advanced` registry. They are now grouped by existing task boundaries in five categories: `routing-delivery`, `secure-connectivity`, `telemetry`, `dns`, and `pki`. This preserves the original IDs, descriptions, triggers, exclusions, and complete `SKILL.md` Git blobs; only explicit paths and the depth of the YAML route change. Existing routing fixtures remain unchanged, and a new regression test verifies all seven canonical routes and uniqueness. This is **one reviewed category**, not completion of the 95-specialist infrastructure depth audit.

**Outstanding:** Many infrastructure source paths still reflect historical packaging rather than their exact logical route (e.g. `devops-sre` versus `devops-delivery`); native host integration, individual skill correctness and recovery/failure testing remain unverified. Do not claim production-ready or taxonomy-complete based on 95 registered skills.

## Infrastructure routing fixture inventory — 2026-11-05

Prior to this change, **94/95** active Infrastructure skill IDs were covered by at least one deterministic routing fixture; the missing specialist was `platform-operations`. Two explicit requests (English and Persian/English mixed) now verify its route. A regression assertion checks that **every** registered active Infrastructure specialist has at least one matching fixture. This closes one fixture-inventory gap, **not** the broader need for hard negatives, blind multilingual task evaluation and real host/agent execution. Most specialists still have just one positive fixture.

## DevSecOps capability routing increment — 2026-11-05

The previous six-skill shared DevSecOps registry mixed policy enforcement, software supply-chain provenance, runtime detection and workload identity. It is now split into **four** explicitly routed capability groups with **six unchanged specialist skills**:

- `policy-gates` — CI/deployment security gates and admission policy controls (2)
- `supply-chain` — artifact signatures, attestations, SBOM and provenance verification (2)
- `runtime-security` — Falco-based runtime detection and operational response (1)
- `workload-identity` — SPIFFE/SPIRE identity, attestation and credential lifecycle (1)

This division follows the distinct deploy, distribution/supply-chain and runtime concerns of CNCF TAG Security's cloud-native security model. Evidence: https://github.com/cncf/tag-security and https://github.com/cncf/tag-security/blob/main/community/resources/security-whitepaper/v2/cloud-native-security-whitepaper.md .

All six `SKILL.md` files are moved by preserving their original Git blob SHA; IDs, descriptions, registry skill triggers and exclusions are unchanged. No new specialist was added, and the **469 pre-existing routing fixtures** remain unchanged. The additional unit test verifies registry partitioning, end-to-end selection, canonical category path and old-path removal. The result is improved taxonomy isolation, **not** independent security assurance or production-ready procedures.

## Kubernetes cluster operations taxonomy increment — 2026-11-05

The former `cluster-lifecycle` registry mixed **three different operations**: cluster version upgrades, custom-resource/operator controller lifecycle, and CNI/eBPF datapath troubleshooting. They are now independent siblings under the existing Kubernetes map:

- `cluster-lifecycle` — cluster upgrades and capacity/version-skew operations
- `operators-extensions` — CRDs, reconciliation/finalizers and operator lifecycle
- `cni-datapath` — CNI/eBPF datapath, IPAM, MTU and packet policy

The three original `SKILL.md` Git blobs are preserved exactly and the old multi-skill registry is removed. Existing fixtures continue to select the same specialist IDs; tests now assert distinct logical routes, exact physical paths, and a negative near-miss separation between CNI and service NetworkPolicy troubleshooting. The canonical Kubernetes docs distinguish cluster administration, operator patterns and cluster networking:
- https://kubernetes.io/docs/concepts/cluster-administration/
- https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
- https://kubernetes.io/docs/concepts/cluster-administration/networking/

This is a structural/behavior-preserving specialization for existing explicit triggers. It does not certify real Kubernetes commands, integration versions or live agent selection.

## SRE & Reliability taxonomy increment — 2026-11-05

The earlier `sre-practices` registry combined four operationally distinct capabilities. It is now four selectable sibling categories under `sre-reliability`: `slo-governance`, `capacity-engineering`, `failure-injection` and `disaster-recovery`. The existing `incident-management` category remains separate.

All four `SKILL.md` source files retain their original Git blobs; stable skill IDs, descriptions, positive trigger strings and exclusions are unchanged. Registry source paths and map boundaries changed, with no new registered skills. Existing fixtures verify route changes, and a regression check prevents incident management from being routed into an SLO category.

References for reasoning about SLO/error-budget policy, load testing/capacity and restore/disaster recovery readiness:
- https://sre.google/workbook/error-budget-policy/
- https://sre.google/sre-book/service-best-practices/
- https://sre.google/sre-book/launch-checklist/

This is routing/taxonomy normalization, **not** a verification that the individual failure-injection procedures are safe in production or that backup restores meet their actual RPO/RTO.

## Focused specialist-depth correction — Falco runtime security (2026-11-05)

A source-content spot check showed that the previous `runtime-security-falco` skill used a generic SAST/DAST/SCA and deployment-gates workflow instead of a usable Falco runtime diagnosis. This was a substantive specialist-quality gap even though its YAML routing and canonical path were valid.

Updated the **existing** Falco skill in place (version `1.1.0`, stable skill ID and route) with a source-grounded runtime procedure: syscall event-source/driver support, modern eBPF vs kernel module, version and privilege checks, rule validation/load order, documented override semantics, canary rollout, kernel-side drops, output queue drops, benign detection events, incident ownership and safe rollback. The updated document deliberately avoids asserting any measured production result.

Sources: https://falco.org/docs/setup/download/ , https://falco.org/docs/concepts/rules/overriding/ , https://falco.org/docs/reference/daemon/cli-arguments/ , https://falco.org/docs/concepts/metrics/ and https://falco.org/docs/troubleshooting/dropping/ .

The new regression test checks the Falco-specific operational content and preserves the existing deterministic routing fixture. **This is one specialist-depth improvement, not proof that all 95 Infrastructure skills are production-ready.** Other sampled instructions (notably Kubernetes Operator and DR/restore) still show generic procedural content and require their own validated rewrites.

## Specialist depth corrections — Operator/CRD and Backup/DR (2026-11-05)

Two existing named specialist skills still contained cross-specialty generic procedures. The Operator/CRD skill described cluster node-pool upgrades rather than a reconcile/controller lifecycle. The Backup/DR skill outlined broad SLI/SLO telemetry rather than recoverability testing. Both are now versioned `1.1.0` with their existing IDs, registry paths and activation triggers unchanged.

- `kubernetes-operator-crd-lifecycle`: structural CRD schema, idempotent reconciliation, status/observedGeneration, finalizers and safe cleanup, conversion webhooks, served/storage versions and stored-version migration, canary/rollback and evidence. Official Kubernetes docs: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/ and https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/ .
- `backup-dr-restore-exercises`: service dependencies, immutable recovery-point evidence, key/permission isolation, point-in-time recovery, cross-system consistency, isolated drills, actual RPO/RTO measurement, integrity checks, failback and cleanup. Official AWS guidance: https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html and https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/test.html .
- `tests/test_infrastructure_coverage.py` now checks focused specialist terms, exclusion of old generic procedures and unchanged deterministic router selections.

**Limit:** static content tests and CI do not execute a Kubernetes controller, a conversion webhook, a restored service or a five-host agent run. Actual version-specific effectiveness, blast radius and observed RPO/RTO remain unverified. All other 93 Infrastructure skill bodies still need their own evidence-driven depth review.

## Role contract future work

The user requires a dedicated quality-improving **Domain Role** for each domain, designed later. See `docs/DOMAIN_ROLE_DESIGN_BACKLOG.md`. It is an **unimplemented, optional post-router reviewer contract**, not a new role-loading feature, a change in the deterministic allowlist, or a claim that all 41 domains have been analyzed.

## Completion gates

1. Review every existing and new `SKILL.md` for specialist depth, not just frontmatter and headings.
2. Verify commands, APIs and version compatibility against current official vendor documentation.
3. Add negative, ambiguous, near-miss and Persian/English routing fixtures for every specialist.
4. Test failure, recovery, rollback, capacity exhaustion, identity expiry and partial control-plane failure where applicable.
5. Measure resolver false positives/false negatives using a labeled benchmark; deterministic fixtures are not semantic accuracy.
6. Verify real skill loading and context behavior in Codex, OpenCode, Copilot, Claude Code and Cursor.
7. Keep domain boundaries explicit and use typed cross-domain relations instead of duplicating skills.

## Reference basis

The CNCF landscape is a cloud-native ecosystem reference, not a complete infrastructure taxonomy. This map intentionally extends to physical compute, networking, storage, operating systems, private cloud and data-center infrastructure. CNCF TAG Infrastructure explicitly spans data, storage, network, DNS, compute, service mesh, IaC, edge, sovereignty and load balancing.
- https://landscapeapp.cncf.io/cncf/guide
- https://contribute.cncf.io/community/tags/infrastructure/
- https://maturitymodel.cncf.io/aspects/technology/
