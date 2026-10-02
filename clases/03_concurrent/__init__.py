"""Clase 03: perspectivas independientes sobre una misma petición."""

import os
from pathlib import Path

from agent_framework import Agent
from agent_framework.openai import OpenAIChatCompletionClient
from agent_framework.orchestrations import ConcurrentBuilder
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

participants = [
    Agent(client=client, name="beneficios", instructions="Analiza solo beneficios y oportunidades. Responde en español y no inventes datos."),
    Agent(client=client, name="riesgos", instructions="Analiza solo riesgos y limitaciones. Responde en español y no inventes datos."),
    Agent(client=client, name="implementacion", instructions="Propón pasos prácticos de implementación. Responde en español y declara supuestos."),
]

workflow = ConcurrentBuilder(name="concurrent", participants=participants).build()
