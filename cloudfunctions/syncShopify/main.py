from flask import Flask, request, jsonify
from sync_shopify_logic import run_shopify_sync

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def handle_request():
    result = run_shopify_sync()
    return jsonify({"status": "success", "result": result})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)