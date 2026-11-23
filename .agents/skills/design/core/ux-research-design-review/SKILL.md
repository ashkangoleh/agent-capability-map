---
name: ux-research-design-review
description: Use when planning UX research, evaluating a user journey or interface, reviewing interaction patterns, design systems, or accessibility.
license: Proprietary
metadata:
  version: "1.0.1"
---

# Purpose

Evaluate user experience with explicit evidence, usability principles, accessibility criteria, and testable recommendations.

## Inputs and prerequisites

Identify user group, task, platform, design artifact, business context, accessibility target, and whether real user research or only heuristic review is available.

## Procedure

1. State the evaluation method and evidence level: observed user test, analytics, expert heuristic, or design hypothesis.
2. Map the user goal and task flow.
3. Review information architecture, discoverability, feedback, error prevention, recovery, consistency, and cognitive load.
4. Check accessibility with the relevant standard and actual tests; do not claim conformance from visual inspection alone.
5. Rank issues by user impact, frequency evidence, severity, and implementation effort.
6. Recommend specific changes and define how to validate them.
7. Separate measured findings from heuristic opinions.

## Evidence requirements

Use supplied screens, flows, prototypes, usability sessions, analytics, design system documentation, and authoritative accessibility standards. Never invent user-test observations.

## Output contract

Provide method, context, findings, severity, rationale, recommendation, and validation plan.

## Failure modes and abstention

Do not generalize from one screenshot to the whole product. Do not claim WCAG conformance without sufficient testing.

## Validation checklist

- [ ] Method and evidence level are explicit.
- [ ] Findings are tied to a task or user need.
- [ ] Severity is justified.
- [ ] Accessibility claims are test-backed.
- [ ] Recommendations are testable.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
