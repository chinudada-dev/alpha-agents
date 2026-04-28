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

## Run the web app

Start the FastAPI server:

```bash
uvicorn app.app:app --reload
```

Then open `http://127.0.0.1:8000/` for the frontend and `http://127.0.0.1:8000/health` for the API health check.

## Deploy on Railway

This repo now includes a [railway.json](/Users/apple/PycharmProjects/alpha-agents/railway.json) config file for Railway.

1. Push the repo to GitHub.
2. In Railway, create a new project and choose `Deploy from GitHub repo`.
3. Select this repository.
4. Railway will install dependencies from `requirements.txt`.
5. Railway will start the app with `uvicorn app.app:app --host 0.0.0.0 --port $PORT`.
6. After deploy finishes, open the service settings and click `Generate Domain` to make the site public.

If you later enable the RAG pipeline in production, add `OPENAI_API_KEY` in the Railway service variables.
