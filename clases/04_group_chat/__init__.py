"""Clase 04: conversación por turnos entre dos agentes."""

import os
from pathlib import Path

from agent_framework import Agent
from agent_framework.openai import OpenAIChatCompletionClient
from agent_framework.orchestrations import GroupChatBuilder, GroupChatState
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

investigador = Agent(client=client, name="investigador", instructions=(
    "Analiza la petición y aporta ideas, supuestos y datos que faltan. "
    "En tu segundo turno, mejora las ideas según la crítica. Responde en español; no simules búsqueda web."
))
redactor = Agent(client=client, name="redactor", instructions=(
    "En tu primer turno, redacta una propuesta basada en el investigador. "
    "En tu segundo turno, entrega una versión final mejorada. Responde en español."
))


def seleccionar(state: GroupChatState) -> str:
    """Alterna los participantes durante cuatro turnos."""
    return ("investigador", "redactor")[state.current_round % 2]


workflow = GroupChatBuilder(
    name="group_chat",
    participants=[investigador, redactor],
    selection_func=seleccionar,
    max_rounds=4,
).build()
