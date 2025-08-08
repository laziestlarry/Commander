from agents.agent_manager import AgentManager
import json

if __name__ == "__main__":
    manager = AgentManager()

    with open("data/mission_playbooks.json") as f:
        missions = json.load(f)

    for mission in missions:
        print(f"\n🎯 Running Multi-Agent Mission: {mission['name']}")
        logs = manager.run_mission(mission)
        for log in logs:
            print("🪵", log)