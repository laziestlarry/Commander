#!/bin/bash

echo "🔐 Loading environment variables from .env"
export $(grep -v '^#' .env | xargs)

echo "🧱 Building Python app..."
pip install -r requirements.txt

echo "🚀 Deploying Flask app to Google Cloud Run..."
gcloud run deploy autonomax-commander \
  --source . \
  --entry-point app.dashboard_flask:app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --project=$GCP_PROJECT_ID

echo "🌐 Deploying dashboard frontend to Firebase Hosting..."
firebase deploy --only hosting --project $FIREBASE_PROJECT_ID

echo "✅ Deployment complete. Visit:"
echo " - GCP Cloud Run: https://console.cloud.google.com/run"
echo " - Firebase Hosting: https://$FIREBASE_PROJECT_ID.web.app"
