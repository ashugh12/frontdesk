from knowledge_base import update_knowledge_base
from firebase_admin import firestore

db = firestore.client()

def process_supervisor_response(request_id, response_text):
    """Handles supervisor response and updates Firebase."""
    request_ref = db.collection("help_requests").document(request_id)
    request_ref.update({
        "supervisor_response": response_text,
        "status": "resolved"
    })
    update_knowledge_base(request_id, response_text)
