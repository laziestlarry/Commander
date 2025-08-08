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

# Step 8: Launch Control Center UI (optional)
echo "🚀 To launch Control Center UI, run: streamlit run dashboard/control_center.py"

echo "✅ AutonomaX Commander setup complete. You’re ready to launch missions!"