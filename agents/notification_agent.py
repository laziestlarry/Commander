import requests, os
class NotificationAgent:
    def send_slack(self, message):
        webhook_url = os.getenv("SLACK_WEBHOOK")
        if webhook_url:
            requests.post(webhook_url, json={"text": message})
    def send_telegram(self, message):
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if token and chat_id:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            requests.post(url, data={"chat_id": chat_id, "text": message})
