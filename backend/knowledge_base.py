import firebase_admin
from firebase_admin import firestore

# Initialize Firebase Admin
if not firebase_admin._apps:
    firebase_admin.initialize_app()
db = firestore.client()

def update_knowledge_base(request_id, response_text):
    """Stores learned answers in Firebase."""
    request_ref = db.collection("help_requests").document(request_id).get()
    if request_ref.exists:
        query_text = request_ref.to_dict()["customer_query"]
        db.collection("knowledge_base").document(query_text).set({
            "answer": response_text
        })
