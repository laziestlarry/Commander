#!/bin/bash

echo "🔧 Starting AutonomaX Commander Fixed Init Script..."

# Step 1: Navigate to project root
cd "$(dirname "$0")"

# Step 2: Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Load environment variables
if [ -f .env ]; then
    echo "✅ .env file found."
else
    echo "⚠️ No .env file found. Please create one before proceeding."
    exit 1
fi

# Step 5: Deploy syncShopify Function
gcloud functions deploy syncShopify \
  --gen2 \
  --entry-point syncShopify \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated \
  --region=us-central1 \
  --source=cloudfunctions/syncShopify \
  --project=propulse-autonomax

# Step 6: Deploy strategyLoop Function
gcloud functions deploy strategyLoop \
  --gen2 \
  --entry-point strategyLoop \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated \
  --region=us-central1 \
  --source=cloudfunctions/strategyLoop \
  --project=propulse-autonomax

# Step 7: Create Scheduler Jobs with --location
gcloud scheduler jobs create http syncShopifyDaily \
  --schedule="0 9 * * *" \
  --uri="https://us-central1-propulse-autonomax.cloudfunctions.net/syncShopify" \
  --http-method=GET \
  --time-zone="Europe/Istanbul" \
  --location=us-central1 \
  --project=propulse-autonomax

gcloud scheduler jobs create http weeklyStrategyLoop \
  --schedule="0 10 * * MON" \
  --uri="https://us-central1-propulse-autonomax.cloudfunctions.net/strategyLoop" \
  --http-method=GET \
  --time-zone="Europe/Istanbul" \
  --location=us-central1 \
  --project=propulse-autonomax

# Run the agent mission loop on Commander start
nohup python3 agents/core/agent_runtime_loop.py &

# Step 8: Launch Control Center UI (optional)
echo "🚀 To launch Control Center UI, run: streamlit run dashboard/control_center.py"

# Step 9: Trigger Revenue Modules 🔁

echo "🚀 Running Shopify Sync..."
nohup python3 fiverr_sync.py &

echo "🚀 Running Fiverr Sync..."
nohup python3 shopify_sync.py &

echo "📺 Running YouTube Automation Bot..."
nohup python3 launch_youtube_bot.py &

# (Optional) Telegram Reporter or Email Trigger can go here if configured
# echo "📨 Notifying Telegram..."
# nohup python3 agents/utils/notify_telegram.py &

# (Optional) Activate Secret Agent if needed at each boot
# echo "🕵️ Running Secret Collector Agent..."
# nohup python3 agents/secret_agent/secret_agent_online_collector.py &

echo "✅ All Revenue Agents Activated."

Launch dashboard automatically (comment out if using tmux)
# streamlit run dashboard/control_center.py
echo "✅ AutonomaX Commander setup complete. You’re ready to launch missions!"