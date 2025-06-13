import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "✅ Optimus is alive and running on Cloud Run!"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == "__main__":
    # Cloud Run expects the service to listen on the port defined by the PORT env variable
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
