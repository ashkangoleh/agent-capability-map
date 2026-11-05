---
name: runtime-security-falco
description: "Deploy runtime threat detection with Falco rules, signal quality, response ownership and safe tuning."
metadata:
  version: "1.1.0"
---

# runtime-security-falco

## Activation boundary
Use for Falco deployment, runtime rule changes, kernel event-source coverage, detection troubleshooting, alert-pipeline reliability and safe Falco upgrades. This is not a SAST/DAST pipeline or generic image-scanning procedure.

## Required context
Exact Falco binary/image and Helm chart versions, deployment mode (host or Kubernetes), kernel release/architecture, driver selection (modern eBPF or kernel module), kernel capabilities/BTF and host security policy, intended event sources/plugins, ruleset and its load order, monitored nodes and namespaces, detection use cases, output integration, event/drop metrics, on-call owner, data handling limits and rollback path. Treat unprovided values as unknown.

## Production procedure
1. **Establish coverage.** Identify monitored hosts, containers and attack behaviors. Map each detection to a Falco rule, an event source and an output destination. Falco's `syscall` source relies on a kernel driver; plugin event sources are separate and Falco does not natively correlate events across different sources. Do not claim coverage for events that cannot be observed.
2. **Preflight versions and privileges.** Inspect `falco --version`, `uname -r`, intended driver configuration and installation manifests. Falco 0.38+ defaults to bundled modern eBPF when compatible; otherwise assess the supported kernel-module route for the exact environment. Confirm BPF permissions, required kernel capabilities and any SELinux/host restrictions. Do not request unrestricted privileged access as a shortcut or claim that kernel-module availability proves detection readiness.
3. **Pin and validate artifacts.** Pin the Falco distribution, chart and rule/plugin artifact versions supported by the target installation. Verify signatures and artifact provenance where available. Inspect rule file order; validate the complete intended rule set with the version-compatible `falco --validate <rules_file>` option (multiple files in load order where applicable). Record parser errors and unresolved fields before rollout. Do not silently reinterpret incompatible rules.
4. **Tune rules with evidence.** Prefer local override rules loaded after vendor defaults, using current `override` append/replace semantics and explicit scoped exceptions. Avoid deprecated legacy `append: true` syntax for new rule changes. Verify event-source-specific fields and rule priorities; never globally disable high-signal rules just to lower alert volume. Keep each exception owned, justified, narrow and expiring.
5. **Roll out safely.** Deploy to staging or a bounded node/pod canary first, with explicit stop conditions for startup failures, syscall drops, CPU overhead and sink backpressure. Confirm rule-file hashes/reload state, driver initialization, plugin loading, alert forwarding and redaction of sensitive process/command data. Only expand coverage after representative workload observation.
6. **Instrument detection health.** Enable Falco metrics intentionally and monitor kernel-side drops (`scap.n_drops` and drop rate where exposed), event rates, rule firing, CPU/memory use and `falco.outputs_queue_num_drops`. The official metrics settings include `metrics.enabled`, `kernel_event_counters_enabled`, `rules_counters_enabled` and `resource_utilization_enabled`. If Prometheus is required, explicitly review and protect the optional webserver `prometheus_metrics_enabled` endpoint. An up process with event loss or broken output delivery is not healthy.
7. **Verify detection and alert delivery.** Run an approved, benign and reproducible test event for each critical rule in an isolated test workload. Verify the expected event source, Falco rule name, output destination, incident ownership, alert latency and absence of unintended private fields. Measure false positives against baseline traffic; never fabricate a detection-rate or zero-loss guarantee.
8. **Publish/rollback gate.** Record config/rules versions, rollout cohort, observed metrics, accepted residual risk, named approver and the last known-good image/ruleset. Roll back on sustained event loss, incompatible rule loads, excessive noise, unexpected privilege increases or sink failures; then recheck both kernel collection and end-to-end alert delivery.

## Failure modes and recovery
- **Driver missing or blocked:** distinguish modern eBPF precondition failure from kernel-module/driver mismatch. Check kernel and security policy evidence, revert the deployment if host access cannot be safely granted; never downgrade host security blindly.
- **Kernel event drops or overload:** inspect collector/drop counters and resource saturation before tuning ring buffers or scaling; document blind spots and prevent a misleading healthy status.
- **Rules silently ineffective:** confirm loaded rules, event source, plugin availability, rule priority and changed rule-file order. Revert incompatible overrides and re-run an approved test event.
- **False positives and exhausted outputs:** use precise scoped exceptions and bounded alert rates, not wholesale disabling; monitor output queue drops and consumer availability, and restore last known-good output configuration if delivery fails.
- **Unsafe rollout:** isolate affected nodes, stop further promotion, restore known-good signed artifacts and configs, verify startup and detection again. Record remaining coverage gaps and incident escalation criteria.

## Validation
Report the observed Falco version, driver and target kernel, exact ruleset/override versions, rule validation result, canary scope, syscall-drop and output-queue counters, test-event results, destination acknowledgments, false-positive assessment and rollback evidence. Separate tested outcomes from recommended checks. No claims of production execution without actual logs and artifacts.

## Official references
- https://falco.org/docs/setup/download/
- https://falco.org/docs/concepts/event-sources/
- https://falco.org/docs/concepts/rules/overriding/
- https://falco.org/docs/reference/daemon/cli-arguments/
- https://falco.org/docs/concepts/metrics/
- https://falco.org/docs/troubleshooting/dropping/
- https://falco.org/docs/troubleshooting/start-up-error/

## Output contract
Produce an environment-specific plan or diagnosis with evidence, exact version assumptions, driver/rules/alerts coverage, canary and rollback gates, observed test results and unresolved risks. Do not execute privileged changes, run simulated attacks or declare detector health without explicit authorization and measured evidence.
