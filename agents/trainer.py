import csv
from datetime import datetime

def train_agents_with_playbook(missions):
    results = []
    for m in missions:
        score = len(str(m)) % 10 + 1  # Dummy scoring logic
        results.append((datetime.now().isoformat(), m['objective'], score))

    with open("data/strategy_feedback.csv", "a") as f:
        writer = csv.writer(f)
        for r in results:
            writer.writerow([r[0], r[1], "AUTO", r[2]])
    return results