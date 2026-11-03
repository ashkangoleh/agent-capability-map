# Coverage charter

This repository is intended to be a comprehensive library of **ready-to-use Agent Skills**, not merely an example router. Coverage is open-ended: new tools and disciplines can be added without increasing the size of the root agent instructions.

## Coverage levels

- **Mapped:** A domain, product or technology has a discoverable taxonomy entry; no usable skill is implied.
- **Draft:** A concrete SKILL.md exists, but correctness, references and routing have not all been reviewed.
- **Active:** A usable SKILL.md has passed structural validation and domain-specific review. This does not prove host-agent routing accuracy.
- **Verified:** In addition to being active, a representative task and client-specific routing/execution evaluation has passed.

Do not equate a mention in this document or in a YAML manifest with a completed skill. Do not promise universal coverage until the corresponding leaf skills exist.

## Required breadth

- **Data engineering:** ETL/ELT, CDC, batch, streaming, lakehouse, OLTP/OLAP/HTAP, SQL, DB administration, modeling, storage formats, orchestration, data quality, catalog, lineage, privacy and governance. Include Spark/PySpark/Scala, Flink, Beam, Kafka, Pulsar, Airflow, Dagster, Prefect, dbt, Iceberg, Delta, Hudi, Trino, StarRocks, ClickHouse, PostgreSQL, MySQL, MongoDB, Redis, Cassandra, DuckDB, Snowflake, BigQuery and Redshift.
- **Data science, analytics and ML:** Statistics, experiment design, BI, semantic layers, metrics, forecasting, feature engineering, model training and evaluation, traditional ML, deep learning, inference, MLOps, LLM applications, RAG, agents, prompts, security and evaluations. Include scikit-learn, XGBoost, PyTorch, TensorFlow, MLflow and Kubeflow as candidates, not automatic active skills.
- **Cloud and infrastructure:** AWS, Google Cloud and Azure across data, networking, compute, identity, storage, managed services, monitoring and deployment. Include Kubernetes, containers, Terraform/OpenTofu, Ansible, CI/CD, DevOps, SRE, DevSecOps, security, observability, reliability and cost management.
- **Networking and datacenter:** TCP/IP, DNS, HTTP/TLS, L2/L3, BGP, firewalls, proxies, load balancing, CDN, VPN, SD-WAN, bare metal, Linux, virtualization, on-premises networking, storage, backups, disaster recovery and facilities operations.
- **Software engineering:** Backend, frontend, mobile, distributed systems, APIs, testing, security, architecture, databases, CI/CD and developer tooling. Include Python (FastAPI, Django), Go, Java/Kotlin (Spring), Node.js/TypeScript, .NET, PHP (Laravel), Rust, React, Vue, Angular, Next.js, Android and iOS.
- **Product and business:** Research, problem discovery, PRDs, roadmaps, pricing, experimentation, product analytics, business models, financial modeling, business intelligence, operations, procurement, sales and customer success.
- **Marketing and SEO:** Brand, positioning, go-to-market, channels, paid media, lifecycle/CRM, attribution, content and social, technical SEO, content SEO, local/international SEO, analytics, structured data and search engine guidance.
- **Other professional disciplines:** UX and design, writing, education, people/leadership, privacy/compliance, governance, risk and evidence-based research.

## Authoring rules

Maintain a deep but navigable folder hierarchy for **authors**, and preserve each skill as an independently usable, narrowly scoped package. A technology belongs in the taxonomy even before its active skill exists; maintain a public gap list. Do not create placeholder SKILL.md files that impersonate implementation.

Categorize primarily by **user intent and deliverable**, not by vendor-name coincidence. A cross-domain request (for example PySpark -> Iceberg -> ClickHouse CDC) may select multiple independent skills. The host agent remains responsible for the actual implementation.

Use a compact master index and selected-domain manifests for discovery; avoid eagerly loading all domains, technology names or SKILL.md bodies. Client-specific installation and discovery must be separately verified. A large catalog is a roadmap, not a passing routing benchmark.

## Prioritization

Develop complete vertical slices with verified references and real tasks, then widen coverage. Prioritize broadly applicable workflows and commonly requested tools, with a clear status indicator. Evaluate routing selection, factual support, correctness, loaded-context size, and token consumption before claiming an advantage over other skill libraries.
