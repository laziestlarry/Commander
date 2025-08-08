import json

topics = [f"Product {i}" for i in range(1, 101)]
missions = []

for i, topic in enumerate(topics):
    mission = {
        "name": f"Mission_{i+1}",
        "topic": topic,
        "steps": [
            {"action": "notify", "payload": {"message": f"Launching {topic}"}},
            {"action": "store_data", "payload": {"key": f"{topic.lower()}", "value": "test"}}
        ]
    }
    missions.append(mission)

with open("data/mission_playbooks.json", "w") as f:
    json.dump(missions, f, indent=2)

print("✅ 100 missions generated.")