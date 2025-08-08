#!/bin/bash
echo "🚀 Starting full deploy..."
python3 fiverr_sync.py
python3 shopify_sync.py
python3 launch_youtube_bot.py
echo "✅ Deploy sequence complete."
