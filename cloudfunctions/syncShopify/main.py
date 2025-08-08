import functions_framework
from services.shopify_hook import fetch_shopify_revenue
from services.telegram_notifier import send_telegram_report
from datetime import datetime
import csv
import os

@functions_framework.http
def syncShopify(request):
    try:
        revenue = fetch_shopify_revenue()
        log_path = os.path.join("data", "revenue_log.csv")
        with open(log_path, "a") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().isoformat(), "success", revenue])
        send_telegram_report(f"✅ Shopify revenue synced: ${revenue:.2f}")
        return f"Revenue sync success: ${revenue:.2f}", 200
    except Exception as e:
        send_telegram_report(f"❌ Revenue sync failed: {str(e)}")
        return f"Error: {str(e)}", 500