<h1 align="center">
LLMOps Course on Databricks
</h1>

## Practical information
- Weekly lectures on Wednesdays 16:00-18:00 CET.
- Weekly Q&A on Mondays 16:00-17:00 CET.
- Code for the lecture is shared before the lecture.
- Presentation and lecture materials are shared right after the lecture.
- Video of the lecture is uploaded within 24 hours after the lecture.

- Every week we set up a deliverable, and you implement it with your own dataset.
- To submit the deliverable, create a feature branch in that repository, and a PR to main branch. The code can be merged after we review & approve & CI pipeline runs successfully.
- The deliverables can be submitted with a delay (for example, lecture 1 & 2 together), but we expect you to finish all assignments for the course before the demo day. OK.


## LLMOps Databricks official documentation

### Building GenAI Apps & Agents
- [Generative AI overview](https://docs.databricks.com/generative-ai/agent-framework/build-genai-apps) — Building generative AI apps on Databricks
- [Agent Framework](https://docs.databricks.com/generative-ai/agent-framework/author-agent) — Code-first agent authoring
- [Agent Bricks](https://docs.databricks.com/generative-ai/agent-bricks/) — Domain-specialized AI agents (Knowledge Assistants, Genie, Supervisors)
- [Foundation Model APIs](https://docs.databricks.com/machine-learning/foundation-model-apis) — Query LLMs via serving endpoints
- [AI Playground](https://docs.databricks.com/large-language-models/ai-playground) — Interactive LLM prototyping

### Model Serving & Deployment
- [Model Serving](https://docs.databricks.com/machine-learning/model-serving/) — Deploying ML and GenAI models to endpoints
- [Vector Search](https://docs.databricks.com/generative-ai/vector-search) — Embeddings and RAG retrieval

### MLflow & Experiment Tracking
- [MLflow for GenAI](https://docs.databricks.com/mlflow3/genai) — MLflow 3 for GenAI lifecycle (tracing, evaluation, prompt engineering)
- [Model Registry](https://docs.databricks.com/mlflow/model-registry) — Model versioning and lifecycle
- [Manage Models in Unity Catalog](https://docs.databricks.com/machine-learning/manage-model-lifecycle/) — Governed model lifecycle

### CI/CD & Deployment Automation
- [Databricks Asset Bundles](https://docs.databricks.com/dev-tools/bundles/) — Programmatic resource management (jobs, pipelines, MLOps stacks)
- [GitHub Actions](https://docs.databricks.com/dev-tools/ci-cd/github) — CI/CD with GitHub Actions
- [CI/CD Best Practices](https://docs.databricks.com/dev-tools/ci-cd/best-practices) — Recommended CI/CD workflows
- [Lakeflow Jobs](https://docs.databricks.com/jobs/) — Orchestrating workflows

### Developer Tools
- [SDK for Python](https://docs.databricks.com/dev-tools/sdk-python) — Automating Databricks via Python
- [Databricks CLI](https://docs.databricks.com/dev-tools/cli/) — Command-line interface
- [Databricks Connect](https://docs.databricks.com/dev-tools/databricks-connect) — Local IDE to remote compute
- [Authentication](https://docs.databricks.com/dev-tools/auth/) — Auth for CLI, SDK, and APIs
- [REST API Reference](https://docs.databricks.com/api/workspace/introduction) — Full API docs

### Data & Governance
- [Unity Catalog](https://docs.databricks.com/data-governance/unity-catalog/) — Data governance
- [Data Lineage](https://docs.databricks.com/data-governance/unity-catalog/data-lineage) — Tracking data provenance
- [Feature Engineering](https://docs.databricks.com/machine-learning/feature-store/) — Feature store in Unity Catalog
- [Secret Management](https://docs.databricks.com/aws/en/security/secrets/) — Storing credentials securely

### Monitoring & Operations
- [System Tables](https://docs.databricks.com/admin/system-tables/) — Audit, lineage, billing data
- [Audit Logging](https://docs.databricks.com/admin/account-settings/audit-logs) — Event auditing
- [Cost Management](https://docs.databricks.com/admin/usage) — Usage monitoring and cost controls

### Reference
- [Notebooks](https://docs.databricks.com/notebooks/) — Notebook development
- [Serverless Compute](https://docs.databricks.com/compute/serverless/) — On-demand infrastructure
- [Best Practices](https://docs.databricks.com/getting-started/best-practices) — General platform guidance


## Set up your environment
In this course, we use serverless environment 4, which uses Python 3.12.
In our examples, we use UV. Check out the documentation on how to install it: https://docs.astral.sh/uv/getting-started/installation/

To create a new environment and create a lockfile, run:

```
uv sync --extra dev
```



