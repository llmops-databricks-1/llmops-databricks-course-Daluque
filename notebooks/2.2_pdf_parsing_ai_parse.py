# Databricks notebook source
# MAGIC %md
# MAGIC # Lecture 2.2: PDF Parsing with AI Parse Documents
# MAGIC
# MAGIC ## Topics Covered:
# MAGIC - Downloading and storing PDFs
# MAGIC - AI Parse Documents for intelligent parsing
# MAGIC - Comparison with other PDF parsing tools
# MAGIC - Storing parsed content in Delta tables

# COMMAND ----------
# %pip install ../arxiv_curator-0.1.0-py3-none-any.whl
# COMMAND ----------

from databricks.connect import DatabricksSession
from loguru import logger

from arxiv_curator.config import get_env, load_config
from arxiv_curator.data_processor import DataProcessor

# COMMAND ----------

spark = DatabricksSession.builder.getOrCreate()
logger.info("✅ Using Databricks Connect Spark session")

env = get_env(spark)
cfg = load_config("../project_config.yml", env)

# Initialize the DataProcessor (reusable class from arxiv_curator package)
processor = DataProcessor(spark=spark, config=cfg)

logger.info(
    f"Catalog: {cfg.catalog}, Schema: {cfg.schema}, "
    f"Volume: {cfg.volume}, ArXiv Query: {cfg.arxiv_query}"
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. PDF Parsing Tools Comparison
# MAGIC
# MAGIC | Tool | Pros | Cons | Best For |
# MAGIC |------|------|------|----------|
# MAGIC | **AI Parse** | AI-powered | Databricks-only | Complex docs |
# MAGIC | **PyPDF2** | Simple, free | Poor layouts | Simple text |
# MAGIC | **pdfplumber** | Good tables | Manual tuning | Structured |
# MAGIC | **Apache Tika** | Multi-format | Java, heavy | Multi-format |
# MAGIC | **Unstructured** | ML-powered | External svc | RAG |
# MAGIC
# MAGIC **AI Parse Documents** is recommended for Databricks users.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Download PDFs, Parse, and Create Chunks
# MAGIC
# MAGIC The `DataProcessor` class handles the full pipeline:
# MAGIC 1. Download PDFs for unprocessed papers from arXiv
# MAGIC 2. Update `arxiv_papers` table with timestamps
# MAGIC 3. Parse PDFs using AI Parse (`ai_parse_document`)
# MAGIC 4. Extract and clean text chunks with metadata
# MAGIC 5. Write chunks to `arxiv_chunks` table (CDF enabled)
# MAGIC
# MAGIC Also used in `resources/deployment_scripts/process_data.py`.

# COMMAND ----------

processor.process_and_save()
