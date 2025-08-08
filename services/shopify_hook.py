import requests

def fetch_shopify_revenue():
    headers = {
        "X-Shopify-Access-Token": "YOUR_ACCESS_TOKEN"
    }
    resp = requests.get("https://autonomax.myshopify.com/admin/api/2024-07/orders.json", headers=headers)
    data = resp.json()
    revenue = sum(float(order["total_price"]) for order in data.get("orders", []))
    return revenue