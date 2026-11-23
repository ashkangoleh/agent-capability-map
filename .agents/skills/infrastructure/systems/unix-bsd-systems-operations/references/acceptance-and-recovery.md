# unix-bsd-systems-operations: specialist evaluation and negative controls

Domain `infrastructure/systems`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Identify exact OS family, release and architecture before choosing commands or configuration paths.
2. Inspect boot loader, kernel modules, rc/service framework, packages, filesystems and network configuration using native tools.
3. Review PF, jails, MAC controls, secure levels, SSH, package signatures and supported update paths.
4. Preserve boot environments, snapshots or verified backups before kernel, storage or network changes.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not copy Linux systemd, iproute2 or package commands to BSD without verifying equivalents.
- Kernel or bootloader changes can make remote hosts unbootable; retain console recovery.
- Filesystem, jail and network semantics differ by OS and release.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.freebsd.org/en/books/handbook/
- https://www.openbsd.org/faq/
- https://man.netbsd.org/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
