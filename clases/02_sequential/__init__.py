"""Clase 02: planificador -> ejecutor -> revisor, basado en main.py."""

import os
from pathlib import Path

from agent_framework import Agent
from agent_framework.openai import OpenAIChatCompletionClient
from agent_framework.orchestrations import SequentialBuilder
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

roles = [
    Agent(client=client, name="planificador", instructions=(
        "Analiza la petición original y propone un plan breve con pasos y criterios de éxito. "
        "Declara supuestos y datos faltantes. No inventes información."
    )),
    Agent(client=client, name="ejecutor", instructions=(
        "Desarrolla la respuesta siguiendo el plan anterior. Solo puedes razonar y redactar: "
        "no tienes herramientas ni acceso a archivos, web o sistemas externos. "
        "No afirmes haber ejecutado acciones ni comprobaciones externas."
    )),
    Agent(client=client, name="revisor", instructions=(
        "Contrasta el trabajo anterior con la petición original, corrige errores y entrega "
        "la respuesta final completa en español. Señala limitaciones y datos pendientes."
    )),
]

workflow = SequentialBuilder(name="sequential", participants=roles).build()
