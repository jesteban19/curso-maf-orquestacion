# Clase 03 — Concurrent

**Objetivo del video:** pedir perspectivas independientes sobre una misma tarea y reunirlas en una salida.

```text
               ┌→ beneficios ───────┐
Usuario ───────┼→ riesgos ──────────┼→ resultados agregados
               └→ implementacion ───┘
```

Abre DevUI con `uv run devui ./clases --port 8080` y selecciona `concurrent`. Prueba: **«Evalúa la idea de crear un portal interno de preguntas frecuentes»**.

En [`__init__.py`](__init__.py), `ConcurrentBuilder` envía la misma petición a tres agentes. Cada uno aporta un enfoque distinto. El agregador predeterminado devuelve las respuestas juntas; no crea por sí solo una conclusión consensuada.

**Cuándo usarlo:** cuando los trabajos no dependen entre sí. Compara el recorrido con Sequential y observa que el número de llamadas sigue siendo uno por participante.

[Anterior: Sequential](../02_sequential/README.md) · [Siguiente: Group Chat](../04_group_chat/README.md) · [Índice del curso](../../README.md)
