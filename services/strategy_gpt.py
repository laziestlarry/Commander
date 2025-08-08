import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
MEMORY_FILE = "data/strategy_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_memory(memory):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)

def generate_strategy(topic):
    memory = load_memory()
    history = [{"role": "system", "content": "You are a business strategist AI."}]

    # Add last 3 successful strategies to context
    for entry in memory[-3:]:
        history.append({"role": "user", "content": f"Topic: {entry['topic']}"})
        history.append({"role": "assistant", "content": entry["strategy"]})

    prompt = f"Create a 5-step business strategy to launch a product about: {topic}"
    history.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=history,
        max_tokens=400
    )

    strategy = response['choices'][0]['message']['content']

    # Save to memory
    memory.append({"topic": topic, "strategy": strategy})
    save_memory(memory)


    # Optional Agent Feedback Hook
    from agents.cua_agent import CUAAgent
    from db.models import engine as db_engine
    agent = CUAAgent(db_engine, persona="📩 Strategy Learner")
    agent.realize_plan([{"action": "store_data", "payload": {"key": topic, "value": strategy}}])
    return strategy