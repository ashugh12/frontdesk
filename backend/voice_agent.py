import requests
import logging
import asyncio
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RoomInputOptions
from livekit.plugins import google, noise_cancellation, deepgram

# ✅ Load environment variables
load_dotenv()

# ✅ Setup Logging for Continuous Tracking
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class Assistant(Agent):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            instructions="You are a virtual receptionist. Answer common inquiries like booking, pricing, and services. "
                         "If unsure, say 'I will go to my supervisor and let you connect.' and escalate the request.",
            **kwargs,
        )

async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
        stt=deepgram.STT(model="nova-2-general"),
        llm=google.beta.realtime.RealtimeModel(
            model="gemini-2.0-flash-exp",
            voice="Puck",
            temperature=0.8,
            instructions="If you cannot answer the question, say 'I will go to my supervisor and let you connect.'",
        ),
        tts=google.TTS(
            gender="female",
            voice_name="en-US-Standard-H",
        ),
    )

    await session.start(room=ctx.room, agent=Assistant(), room_input_options=RoomInputOptions(noise_cancellation=noise_cancellation.BVC()))

        # ✅ Hardcoded Help Request Every Time
    send_help_request(" Doing outside Hardcoded: Supervisor assistance needed.")

    try:
        user_query = await session.generate_reply(instructions="Listen and transcribe user inquiry.")

        if hasattr(user_query, "_chat_message"):
            chat_message = user_query._chat_message
            if hasattr(chat_message, "content"):
                message_content = chat_message.content
                logging.info(f"📜 New Agent Instruction: {message_content}")

                # ✅ Hardcoded Help Request Every Time
                send_help_request("Hardcoded: Supervisor assistance needed.")

        await asyncio.sleep(1)  # ✅ Prevent excessive CPU usage

    except Exception as e:
        logging.error(f"🚨 Error handling speech input: {str(e)}")
        
def send_help_request(user_message):
    payload = {"query": user_message}

    try:
        response = requests.post("http://127.0.0.1:5000/new_request", json=payload)  # ✅ Corrected Flask URL
        response.raise_for_status()

        logging.info(f"📡 Help Request Sent: {payload}")
        logging.info(f"🌐 Flask Response: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as api_error:
        logging.error(f"🚨 API Error: {api_error}")


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))

logging.info("🚀 Assistant is running indefinitely...")