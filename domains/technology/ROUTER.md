# Technology Domain Router

Use for software delivery, architecture, platform operations, cloud, APIs, testing, reliability, and security engineering.

1. Read this domain's skills.json only.
2. Match the requested deliverable, not just the technology named.
3. Code changes and code review route to software-engineering-implementation.
4. Kubernetes, deployment, infrastructure, incidents, and operational runbooks route to platform-operations.
5. If the task is primarily data platform or data pipeline work, route to the data domain instead.
6. If it is LLM, agent, or retrieval system design, route to ai-ml.
7. Load one skill by default. Add a second only for a distinct required workstream.
8. For production changes, require inspection, tests, rollout, rollback, and failure-mode analysis. Never infer that a command is safe from its name alone.

## Phase-one infrastructure and network capability boundaries

Treat infrastructure as a major user-facing route under the technology root, with four explicit specializations:
- DevOps: CI/CD, release automation, artifact promotion -> devops-delivery.
- DevSecOps: supply chain security, least-privilege build/release, secrets -> devsecops-review.
- Platform Engineering: developer self-service platforms, golden paths and provisioning -> platform-engineering-workflows.
- SRE: incidents, SLI/SLOs, error budgets and recovery -> sre-incident-response.
For network troubleshooting (DNS, TCP, TLS, routing, proxies and firewalls), route to network-diagnostics.
The broad platform-operations skill remains available for general infrastructure tasks without a specialized deliverable. Do not preload all five specialized skills simply because the user mentioned infrastructure.
