from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow calls from the Power Apps connector service

# simple health check so you can test the base URL
@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

alerts = [
    {"id": "A001", "type": "Phishing", "severity": "High", "timestamp": "2025-10-16T14:00:00Z"},
    {"id": "A002", "type": "Malware", "
