import time
from agents.commander import Commander
from agents.logic.decision_tree import DecisionTreeAI
from agents.logic.self_optimizer import SelfOptimizer

def continuous_loop():
    while True:
        print("🚀 Looping: Commander mission execution starting...")
        commander = Commander()
        commander.assign_weekly_objectives()

        result = commander.run_eval()
        decision = DecisionTreeAI().evaluate(result)

        print(f"🧠 Strategy decision: {decision}")
        if decision == "retrain_with_examples":
            commander.retrain_agents("examples")
        elif decision == "launch_sales_sequence":
            commander.deploy_sales_automation()

        SelfOptimizer(commander).optimize()

        print("✅ Sleeping for 24 hours before next cycle...")
        time.sleep(86400)  # Run every 24h