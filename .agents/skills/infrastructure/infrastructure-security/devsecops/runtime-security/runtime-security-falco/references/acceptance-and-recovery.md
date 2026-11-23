# runtime-security-falco: specialist evaluation and negative controls

Domain `infrastructure/infrastructure-security/devsecops/runtime-security`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. **Establish coverage.** Identify monitored hosts, containers and attack behaviors. Map each detection to a Falco rule, an event source and an output destination. Falco's `syscall` source relies on a kernel driver; plugin event sources are separate and Falco does not natively correlate events across different sources. Do not claim coverage for events that cannot be observed.
2. **Preflight versions and privileges.** Inspect `falco --version`, `uname -r`, intended driver configuration and installation manifests. Falco 0.38+ defaults to bundled modern eBPF when compatible; otherwise assess the supported kernel-module route for the exact environment. Confirm BPF permissions, required kernel capabilities and any SELinux/host restrictions. Do not request unrestricted privileged access as a shortcut or claim that kernel-module availability proves detection readiness.
3. **Pin and validate artifacts.** Pin the Falco distribution, chart and rule/plugin artifact versions supported by the target installation. Verify signatures and artifact provenance where available. Inspect rule file order; validate the complete intended rule set with the version-compatible `falco --validate <rules_file>` option (multiple files in load order where applicable). Record parser errors and unresolved fields 

## Challenge / acceptance
- **Challenge:** Inject compromised dependency, stale token and policy bypass. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Prevent unauthorized actions, preserve audit trail and verify remediation. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - **Driver missing or blocked:** distinguish modern eBPF precondition failure from kernel-module/driver mismatch. Check kernel and security policy evidence, revert the deployment if host access cannot be safely granted; never downgrade host security blindly.
- **Kernel event drops or overload:** inspect collector/drop counters and resource saturation before tuning ring buffers or scaling; document blind spots and prevent a misleading healthy status.
- **Rules silently ineffective:** confirm loaded rules, event source, plugin availability, rule priority and changed rule-file order. Revert incompatible overrides and re-run an approved test event.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://falco.org/docs/setup/download/
- https://falco.org/docs/concepts/event-sources/
- https://falco.org/docs/concepts/rules/overriding/
- https://falco.org/docs/reference/daemon/cli-arguments/
- https://falco.org/docs/concepts/metrics/
- https://falco.org/docs/troubleshooting/dropping/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
