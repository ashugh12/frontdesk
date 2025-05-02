import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials
cred = credentials.Certificate("/Users/ashutosh/frontDesk/backend/frontdesk-3d251-firebase-adminsdk-fbsvc-b31f713d98.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# 🔥 Test writing to Firestore
doc_ref = db.collection("help_requests").document()

print(f"✅ Firestore Successfully Stored: {doc_ref.id}")
