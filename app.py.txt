from flask import Flask, jsonify
import os

app = Flask(__name__)

alerts = [
    {"id": "A001", "type": "Phishing", "severity": "High", "timestamp": "2025-10-16T14:00:00Z"},
    {"id": "A002", "type": "Malware", "severity": "Medium", "timestamp": "2025-10-16T13:45:00Z"}
]

logs = [
    {"id": "L001", "source": "Firewall", "message": "Blocked IP 192.168.1.10", "timestamp": "2025-10-16T13:30:00Z"},
    {"id": "L002", "source": "Antivirus", "message": "Scan completed", "timestamp": "2025-10-16T13:00:00Z"}
]

scan_results = [
    {"id": "S001", "host": "server01", "vulnerability": "CVE-2023-1234", "severity": "Critical"},
    {"id": "S002", "host": "server02", "vulnerability": "CVE-2023-5678", "severity": "Low"}
]

@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alerts)

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs)

@app.route('/scan-results', methods=['GET'])
def get_scan_results():
    return jsonify(scan_results)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
