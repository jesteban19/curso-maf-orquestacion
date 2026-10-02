# Clase 02 — Sequential

**Objetivo del video:** mostrar una secuencia fija en la que cada agente recibe el trabajo anterior. Este ejemplo adapta el `main.py` original.

```text
Usuario → planificador → ejecutor → revisor → respuesta final
```

Abre DevUI con `uv run devui ./clases --port 8080` y selecciona `sequential`. Prueba: **«Diseña un proceso para clasificar solicitudes de soporte»**.

En [`__init__.py`](__init__.py), `SequentialBuilder` fija el orden. El planificador propone pasos, el ejecutor desarrolla la respuesta y el revisor la corrige. En DevUI compara la contribución de cada etapa y observa que el contexto se acumula.

**Cuándo usarlo:** cuando los pasos dependen unos de otros y el orden ya se conoce. Suele requerir una llamada al modelo por participante.

[Anterior: Agente](../01_agente/README.md) · [Siguiente: Concurrent](../03_concurrent/README.md) · [Índice del curso](../../README.md)
