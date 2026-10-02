# Clase 05 — Handoff

**Objetivo del video:** mostrar que un agente puede transferir la conversación a otro según el tema.

```text
Usuario → recepcion ─┬→ acceso
                     └→ facturacion
```

Abre DevUI con `uv run devui ./clases --port 8080` y selecciona `handoff`. Prueba: **«No puedo iniciar sesión en mi cuenta»** y luego **«Tengo una duda sobre un cobro»**.

En [`__init__.py`](__init__.py), `recepcion` es el punto de entrada y `.add_handoff(...)` define las rutas permitidas. El agente decide si usa la herramienta de traspaso. Cuando un especialista responde sin otro traspaso, el flujo puede pedir una nueva intervención del usuario: es una conversación interactiva.

**Cuándo usarlo:** cuando diferentes expertos deben hacerse cargo de consultas distintas. El ejemplo no accede a cuentas ni a pagos reales.

[Anterior: Group Chat](../04_group_chat/README.md) · [Siguiente: Magentic](../06_magentic/README.md) · [Índice del curso](../../README.md)
