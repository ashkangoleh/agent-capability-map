# Master Skill Coverage — 2026-11-03

## Scope

- Top-level domains: 33, mapped for discovery and future expansion.
- Active skill packages: 30 (12 newly added in this expansion).
- Distinction: a mapped node is discoverable taxonomy but may not provide an executable skill.
- The router remains deterministic lexical routing, not semantic retrieval. Auto-activation in other hosts is not certified by a passing registry test.

## New specialist packages

| Capability | Skill ID | Source baseline / verification |
|---|---|---|
| dbt incremental correctness | `dbt-incremental-modeling` | dbt incremental models / strategy docs |
| Data contracts / quality | `data-quality-contracts` | dbt data tests, source assertions |
| Backfill / replay | `pipeline-backfill-recovery` | source/sink recovery contracts, Airflow/dbt docs |
| Spark Structured Streaming | `spark-structured-streaming` | version-specific Spark structured-streaming guide |
| Kubernetes rollout | `kubernetes-rollout-safety` | Kubernetes deployment and Helm official docs |
| Product A/B experiments | `product-experiment-design` | experimentation methodology and instrumentation |
| Product instrumentation | `product-metrics-instrumentation` | Google Analytics events and event validation |
| Marketing measurement | `marketing-measurement-attribution` | Google Analytics event measurement/validation |
| SEO crawl/indexation | `seo-indexability-diagnostics` | Google Search Central crawling/indexing |
| SEO rich results | `seo-structured-data-validation` | Google structured-data guidelines |
| Agent evaluation | `agent-evaluation-suite` | Agent Skills specification and evaluation guidance |
| Content/editorial | `content-editorial-brief` | Google helpful content guidance |

## Quality policy

Every specialist SKILL.md includes:
1. Activation boundary and exact deliverable.
2. Input and version requirements.
3. Operational procedure, including failure scenarios.
4. Official reference starting points and freshness checks.
5. Explicit uncertainty and abstention conditions.
6. Output and verification contract.

No measured hallucination reduction, token savings or all-host compatibility is claimed. The regression fixture set checks whether the deterministic resolver chooses the expected path, not whether an LLM completes the work correctly.

## Examples

    capability-map resolve --request "Design a dbt incremental model with merge and unique_key"
    capability-map resolve --request "Create a data quality contract for daily orders"
    capability-map resolve --request "Design a product A/B test with guardrail metrics"
    capability-map resolve --request "Implement GA4 event tracking for marketing conversions"
    capability-map resolve --request "Diagnose canonical mismatch on indexed pages"
    capability-map resolve --request "Prepare a content strategy editorial brief for a product launch"

## Acceptance before publishing a new specialist as production-ready

- Verify versions and citations against official docs, including any APIs used.
- Evaluate on positive, negative, near-miss, ambiguous and adversarial task sets.
- Review sampled outputs for correctness, safety, evidence support and task completion.
- Benchmark actual agent token usage; the number of YAML files read is not a token-cost benchmark.
- Record which host and model versions were tested and remaining failures.
