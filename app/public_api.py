from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/api/scores")
def get_scores():
    with open("data/agent_scores.json") as f:
        return json.load(f)

@app.get("/api/strategy")
def get_memory():
    with open("data/strategy_memory.json") as f:
        return json.load(f)