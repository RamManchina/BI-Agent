from fastapi import FastAPI
from pydantic import BaseModel
from monday_client import fetch_board_items
from data_cleaner import normalize_items
from analytics import compute_metrics
from llm import generate_answer

app = FastAPI(title="Founder BI Agent")

class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "Founder BI Agent is live"}

@app.post("/ask")
def ask_agent(query: Query):
    raw = fetch_board_items()
    cleaned = normalize_items(raw)
    metrics = compute_metrics(cleaned)
    answer = generate_answer(metrics, query.question)

    return {
        "metrics": metrics,
        "answer": answer
    }
