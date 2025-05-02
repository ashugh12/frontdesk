from datetime import datetime
from firebase_config import db

def create_help_request(query):
    """Stores a help request in Firestore with status & timestamp."""
    try:
        doc_ref = db.collection("help_requests").document()

        payload = {
            "customer_query": query,
            "status": "pending",
            "created_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),  # ✅ Save timestamp
            "supervisor_response": None,
        }

        print(f"🛠️ Writing to Firestore: {payload}")  # ✅ Debugging log
        doc_ref.set(payload)

        print(f"✅ Firestore Successfully Stored: {query}")
        return doc_ref.id

    except Exception as e:
        print(f"🚨 Firestore Write Failed: {str(e)}")
        return None


def get_pending_requests():
    """Retrieves all pending help requests with complete information."""
    try:
        requests_ref = db.collection("help_requests").where("status", "==", "pending").stream()
        
        pending_requests = [{
            "id": req.id,
            "query": req.to_dict().get("customer_query", ""),
            "status": req.to_dict().get("status", ""),
            "created_at": req.to_dict().get("created_at", "Unknown Date"),
            "supervisor_response": req.to_dict().get("supervisor_response", None),
        } for req in requests_ref]

        print(f"✅ Retrieved {len(pending_requests)} pending requests.")  
        return pending_requests

    except Exception as e:
        print(f"🚨 Firestore Query Failed: {str(e)}")
        return []
