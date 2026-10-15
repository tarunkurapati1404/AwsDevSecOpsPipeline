from flask import Flask, jsonify
import datetime
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the DevSecOps Demo API!"})

@app.route("/health")
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "system": platform.system()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec B104