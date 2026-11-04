# Domain Taxonomy — Authoritative YAML Graph

The master graph contains 41 top-level discovery domains, each with at least one active skill. Many subdomain nodes remain **mapped** placeholders. The taxonomy is intentionally extensible, not a claim to cover every discipline in the world.

| Domain ID | Purpose |
|---|---|
| data | Data Engineering, Data Science, Data Analysis, BI, distributed processing, warehouses and governance |
| infrastructure | Kubernetes, DevOps, cloud, networking, Linux and platform engineering |
| software-engineering | Backend, frontend, software architecture, programming and testing |
| ai-ml | LLM engineering, RAG, model evaluation, ML and MLOps |
| agent-systems | Capability routing, agent skill authoring, tools and evaluations |
| security | Application, cloud, identity, privacy and incident security |
| product | Discovery, PRDs, metrics, experiments and roadmaps |
| marketing | GTM, channels, brand, lifecycle, marketing analytics |
| seo | Technical SEO, structured data, indexability and organic performance |
| design | UX, UI, accessibility, interaction and design systems |
| research | Evidence synthesis, fact checking and technical writing |
| business | Strategy, operating models and business analysis |
| content | Editorial planning, copywriting and publishing |
| people | Recruiting, people operations and organizational development |
| education | Curriculum, instructional design, tutoring and assessment |
| finance | Accounting, corporate finance, treasury and investing research |
| legal | Legal information, contract review and regulatory research |
| health | Healthcare information, public health and biomedical research |
| science | Mathematics, physics, chemistry, biology and scientific computing |
| ecommerce | Commerce platforms, merchandising and inventory |
| sales | Sales strategy, operations, analytics and enablement |
| customer-experience | Customer support, success, knowledge bases and feedback |
| media | Media, publishing, film, music and podcast production |
| gaming | Game development, game design and analytics |
| manufacturing | Industry, manufacturing automation, quality and maintenance |
| logistics | Transport, warehousing, last-mile and supply chain planning |
| construction | Architecture, BIM, civil engineering and construction planning |
| energy | Energy systems, renewables and sustainability |
| agriculture | Agriculture, food production and agribusiness |
| public-sector | Public policy, public services and civic technology |
| travel | Travel, tourism, hospitality and events |
| sports | Fitness, athletic coaching and sports science |
| personal | Productivity, organization and personal planning |

| robotics | Robotics, perception, controls and autonomous systems |
| telecommunications | Telecom networks, radio access and connectivity |
| aerospace | Avionics, aerospace engineering and space missions |
| social-sciences | Sociology, economics, demography and research methods |
| humanities | History, philosophy, languages and cultural heritage |
| environment | Environmental science, ecology and biodiversity |
| real-estate | Property management, analytics and valuation research |
| nonprofit | Grant management, volunteering and social impact |

## Governance

Add a new domain only when task boundaries and routing tests justify it. Every proposed active node needs a validated path to a maintained Skill. For regulated or high-impact work, mapped status is preferred to publishing a generic untested pseudo-expert.

See `catalog/root.yaml`, `docs/SKILL_COVERAGE.md` and `tests/fixtures/yaml-routing-cases.yaml` for executable coverage and regression evidence.

## Expanded first-class subdomains

- `data/data-science`: statistical inference, causal analysis, sklearn validation, feature engineering, forecasting, EDA, geospatial and anomaly detection.
- `data/data-analysis`: SQL metrics, cohorts, funnels, experiment result analysis, Polars, visualizations and reconciliation.
- `data/business-intelligence`: Apache Superset and dashboard evidence.
- `ai-ml/{llm-engineering,rag-retrieval,machine-learning,deep-learning,mlops}`: fine-grained specialist selection.
- `infrastructure/{kubernetes,devops-sre,cloud-engineering,network-engineering,linux-systems,platform-engineering}`: dedicated skill registries and nested maps.
- `data/data-engineering`: additional CDC, object storage, metadata catalogs and analytical databases.

All new paths preserve the root `AGENTS.md` instruction bootstrap, YAML progressive disclosure and explicit personal skill overlay registration.
