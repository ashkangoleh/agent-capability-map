# robotics-ros2-interface-review: specialist evaluation and negative controls

Domain `robotics/core`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Inspect the actual ROS 2 distribution and graph rather than assuming middleware defaults.
2. Define each topic, service and action contract: message type, units, frame IDs, rate and ownership.
3. Choose reliability, durability and history QoS per communication requirement and record incompatible combinations.
4. Separate simulation validation from robot-hardware testing, with explicit emergency stop, operator approval and fail-safe boundaries.

## Challenge / acceptance
- **Challenge:** Inject sensor delay, localization loss or actuator fault in simulation. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Bounded safety envelope and stop control validated before any hardware test. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No physical robot actuation without explicit approval and safety case. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.ros.org/en/rolling/Concepts/Intermediate/About-Quality-of-Service-Settings.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
