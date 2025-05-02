This is what I have thought

````markdown
# 🧠 Human-in-the-Loop AI Supervisor

A voice-based AI receptionist using **LiveKit**, **Google Gemini**, and **Deepgram**, with escalation support and knowledge base learning via **Firebase**. It simulates real-time customer support where the AI agent handles calls and escalates unresolved queries to a human supervisor, who teaches the system for future automation.

---

## 📦 Features

- 🤖 Real-time AI voice assistant using LiveKit + Deepgram
- 📞 Automatic escalation to a human supervisor when the AI is unsure
- 🗄️ Supervisor responses stored in Firebase as a dynamic knowledge base
- 🔁 Continuous learning loop from supervisor input

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/human-loop-voice-agent.git
cd human-loop-voice-agent
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Firebase

* Download your Firebase service account key (JSON).
* Update the path in `firebase_config.py`:

```python
cred = credentials.Certificate("path/to/your-firebase-key.json")
```

### 5. Configure Environment Variables

* Create a `.env` file in the project root with any required keys (e.g., LiveKit, OpenAI, Deepgram).
* Example:

  ```
  OPENAI_API_KEY=your_key
  LIVEKIT_API_KEY=your_key
  LIVEKIT_SECRET=your_secret
  ```

---

## 🚀 Running the Application

### 1. Start the Flask Backend (API Server)

```bash
python app.py
```

Handles:

* `POST /new_request` - Store new escalation
* `GET /get_requests` - Fetch pending supervisor escalations
* `POST /resolve_request` - Supervisor resolves and updates KB

### 2. Start the Voice Agent (AI Worker)

```bash
python voice_agent.py
```

* Handles real-time speech via LiveKit
* Uses Gemini for LLM responses
* Escalates when unsure

---

## 🧩 Project Structure

```
├── app.py                 # Flask API backend
├── voice_agent.py         # AI voice assistant using LiveKit
├── help_requests.py       # Firestore logic for help requests
├── supervisor.py          # Supervisor resolution + KB learning
├── knowledge_base.py      # Dynamic knowledge storage
├── firebase_config.py     # Firebase client initialization
├── .env                   # Environment variables (excluded from Git)
├── .gitignore             # Files to ignore (e.g., credentials)
```

---

## 🔄 System Flow

1. User calls and speaks to the **AI Agent**.
2. If the AI is unsure, it creates a **help request** via `/new_request`.
3. Supervisor UI (external) fetches unresolved queries via `/get_requests`.
4. Supervisor submits a resolution via `/resolve_request`.
5. Response is stored in the **Knowledge Base** for future automation.

---

## ✅ API Overview

### `POST /new_request`

Create a help request.

```json
{
  "query": "What's the refund policy?"
}
```

---

### `GET /get_requests`

Get all unresolved help requests.

---

### `POST /resolve_request`

Mark a request as resolved and store the answer.

```json
{
  "request_id": "abc123",
  "response": "Our refund policy allows returns within 30 days."
}
```

---

## 🧪 Testing

You can test the backend using:

* `curl` commands
* Postman
* Your frontend (in progress)
* Logs will display agent activity and Firebase updates

---

## 🧐 Code Review Summary

### `voice_agent.py`

* Uses LiveKit's `AgentSession`, Deepgram STT, Gemini LLM, and TTS.
* Hardcoded escalation logic (can be improved via dynamic KB checks).

### `app.py`

* Clean RESTful Flask API routing.
* Delegates logic to dedicated modules.

### `help_requests.py`

* Well-structured Firestore document creation with timestamps.

### `supervisor.py` & `knowledge_base.py`

* Updates Firebase with supervisor answers.
* Builds a long-term knowledge base.

### `firebase_config.py`

* Loads credentials and initializes Firestore.

---

## 📘 Future Improvements

* 🔍 Smart knowledge base check before escalation
* 💻 Frontend UI for supervisors to manage requests
* 🔐 Auth system for API endpoints
* ☎️ Telephony API integration for real phone support
* 🧠 Semantic search in knowledge base (e.g., using vector DB)

---