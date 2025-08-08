#!/bin/bash

# Replace with your repo (preset)
REPO="laziestlarry/Commander"

# Secrets to add
declare -a secrets=("GCP_PROJECT_ID" "GCP_SA_KEY" "SHOPIFY_API_KEY" "SHOPIFY_API_SECRET" "TELEGRAM_BOT_TOKEN" "TELEGRAM_CHAT_ID")

echo "🔐 Adding secrets to $REPO..."

for secret in "${secrets[@]}"; do
  echo -n "Enter value for $secret: "
  read -s value
  echo
  echo "Adding $secret..."
  echo "$value" | gh secret set "$secret" -R "$REPO"
done

echo "✅ All secrets added successfully!"
