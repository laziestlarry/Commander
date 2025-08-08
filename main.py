from agents.cua_agent import CUAAgent
from db.models import engine as db_engine  # Define your engine in db/models.py

if __name__ == "__main__":
    cua = CUAAgent(db_engine)
    plan = [
        {"action": "ai_strategy", "payload": {"topic": "Eco Planner for Gen-Z"}},
        {"action": "add_product_db", "payload": {"title": "Eco Planner", "price": 12.99, "platform": "shopify"}},
        {"action": "sync_shopify", "payload": {"title": "Eco Planner", "body_html": "Go green!", "price": 12.99}},
        {"action": "track_kpi", "payload": {"metric": "product_uploaded", "value": 1}},
        {"action": "wait", "seconds": 1},
        {"action": "review_feedback", "payload": {"platform": "shopify"}},
        {"action": "ad_campaign", "payload": {"platform": "facebook", "adset": "eco_launch"}},
        {"action": "notify", "payload": {"message": "Launch completed for Eco Planner!"}},
    ]
    cua.realize_plan(plan)
    print("Execution Log:", cua.status_log)
