"""Clase 06: gestor que planifica y coordina especialistas dinámicamente."""

import os
from pathlib import Path

from agent_framework import Agent
from agent_framework.openai import OpenAIChatCompletionClient
from agent_framework.orchestrations import (
    MagenticBuilder,
    MagenticContext,
    MagenticOrchestratorEvent,
    MagenticProgressLedger,
    MagenticProgressLedgerItem,
    StandardMagenticManager,
)
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv(Path(__file__).resolve().parents[2] / ".env")


def _evento_magentic_to_dict(event: MagenticOrchestratorEvent) -> dict:
    """Compatibilidad con DevUI b260910: serializa el Message del plan."""
    return {"event_type": event.event_type.value, "content": event.content.to_dict()}


# DevUI espera to_dict() en los eventos informativos. Esta versión de
# orchestrations entrega una dataclass con un Message sin convertir a JSON.
# Se añade solo el adaptador faltante, sin modificar los paquetes instalados.
if not hasattr(MagenticOrchestratorEvent, "to_dict"):
    MagenticOrchestratorEvent.to_dict = _evento_magentic_to_dict

sdk = AsyncOpenAI(
    api_key=os.environ["TOKEN"],
    base_url=os.getenv("ENDPOINT", "https://coursesyoutube-resource.services.ai.azure.com/openai/v1").rstrip("/") + "/",
    timeout=60.0,
    max_retries=1,
)
client = OpenAIChatCompletionClient(async_client=sdk, model=os.getenv("MODEL", "gpt-5.4-mini"))

gestor = Agent(client=client, name="gestor", description="Planifica y coordina el trabajo.", instructions=(
    "Coordina a los especialistas para resolver la tarea. Revisa el progreso, adapta el plan "
    "y entrega una respuesta final en español. No inventes verificaciones externas. "
    "Ajusta el esfuerzo a la petición: para un título, nombre o frase, encarga directamente "
    "al redactor una propuesta y termina cuando exista una opción útil. No exijas análisis, "
    "validaciones ni consenso si el usuario no los pidió. Si faltan detalles opcionales, "
    "usa supuestos razonables; no bloquees la entrega."
))
analista = Agent(client=client, name="analista", description="Identifica requisitos, supuestos y riesgos.", instructions=(
    "Analiza solo lo necesario para resolver la petición, de forma breve. "
    "Los datos opcionales faltantes no impiden proponer una respuesta: usa supuestos razonables. "
    "Responde en español. No afirmes haber investigado en fuentes externas."
))
redactor = Agent(client=client, name="redactor", description="Desarrolla una propuesta concreta.", instructions=(
    "Entrega directamente el resultado solicitado por el usuario. Si pide un título, "
    "propón un título concreto aunque no indique la temática del canal. No te limites "
    "a explicar cómo crearlo ni pidas detalles opcionales. Incluye pasos y criterios "
    "de éxito solo cuando la tarea lo requiera. Responde en español."
))


class GestorAcotado(StandardMagenticManager):
    """Sintetiza tras dos intervenciones, antes del aviso de límite del framework."""

    async def create_progress_ledger(self, magentic_context: MagenticContext) -> MagenticProgressLedger:
        # La primera evaluación ocurre antes de que hable cualquier especialista.
        if magentic_context.round_count >= 3:
            return MagenticProgressLedger(
                is_request_satisfied=MagenticProgressLedgerItem(
                    reason="Se agotó el presupuesto de especialistas; entregar la mejor respuesta disponible.",
                    answer=True,
                ),
                is_in_loop=MagenticProgressLedgerItem(reason="Cierre por presupuesto.", answer=False),
                is_progress_being_made=MagenticProgressLedgerItem(reason="Pasar a la síntesis final.", answer=True),
                next_speaker=MagenticProgressLedgerItem(reason="No habrá otra intervención.", answer="redactor"),
                instruction_or_question=MagenticProgressLedgerItem(reason="Finalizar.", answer=""),
            )
        return await super().create_progress_ledger(magentic_context)


manager = GestorAcotado(
    agent=gestor,
    final_answer_prompt=(
        "Petición original: {task}\n"
        "Entrega ahora la mejor respuesta disponible en español usando la conversación. "
        "Para un título, entrega un título concreto y breve. No describas la coordinación interna. "
        "Si la tarea compleja quedó incompleta, indica brevemente qué falta; no afirmes "
        "haberla completado ni inventes verificaciones."
    ),
    max_round_count=4,
    max_stall_count=2,
    max_reset_count=1,
)

workflow = MagenticBuilder(
    name="magentic",
    participants=[analista, redactor],
    manager=manager,
).build()
