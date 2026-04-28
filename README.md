# Agentic AI Stocks

This project is a starter RAG-based agent system for stock and company news analysis.

## Structure

```text
aplha-agents/
├── agents/
│   ├── ingestion_agent.py
│   └── analysis_agent.py
├── app/
│   └── app.py
├── chroma_db/
├── frontend/
│   └── index.html
├── rag/
│   └── rag_store.py
├── config.py
├── requirements.txt
└── README.md
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key:

```bash
export OPENAI_API_KEY="your-api-key"
```

4. Optional: set the project root on `PYTHONPATH` if you run into import issues:

```bash
export PYTHONPATH=$(pwd)
```

## Run ingestion

From inside `aplha-agents`:

```bash
python agents/ingestion_agent.py
```

## Verify storage

After ingestion runs, check:

```bash
ls chroma_db/
```
