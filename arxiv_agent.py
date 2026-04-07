import mlflow
from mlflow.models import ModelConfig

from arxiv_curator.agent import ArxivAgent

config = ModelConfig(
    development_config={
        "catalog": "site",
        "schema": "ai_library_dev",
        "genie_space_id": "01f1315002321eed9477cd90308b379b",
        "system_prompt": "prompt placeholder",
        "llm_endpoint": "databricks-qwen3-next-80b-a3b-instruct",
        "lakebase_project_id": "arxiv-agent-lakebase",
    }
)

agent = ArxivAgent(
    llm_endpoint=config.get("llm_endpoint"),
    system_prompt=config.get("system_prompt"),
    catalog=config.get("catalog"),
    schema=config.get("schema"),
    genie_space_id=config.get("genie_space_id"),
    lakebase_project_id=config.get("lakebase_project_id"),
)
mlflow.models.set_model(agent)
