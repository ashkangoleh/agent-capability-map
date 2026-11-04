# Infrastructure Engineering Tool and Concept Matrix

| Domain | Open-source / self-managed tools | Commercial / managed ecosystems | Concepts |
|---|---|---|---|
| Linux / OS | Linux, systemd, eBPF, perf, bpftrace, LVM, mdadm, ZFS | RHEL, SUSE, Ubuntu Pro, Windows Server | kernel, cgroups, namespaces, boot, drivers, filesystems, resource limits |
| Virtualization | KVM, QEMU, Proxmox, Xen, OpenStack | VMware vSphere, Nutanix, cloud VMs | hypervisors, HA, live migration, snapshots, overcommit, NUMA |
| Containers | Docker, containerd, CRI-O, Buildah, Podman | ECR, GCR/Artifact Registry, ACR | OCI images, registries, layers, build cache, runtime isolation |
| Kubernetes | Kubernetes, Helm, Kustomize, Operators, Crossplane | EKS, GKE, AKS, OpenShift | scheduling, CRDs, controllers, RBAC, CNI, CSI, HPA/VPA, PDB, upgrades |
| Platform engineering | Backstage, Crossplane, Karpenter, KEDA, Argo CD, Flux | Humanitec, Port, cloud platform services | IDP, golden paths, self-service, control plane, service catalog |
| IaC / config | Terraform, OpenTofu, Pulumi, Ansible, Packer, CloudFormation | HCP Terraform, enterprise automation platforms | state, locking, modules, drift, imports, immutable images, policy |
| CI/CD / GitOps | GitHub Actions, GitLab CI, Jenkins, Tekton, Argo CD, Flux | GitHub/GitLab SaaS, hosted CI | runners, artifacts, promotion, rollback, provenance, reconciliation |
| DevSecOps | Trivy, Grype, Syft, Cosign, Sigstore, Falco, OPA, Kyverno | Snyk, Wiz, Prisma, Aqua, enterprise scanners | SBOM, SLSA, signing, attestation, SAST/DAST/SCA, admission, runtime defense |
| Secrets / identity | Vault, SPIFFE/SPIRE, cert-manager, External Secrets | Cloud KMS/Secrets Manager, HSM/PKI services | workload identity, short-lived credentials, rotation, mTLS, trust roots |
| Networking | FRR, BIRD, Cilium, Calico, Envoy, HAProxy, NGINX, WireGuard | Cloud VPC/VNet, hardware network vendors | TCP/IP, DNS, BGP, routing, NAT, MTU, firewall, proxy, VPN, TLS, PKI, IPAM |
| Service mesh | Istio, Linkerd, Consul Connect | Managed mesh services | mTLS, traffic shifting, retries, circuit breaking, gateways, telemetry |
| Observability / SRE | Prometheus, Grafana, Loki, Tempo, OpenTelemetry, Alertmanager, VictoriaMetrics | Datadog, New Relic, Dynatrace, Splunk | SLIs/SLOs, error budgets, burn rates, traces, logs, metrics, profiles, cardinality |
| Resilience | Chaos Mesh, LitmusChaos, Velero, Restic | Cloud backup and DR services | chaos experiments, backup immutability, RPO/RTO, failover, restore drills |
| Storage | Ceph, ZFS, LVM, Longhorn, Rook, MinIO | SAN/NAS vendors, S3/GCS/ADLS | block/file/object, replication, snapshots, rebuild, encryption, durability |
| Database operations | PostgreSQL, MySQL, PgBouncer, ProxySQL, Patroni | RDS, Cloud SQL, Azure Database | WAL/binlog, replication, failover, pooling, backups, upgrades, consistency |
| Cloud foundations | AWS, Google Cloud, Azure, OpenStack | Cloud landing-zone services | accounts/projects, IAM, regions, CIDR, private endpoints, quotas, egress, FinOps |

## Production operating concepts

Identity and least privilege; network segmentation; immutable artifacts; state locking; idempotent automation; reconciliation; capacity headroom; SLO/error budget; incident command; patch/upgrade compatibility; SBOM/provenance/signing; secrets rotation; backup restore drills; RPO/RTO; cost allocation; change windows; blast radius and rollback.

This is a taxonomy of major current infrastructure ecosystems, not a claim to enumerate every vendor, plugin or hardware platform. Select tools from requirements and operational ownership, not popularity alone.
