#!/bin/bash

echo "🚀 Starting Full Commander Deployment..."

# Firebase Deployment
cd firebase
firebase deploy --project=propulse-autonomax
cd ..

# Build and Deploy Cloud Run API
echo "🛠️ Deploying FastAPI public API to Cloud Run..."
gcloud builds submit --tag gcr.io/propulse-autonomax/commander-api
gcloud run deploy commander-api \
  --image gcr.io/propulse-autonomax/commander-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --project=propulse-autonomax

# Scheduler Job Setup
echo "⏰ Setting up weekly GCP Scheduler job..."
bash deploy/gcp_scheduler_setup.sh

echo "✅ Deployment Complete!"