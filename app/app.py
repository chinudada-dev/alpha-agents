from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="Agentic AI Stocks API")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FRONTEND_FILE = PROJECT_ROOT / "frontend" / "index.html"


@app.get("/", include_in_schema=False)
def serve_frontend():
    return FileResponse(FRONTEND_FILE)


@app.get("/health")
def health_check():
    return {"status": "ok"}
