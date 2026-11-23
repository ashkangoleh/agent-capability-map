# Infrastructure Engineering Tool and Concept Matrix

This is a maintained discovery baseline, not an endorsement list. A tool is not promoted to an active specialist solely because it is popular; official references, task boundaries and failure/recovery procedures are required.

| Capability area | Concepts and standards | Representative tools and ecosystems |
|---|---|---|
| Compute & OS | CPU, NUMA, memory, kernel, boot, systemd/rc, patch rings, package provenance, cgroups | Linux, Windows Server, FreeBSD, OpenBSD, NetBSD, Solaris/illumos, systemd, DNF/APT, cloud-init |
| HPC & accelerators | Batch scheduling, fair-share, QoS, GPU partitioning, NUMA, RDMA, InfiniBand, checkpoint/requeue | Slurm, PBS, NVIDIA GPUs, MIG, CUDA, NCCL, ROCm, InfiniBand |
| Network foundations | Ethernet, VLAN, STP, LACP, IPv4/IPv6, ARP/ND, MTU, VRF, QoS, routing convergence | Cisco IOS/NX-OS, Juniper Junos, Arista EOS, FRRouting, SONiC |
| Routing and fabric | BGP, OSPF, IS-IS, EVPN/VXLAN, ECMP, route policy, anycast, SD-WAN | FRR, BIRD, GoBGP, vendor routing stacks |
| Network services | DNS, DNSSEC, DHCP, DHCPv6, IPAM, NTP/PTP, RADIUS, TACACS+, PKI | BIND, Unbound, CoreDNS, Kea, Infoblox, NetBox, chrony, FreeRADIUS |
| Network automation | Source of truth, NETCONF, RESTCONF, gNMI/gNOI, YANG, OpenConfig, drift, intent | NetBox, Nornir, Ansible Network, pyATS, Batfish, OpenConfig |
| Network security | Segmentation, firewall policy, NAC, 802.1X, VPN, IPsec, WireGuard, WAF, DDoS | nftables, iptables, pf, Palo Alto, Fortinet, WireGuard, strongSwan |
| Load balancing and proxy | L4/L7, reverse proxy, TLS termination, health checks, connection draining, rate limits | HAProxy, Envoy, NGINX, Traefik, F5, A10, cloud load balancers |
| Cloud foundations | Organizations, accounts, subscriptions, projects, landing zones, regions, zones, quotas | AWS Organizations/Control Tower, Azure CAF/Management Groups, GCP Resource Manager/Shared VPC, OCI compartments/VCN |
| Cloud network | VPC/VNet/VCN, transit, peering, private endpoints, NAT, DNS, egress | AWS Transit Gateway/Cloud WAN, Azure Virtual WAN, GCP Cloud Router, OCI DRG |
| Cloud IAM and security | Federation, workload identity, policy inheritance, KMS, audit, CSPM/CNAPP | IAM Identity Center, Entra ID, GCP IAM, OCI IAM, Security Hub, Defender for Cloud, Security Command Center |
| Cloud cost and capacity | Allocation, tagging, showback, unit economics, commitments, egress, rightsizing, quotas | AWS Cost Explorer, Azure Cost Management, GCP Billing, OCI Cost Analysis, OpenCost, Kubecost |
| Serverless infrastructure | FaaS, managed containers, event sources, concurrency, retries, DLQ, cold starts | AWS Lambda, Azure Functions, Cloud Run, Knative |
| IaC | Declarative plans, state, drift, imports, policy checks, module contracts, provider pinning | Terraform, OpenTofu, Pulumi, CloudFormation, CDK, Bicep, ARM, Crossplane |
| Configuration management | Desired state, idempotency, convergence, agent/pull models, package/policy management | Ansible, Puppet, Chef, Salt, CFEngine, Nix |
| Image lifecycle | Immutable images, golden images, provenance, promotion, SBOM | Packer, Image Builder, cloud image pipelines, OpenSCAP |
| Virtualization/private cloud | Hypervisors, live migration, virtual networking, HCI, VM lifecycle, quotas | KVM, QEMU, Proxmox, VMware vSphere/VCF, Hyper-V, OpenStack, Nutanix |
| Container runtime | OCI image/runtime, namespaces, cgroups v2, seccomp, AppArmor, SELinux, rootless | containerd, CRI-O, Docker Engine, Podman, BuildKit, runc, crun |
| Kubernetes core | API server, etcd, scheduler, controllers, kubelet, admission, RBAC, quotas, upgrades | Kubernetes, kubeadm, Cluster API, managed Kubernetes distributions |
| Kubernetes networking | CNI, IPAM, NetworkPolicy, Gateway API, ingress, service routing, eBPF datapath | Cilium, Calico, Flannel, Antrea, Gateway API controllers, CoreDNS |
| Kubernetes storage | CSI, PV/PVC, StorageClass, topology, snapshots, expansion, attach/mount recovery | CSI drivers, Ceph RBD, EBS, Azure Disk, GCE PD, Longhorn |
| Kubernetes packaging/policy | Helm, Kustomize, CRDs, operators, GitOps, admission and policy | Helm, Kustomize, Operator SDK, OPA Gatekeeper, Kyverno |
| Service mesh/discovery | mTLS, traffic policy, retries, telemetry, registration, quorum, DNS discovery | Istio, Linkerd, Consul, etcd, CoreDNS |
| CI/CD and delivery | Build isolation, artifact promotion, immutable releases, canary, blue/green, rollback | GitHub Actions, GitLab CI, Jenkins, Tekton, Argo CD, Flux |
| Supply-chain security | SBOM, SLSA provenance, signing, attestations, verification, trusted builders | Sigstore Cosign, Fulcio, Rekor, in-toto, Syft, Grype, Trivy |
| Platform engineering | IDP, catalog, golden paths, platform APIs, control planes, self-service, tenancy | Backstage, Crossplane, Karpenter, KEDA, Humanitec, Port, Cortex |
| SRE and incident | SLI/SLO, error budgets, on-call, incident command, postmortem, chaos, RPO/RTO | Prometheus, Grafana, PagerDuty, Opsgenie, Litmus, Chaos Mesh |
| Observability | Metrics, logs, traces, profiles, sampling, cardinality, retention, telemetry pipelines | OpenTelemetry, Prometheus, Grafana, Loki, Tempo, Jaeger, Mimir, VictoriaMetrics, eBPF |
| Storage infrastructure | Block/file/object, SAN/NAS, Fibre Channel, iSCSI, NVMe-oF, RAID, snapshots, replication | Ceph, ZFS, LVM, NetApp, Dell PowerStore, Pure Storage, MinIO, S3 |
| Database infrastructure | HA, replication, failover, WAL/binlog, PITR, pooling, sharding, compaction, persistence | PostgreSQL, Patroni, repmgr, MySQL InnoDB Cluster, ProxySQL, PgBouncer, MongoDB, Redis, Cassandra |
| Edge and CDN | Offline autonomy, fleet lifecycle, OTA, local orchestration, cache key, TTL, purge, origin shield | K3s, KubeEdge, MicroK8s, Cloudflare, CloudFront, Fastly, Akamai |
| Hardware/data center | Bare metal, PXE/iPXE, BMC, Redfish, IPMI, UEFI, Secure Boot, rack, PDU, UPS, cooling, DCIM | MAAS, Metal3, Tinkerbell, Redfish, OpenBMC, Open Compute Project, DCIM platforms |
| Asset/architecture governance | CMDB, source of truth, ownership, configuration items, NFRs, ADRs, dependency graph, lifecycle | NetBox, ServiceNow CMDB, cloud asset inventory, ADRs |

## Boundary rules

- Infrastructure database operations cover availability, replication, backup, patching, capacity and failover. Data-domain database engineering covers schema, SQL semantics, modeling and analytical workloads.
- Infrastructure storage covers storage systems and durability. Data Engineering covers table formats, lakehouse metadata and data lifecycle semantics.
- Infrastructure networking covers enterprise and cloud network foundations. Telecommunications covers carrier networks, radio access, 5G core and telecom signaling.
- Infrastructure security covers control-plane, host, network and cloud foundations. Enterprise cybersecurity remains a separate cross-domain specialization.
- Kubernetes is a runtime/orchestration platform, not a substitute for cloud, network, storage, security, SRE or platform engineering.
