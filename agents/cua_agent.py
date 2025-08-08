from agents.platform.shopify_bot import ShopifyBot
    def __init__(self, db_engine=None, persona="Generic Agent"):
        self.db_engine = db_engine
        self.persona = persona
        self.status_log = []
from agents.platform.etsy_bot import EtsyBot
from agents.platform.amazon_bot import AmazonBot
from agents.platform.ads_agent import AdsAgent
from agents.kpi_agent import KPIAgent
from agents.content_agent import ContentAgent
from agents.review_agent import ReviewAgent
from agents.notification_agent import NotificationAgent
from db.micro_agents import ProductDBAgent
import time

class CUAAgent:
        self.shopify = ShopifyBot()
        self.etsy = EtsyBot()
        self.amazon = AmazonBot()
        self.ads = AdsAgent()
        self.kpi = KPIAgent()
        self.content = ContentAgent()
        self.review = ReviewAgent()
        self.notify = NotificationAgent()
        self.db_agent = ProductDBAgent(db_engine)
        self.status_log = []

    def realize_plan(self, plan_steps):
        for idx, step in enumerate(plan_steps, 1):
            print(f"Step {idx}: {step['action']}")
            try:
                result = self.act_on_step(step)
                self.status_log.append({"step": step, "status": "completed", "result": result})
                print(f"✓ Completed: {step['action']}")
            except Exception as e:
                self.status_log.append({"step": step, "status": "failed", "error": str(e)})
                print(f"✗ Failed: {step['action']} | Error: {e}")

    def act_on_step(self, step):
        action = step["action"]
        if action == "sync_shopify":
            return self.shopify.create_product(step["payload"])
        elif action == "sync_etsy":
            return self.etsy.create_listing(step["payload"])
        elif action == "sync_amazon":
            return self.amazon.create_listing(step["payload"])
        elif action == "ai_strategy":
            return self.content.generate_description(step["payload"]["topic"])
        elif action == "track_kpi":
            m = step["payload"]
            return self.kpi.track(m["metric"], m["value"])
        elif action == "review_feedback":
            return self.review.collect(step["payload"]["platform"])
        elif action == "ad_campaign":
            return self.ads.launch(step["payload"])
        elif action == "notify":
            msg = step["payload"]["message"]
            return self.notify.send_slack(msg)
        elif action == "add_product_db":
            p = step["payload"]
            return self.db_agent.add_product(p["title"], p["price"], p["platform"])
        elif action == "wait":
            time.sleep(step.get("seconds", 1))
            return "Waited"
        else:
            raise ValueError(f"Unknown action: {action}")
