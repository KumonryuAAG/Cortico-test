from flask import Flask, jsonify
import requests

app = Flask(__name__)

TEXTBOARD_URL = "http://textboard:5000"  # use Docker service name

@app.route("/health")
def health():
    try:
        r = requests.get(f"{TEXTBOARD_URL}/", timeout=2)
        if r.status_code == 200:
            return jsonify(status="ok", textboard="up")
        else:
            return jsonify(status="degraded", textboard="unhealthy"), 502
    except Exception as e:
        return jsonify(status="down", textboard="unreachable", error=str(e)), 503

@app.route("/metrics")
def metrics():
    # Placeholder metrics; you could extend later
    return jsonify(
        requests=123,
        errors=1,
        monitored_service="textboard"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
