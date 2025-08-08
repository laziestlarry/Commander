import time
import requests
import logging

logging.basicConfig(level=logging.INFO)

def ping_service(name, url):
    logging.info(f"⏳ Calling {name} service...")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"✅ {name} Success: {response.json()}")
        else:
            logging.error(f"❌ {name} Failed with status {response.status_code}: {response.text}")
    except Exception as e:
        logging.error(f"❌ Error calling {name}: {str(e)}")

if __name__ == "__main__":
    while True:
        logging.info("🚀 Executing Commander AI Bind Loop...")

        ping_service("Shopify Sync", "https://syncshopify-service-71658389068.us-central1.run.app")
        ping_service("Strategy Loop", "https://strategyloop-service-71658389068.us-central1.run.app")

        logging.info("💤 Sleeping 60 seconds before next bind loop...\n")
        time.sleep(60)