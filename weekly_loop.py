import time
import os

print("🔁 Simulated Weekly Strategy Trainer Started")
while True:
    os.system("python generate_bulk_missions.py")
    os.system("python multi_trainer.py")
    print("✅ Weekly training round complete. Sleeping 7 days (simulated 10s)...")
    time.sleep(10)  # simulate 7 days with 10 seconds for testing