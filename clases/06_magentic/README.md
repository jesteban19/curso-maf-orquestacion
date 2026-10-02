# Clase 06 — Magentic

**Objetivo del video:** presentar un gestor que planifica, elige especialistas, evalúa avances y puede replantear el trabajo.

```text
Usuario → gestor ⇄ analista / redactor → respuesta final del gestor
```

Abre DevUI con `uv run devui ./clases --port 8080` y selecciona `magentic`. Prueba: **«Diseña un plan de seis semanas para lanzar una base de conocimiento interna; incluye etapas, riesgos y criterios de éxito»**.

En [`__init__.py`](__init__.py), `MagenticBuilder` recibe un gestor y dos especialistas. El orden de intervención no está fijado de antemano. El gestor puede finalizar en cuanto tenga una respuesta útil. `GestorAcotado` fuerza la síntesis tras un máximo de dos intervenciones de especialistas, antes de alcanzar el límite de rondas del framework (que solo emite un aviso de terminación). Las tareas complejas pueden recibir una respuesta parcial bajo este presupuesto. Inspecciona en DevUI cómo el gestor decide el siguiente paso y sintetiza la respuesta.

También prueba: **«Dame un título para mi canal de YouTube»**. El redactor debe proponer un título concreto sin bloquearse por detalles opcionales como la temática del canal. Reinicia DevUI después de modificar el ejemplo.

**Compatibilidad con DevUI `1.0.0b260910`:** el ejemplo añade `to_dict()` a `MagenticOrchestratorEvent` si no existe. Esto convierte el contenido del plan (`Message`) y los registros de progreso a datos serializables. Sin este adaptador, el streaming puede cortarse con `Unable to serialize unknown type: Message` y la interfaz queda mostrando el gestor en ejecución.

**Cuándo usarlo:** para tareas abiertas que requieren coordinación adaptable. Hace más llamadas y puede tardar más que los patrones anteriores; los agentes no navegan ni ejecutan acciones externas.

[Anterior: Handoff](../05_handoff/README.md) · [Índice del curso](../../README.md)
