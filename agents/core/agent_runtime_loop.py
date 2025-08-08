# Commander_Orchestrated_Online - Final Main Runtime Script
# agent_runtime_loop.py

import time
import logging
from agents.mission_loader import load_missions

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("agents.mission_loader")


def execute_missions():
    logger.info("\U0001F680 Executing scheduled agent missions...")
    missions = load_missions()

    for mission in missions:
        try:
            logger.info(f"\u2705 Running: {mission['name']} - {mission['description']}")
            mission['function']()
            logger.info(f"\u2714\ufe0f Completed: {mission['name']}")
        except Exception as e:
            logger.error(f"\u274C Mission failed: {e}")


if __name__ == "__main__":
    while True:
        execute_missions()
        logger.info("\U0001F4A4 Sleeping 30 seconds before next loop...")
        time.sleep(30)