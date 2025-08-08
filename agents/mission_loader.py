
from agents.shopify_sync import ShopifySyncAgent
from agents.fiverr_sync import FiverrAgent
from agents.youtube_bot import YouTubeAgent

def load_missions():
    return [
        {
            "name": "Shopify Sync",
            "description": "Sync products and pricing to Shopify",
            "agent": ShopifySyncAgent()
        },
        {
            "name": "Fiverr Bot",
            "description": "Launch Fiverr portfolio sync bot",
            "agent": FiverrAgent()
        },
        {
            "name": "YouTube Upload Bot",
            "description": "Auto-upload Shorts and track views",
            "agent": YouTubeAgent()
        }
    ]
