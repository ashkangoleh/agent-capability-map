---
name: technical-writing-docs
description: Use when creating or improving technical documentation, architecture records, runbooks, API documentation, tutorials, or engineering reports.
license: Proprietary
metadata:
  version: "1.0.1"
---

# Purpose

Produce accurate, maintainable technical documents that help a defined audience complete a task or make a decision.

## Inputs and prerequisites

Identify audience, document purpose, source artifacts, product/version scope, ownership, and maintenance expectations.

## Procedure

1. Choose the document type: guide, reference, tutorial, explanation, runbook, RFC, ADR, or report.
2. Inspect actual implementation, configuration, API schema, and authoritative references.
3. Define prerequisites, scope, non-goals, and terminology.
4. Organize around the reader's task or decision, not the author's chronology.
5. Include runnable examples only when syntax and behavior are verified.
6. Distinguish normative requirements, observed behavior, assumptions, and recommendations.
7. Add failure modes, troubleshooting, security notes, and version compatibility where relevant.
8. Check links, examples, commands, headings, and consistency.
9. Identify owner and review trigger for volatile documentation.

## Evidence requirements

Do not document an endpoint, parameter, configuration key, or behavior unless verified in code, schema, or official documentation. Never invent examples that look production-real.

## Output contract

Deliver the complete document with audience, scope, prerequisites, main content, examples, limitations, and maintenance notes appropriate to its type.

## Failure modes and abstention

If implementation evidence is missing, mark the section as unverified or ask for the source. Do not fill gaps with conventional but unverified API behavior.

## Validation checklist

- [ ] Audience and purpose are clear.
- [ ] Implementation claims were verified.
- [ ] Examples are valid or labeled illustrative.
- [ ] Version scope is explicit.
- [ ] Links and commands were checked.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
