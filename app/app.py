from fastapi import FastAPI

app = FastAPI(title="Agentic AI Stocks API")


@app.get("/health")
def health_check():
    return {"status": "ok"}
