# Clase 01 — Agente

**Objetivo del video:** crear un agente básico y reconocer sus tres piezas: cliente de modelo, instrucciones y petición del usuario.

```text
Usuario → asistente_basico → respuesta
```

Abre DevUI con `uv run devui ./clases --port 8080` y selecciona `asistente_basico`. Prueba: **«Explica con un ejemplo qué es la orquestación de agentes»**.

En [`__init__.py`](__init__.py) se configura el cliente de Azure y se exporta `agent`. Observa cómo las instrucciones delimitan la respuesta y qué sucede si faltan datos. Esta clase sirve de referencia para comparar latencia, costo y complejidad con las siguientes.

**Límite:** no hay coordinación entre agentes ni herramientas externas.

[Siguiente: Sequential](../02_sequential/README.md) · [Índice del curso](../../README.md)
