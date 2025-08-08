import time
import requests
import logging

# URLs for deployed Cloud Run services
SYNC_SHOPIFY_URL = "https://syncshopify-service-71658389068.us-central1.run.app"
STRATEGY_LOOP_URL = "https://strategyloop-service-71658389068.us-central1.run.app"

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def ping_service(name, url):
    try:
        logging.info(f"→ Pinging {name} at {url}")
        response = requests.get(url)
        logging.info(f"✅ {name} responded: {response.status_code} - {response.text[:100]}")
    except Exception as e:
        logging.error(f"❌ Error pinging {name}: {str(e)}")

def run_loop(interval=60):
    logging.info("🔁 Agent Commander Runtime started. Looping every %s seconds.", interval)
    while True:
        ping_service("SyncShopify", SYNC_SHOPIFY_URL)
        ping_service("StrategyLoop", STRATEGY_LOOP_URL)
        logging.info("🕒 Waiting for next loop...\n")
        time.sleep(interval)

if __name__ == "__main__":
    run_loop()