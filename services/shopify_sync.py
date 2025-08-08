from services.shopify_hook import fetch_shopify_revenue
import csv
from datetime import datetime

revenue = fetch_shopify_revenue()
with open("data/revenue_log.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow([datetime.now().isoformat(), "success", revenue])
print(f"✅ Synced Shopify revenue: ${revenue}")