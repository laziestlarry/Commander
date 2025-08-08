from agents.cua_agent import CUAAgent
from db.models import engine as db_engine
import random

class AgentManager:
    def __init__(self):
        self.agents = {
            "planner": CUAAgent(db_engine, persona="🌱 Visionary Planner: Thinks long-term, eco-conscious."),
            "executor": CUAAgent(db_engine, persona="⚙️ Precision Executor: Focused on details, speed, and results."),
            "reviewer": CUAAgent(db_engine, persona="🕵️ Thoughtful Reviewer: Analyzes outcomes and gives feedback.")
        }
        self.logs = []
        self.scores = {}

    def evaluate_agent(self, name, log):
        # Simple score: 1 point for each "Result", minus for "Error"
        score = sum(1 for l in log if "Result" in l) - sum(1 for l in log if "Error" in l)
        self.scores[name] = self.scores.get(name, 0) + score
        self.logs.append(f"🧮 Score for {name}: {score}")

    def run_mission(self, mission):
        self.logs.append("🚀 Starting mission: " + mission["name"])

        planner = self.agents["planner"]
        executor = self.agents["executor"]
        reviewer = self.agents["reviewer"]

        self.logs.append(planner.persona)
        planner.realize_plan([{"action": "ai_strategy", "payload": {"topic": mission["topic"]}}])
        self.logs += planner.status_log
        self.evaluate_agent("planner", planner.status_log)

        self.logs.append(executor.persona)
        executor.realize_plan(mission["steps"])
        self.logs += executor.status_log
        self.evaluate_agent("executor", executor.status_log)

        self.logs.append(reviewer.persona)
        reviewer.realize_plan([{"action": "notify", "payload": {"message": f"Review complete for {mission['name']}"}}])
        self.logs += reviewer.status_log
        self.evaluate_agent("reviewer", reviewer.status_log)

        # Competition: Who scored highest this round?
        top_agent = max(self.scores.items(), key=lambda x: x[1])[0]
        self.logs.append(f"🏆 Best performing agent: {top_agent.upper()} with {self.scores[top_agent]} points!")

        with open("data/agent_scores.json", "w") as f:
            json.dump(self.scores, f, indent=2)

        return self.logs