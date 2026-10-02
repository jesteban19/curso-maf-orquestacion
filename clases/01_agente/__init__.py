"""Clase 01: un agente como punto de partida para la serie."""

import os
from pathlib import Path

from agent_framework import Agent
from agent_framework.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

sdk = AsyncOpenAI(
    api_key=os.environ["TOKEN"],
    base_url=os.getenv("ENDPOINT", "https://coursesyoutube-resource.services.ai.azure.com/openai/v1").rstrip("/") + "/",
    timeout=60.0,
    max_retries=1,
)
client = OpenAIChatCompletionClient(async_client=sdk, model=os.getenv("MODEL", "gpt-5.4-mini"))

agent = Agent(
    client=client,
    name="asistente_basico",
    description="Un solo agente responde la petición del usuario.",
    instructions=(
        "Responde en español, de forma clara y breve. Si te falta información, dilo. "
        "No afirmes haber consultado archivos, sitios web o herramientas."
    ),
)
