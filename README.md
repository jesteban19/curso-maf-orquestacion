# Curso de orquestación con Microsoft Agent Framework

Repositorio de ejemplos para una serie de YouTube. Cada carpeta de `clases/` corresponde a un video y contiene un ejemplo que DevUI puede descubrir, además de su propia guía. Los ejemplos usan el mismo endpoint compatible con OpenAI de Azure que utilizaba el `main.py` original.

## Ruta del curso

| Clase | Tema | Idea central |
| --- | --- | --- |
| [01](clases/01_agente/README.md) | Agente | Una petición, un agente y una respuesta. |
| [02](clases/02_sequential/README.md) | Sequential | Planificador, ejecutor y revisor en orden. |
| [03](clases/03_concurrent/README.md) | Concurrent | Tres perspectivas independientes sobre la misma entrada. |
| [04](clases/04_group_chat/README.md) | Group Chat | Participantes que alternan turnos y comparten contexto. |
| [05](clases/05_handoff/README.md) | Handoff | Un agente transfiere la conversación al especialista. |
| [06](clases/06_magentic/README.md) | Magentic | Un gestor planifica, asigna y revisa el trabajo. |

`clases/` se pasa directamente a DevUI. Cada `__init__.py` exporta `agent` o `workflow`, según el ejemplo. Las clases son independientes para que cada video se pueda seguir sin editar las demás.

## Preparación

1. Instala Python 3.11 o superior y [uv](https://docs.astral.sh/uv/).
2. Desde la raíz del repositorio, instala las dependencias:

   ```powershell
   uv sync --locked
   ```

3. Copia `.env.example` a `.env` y configura `TOKEN`, `ENDPOINT` y `MODEL` con los datos de tu despliegue de Azure. El endpoint debe terminar en `/openai/v1`. `.env` está excluido de Git.
4. Inicia DevUI desde la raíz:

   ```powershell
   uv run devui ./clases --port 8080
   ```

5. Abre la dirección local que muestra DevUI, selecciona la clase y envía el ejemplo sugerido en su README. Si DevUI imprime un token de acceso al iniciar, úsalo en la interfaz y mantenlo privado.

DevUI permite inspeccionar la conversación y el recorrido de cada workflow. Es una interfaz de desarrollo, no una aplicación de producción. Cada llamada al modelo puede consumir cuota y generar costo; Magentic y los patrones con varios agentes suelen hacer más llamadas que la clase 01.

## Configuración

| Variable | Uso |
| --- | --- |
| `TOKEN` | Credencial del endpoint de Azure. |
| `ENDPOINT` | URL base compatible con OpenAI, terminada en `/openai/v1`. |
| `MODEL` | Nombre del despliegue accesible en el recurso. |

Cada módulo carga el `.env` de la raíz. Los ejemplos hacen tareas de texto y no tienen acceso a archivos, navegación ni sistemas externos. Sus respuestas no equivalen a verificaciones reales.

## Referencias

- [Patrones de orquestación de Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/)
- [Descubrimiento de ejemplos en DevUI](https://learn.microsoft.com/en-us/agent-framework/devui/directory-discovery)
- [DevUI](https://learn.microsoft.com/en-us/agent-framework/user-guide/devui/)
