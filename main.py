from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agents import ConversationAgent
from app.logging_config import setup_logging


def create_app():
    setup_logging()
    app = FastAPI(title="Pocket Med Guard")

    # -------------------------
    # CORS FIX (IMPORTANT)
    # -------------------------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],       # frontend allowed
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Agent
    agent = ConversationAgent()

    @app.post("/message")
    async def handle_message(payload: dict):
        user_id = payload.get("user_id", "anon")
        message = payload.get("message", "")
        response = await agent.handle_message(user_id, message)
        return response

    return app


app = create_app()
