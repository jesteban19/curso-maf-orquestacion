"""Clase 05: traspaso de una consulta al especialista adecuado."""

import os
from pathlib import Path

from agent_framework import Agent
from agent_framework.openai import OpenAIChatCompletionClient
from agent_framework.orchestrations import HandoffBuilder
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

recepcion = Agent(client=client, name="recepcion", description="Clasifica consultas de soporte.", require_per_service_call_history_persistence=True, instructions=(
    "Recibes consultas de soporte. Usa la herramienta de handoff para pasar problemas de acceso "
    "a acceso y problemas de facturación a facturacion. Si no puedes clasificar, pide una aclaración. "
    "Responde en español."
))
acceso = Agent(client=client, name="acceso", description="Ayuda con inicio de sesión y cuentas.", require_per_service_call_history_persistence=True, instructions=(
    "Ayuda con acceso a cuentas. Sugiere pasos seguros y pide el dato mínimo que falte. "
    "Nunca solicites contraseñas ni afirmes haber cambiado una cuenta. Responde en español."
))
facturacion = Agent(client=client, name="facturacion", description="Ayuda con cobros y facturas.", require_per_service_call_history_persistence=True, instructions=(
    "Ayuda con dudas de cobros y facturas. Explica qué comprobar y qué datos faltan. "
    "No afirmes haber consultado ni modificado pagos. Responde en español."
))

workflow = (
    HandoffBuilder(name="handoff", participants=[recepcion, acceso, facturacion])
    .with_start_agent(recepcion)
    .add_handoff(recepcion, [acceso, facturacion])
    .add_handoff(acceso, [recepcion])
    .add_handoff(facturacion, [recepcion])
    .build()
)
