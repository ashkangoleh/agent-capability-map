# container-runtime-operations: specialist evaluation and negative controls

Domain `infrastructure/containers/runtime`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Identify runtime, shim, OCI runtime, kernel and cgroups version; verify compatibility.
2. Inspect image provenance, digest, user, capabilities, mounts and entrypoint.
3. Set CPU/memory/pid limits, seccomp, MAC profile, read-only filesystem and rootless mode.
4. Validate overlay storage, inode capacity, garbage collection and scoped registry credentials.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Cgroup v1/v2 differences alter enforcement; inspect effective hierarchy.
- Overlay exhaustion can block workloads; monitor bytes and inodes.
- Privileged containers or host mounts defeat isolation.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://opencontainers.org/
- https://containerd.io/docs/
- https://docs.podman.io/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
