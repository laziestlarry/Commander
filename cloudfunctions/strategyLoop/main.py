from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "result": "Strategy loop active",
        "status": "success"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)