from typing import Any

from utils import leer_json, leer_eliminadas_json


# Función para obtener el próximo ID
def obtener_proximo_id() -> int:
    datos: list[dict[str, Any]] = leer_json()
    datos_json_eliminados: list[dict[str, Any]] = leer_eliminadas_json()
    if not (datos and datos_json_eliminados):
        return 1
    datos.extend(datos_json_eliminados)
    return max(tarea["id"] for tarea in datos) + 1
