import json
import random
from agents.cua_agent import CUAAgent
from db.models import engine as db_engine

class AgentTrainer:
    def __init__(self):
        self.agent = CUAAgent(db_engine)

    def load_static_plans(self, filepath='data/mission_playbooks.json'):
        with open(filepath, 'r') as f:
            return json.load(f)

    def simulate_plan_execution(self, plan):
        print(f"🧠 Simulating: {plan.get('name', 'Unnamed Plan')}")
        self.agent.realize_plan(plan['steps'])
        for log in self.agent.status_log:
            print("🪵", log)
        success = any("Result" in l for l in self.agent.status_log)
        return success

    def train_from_playbooks(self):
        plans = self.load_static_plans()
        results = []
        for plan in plans:
            print("\n📦 Training with mission:", plan.get("name"))
            result = self.simulate_plan_execution(plan)
            results.append({"plan": plan["name"], "success": result})
        return results

    def feedback_loop(self, results):
        total = len(results)
        success = sum(r['success'] for r in results)
        print(f"📊 TRAINING RESULTS: {success}/{total} successful ({(success/total)*100:.1f}%)")

if __name__ == "__main__":
    trainer = AgentTrainer()
    results = trainer.train_from_playbooks()
    trainer.feedback_loop(results)