from datetime import datetime
import logging
from flask import Flask, request, jsonify
from help_requests import create_help_request, get_pending_requests
from supervisor import process_supervisor_response

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("🚀 Flask server started."
              " Listening for help requests...")

@app.route("/")
def index():
    return "Welcome to the Help Request API!"


@app.route("/new_request", methods=["POST"])
def create_request():
    data = request.json
    if not data or "query" not in data:
        return jsonify({"error": "Invalid payload"}), 400
    
    print("📡 Received Help Request:", data)  # ✅ Debugging Log
    
    request_id = create_help_request(data["query"])  # ✅ Save to Firestore
    if request_id:
        return jsonify({"status": "success", "message": "Help request stored.", "request_id": request_id}), 200
    else:
        return jsonify({"error": "Failed to store request"}), 500

@app.route("/get_requests", methods=["GET"])
def get_requests():
    """Fetch pending help requests for supervisor."""
    pending_requests = get_pending_requests()
    return jsonify(pending_requests)

@app.route("/resolve_request", methods=["POST"])
def resolve_request():
    """Handles supervisor response & updates Firebase."""
    data = request.json
    process_supervisor_response(data["request_id"], data["response"])
    return jsonify({"message": "Resolved and updated knowledge base"})

if __name__ == "__main__":
    app.run(debug=True)
