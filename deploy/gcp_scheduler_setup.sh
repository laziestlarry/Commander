gcloud scheduler jobs create http weekly-strategy-loop \
  --schedule="0 6 * * 1" \
  --uri="https://YOUR_CLOUD_RUN_URL/launch_loop" \
  --http-method=GET \
  --time-zone="Europe/Istanbul" \
  --project=propulse-autonomax