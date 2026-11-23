---
name: schema-registry-compatibility
description: "Govern Avro, Protobuf and JSON Schema evolution with subject naming, compatibility modes and producer/consumer rollout controls."
license: Proprietary
metadata:
  version: "1.1.1"
---

# schema-registry-compatibility

## Activation boundary
Use for schema registry and event/data contract compatibility. A registry compatibility check does not prove semantic compatibility or safe downstream transformation.

## Required context
Registry/version; format; subject naming; producer/consumer versions; compatibility mode; key/value schema; references; replay horizon.

## Production procedure
1. Identify subject naming strategy for key and value separately; verify topic, record and tenant mapping.
2. Choose BACKWARD, FORWARD, FULL or transitive compatibility from all supported versions, not only the previous version.
3. For Avro inspect defaults, unions, aliases and logical types; for Protobuf preserve field numbers and reserve removed names/numbers; for JSON Schema inspect required fields, references and dialect.
4. Register and validate schemas in CI before producers deploy. Deploy tolerant consumers first when required by compatibility direction.
5. Test historical payload replay, mixed-version consumers, tombstones, key changes and schema references.
6. Define registry export/backup, subject ownership, deletion policy and emergency override process.

## Failure modes and recovery
- Registry accepts a change but consumers break: run semantic and replay tests; compatibility mode is not an application contract.
- Wrong subject naming creates parallel subjects: inspect actual subject before registering.
- Protobuf field number reuse corrupts wire compatibility: reserve removed numbers permanently.
- Registry outage breaks schema lookup: define cache and producer failure behavior.

## Validation and acceptance
- Test every supported producer/consumer version combination and replay old payloads.
- Validate key and value schema independently.
- Test registry outage, cache expiry, references and rollback.
- Record schema version, compatibility mode, ownership and CI evidence.

## Output contract
Return subject strategy, format-specific compatibility analysis, rollout order, replay tests and explicit semantic risks.

## Official or primary references
- https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html
- https://www.apicur.io/registry/docs/apicurio-registry/3.0.x/getting-started/assembly-what-is-apicurio-registry.html

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
