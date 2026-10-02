# Clase 04 — Group Chat

**Objetivo del video:** enseñar colaboración iterativa con un coordinador que decide quién habla en cada turno.

```text
Usuario → investigador → redactor → investigador → redactor → respuesta
```

Abre DevUI con `uv run devui ./clases --port 8080` y selecciona `group_chat`. Prueba: **«Prepara una propuesta breve para mejorar la documentación de un equipo»**.

En [`__init__.py`](__init__.py), una función selecciona al siguiente participante por turnos y `max_rounds=4` pone un límite. Ambos agentes reciben el historial compartido. Observa cómo la segunda intervención puede modificar la primera propuesta.

**Cuándo usarlo:** cuando el trabajo necesita intercambio y refinamiento. Aquí la selección es determinista para que la demostración sea fácil de seguir.

[Anterior: Concurrent](../03_concurrent/README.md) · [Siguiente: Handoff](../05_handoff/README.md) · [Índice del curso](../../README.md)
