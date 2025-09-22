from datetime import datetime
from typing import Any
import json

from constants import DELETED_JSON
from .MDleer_eliminadas_json import leer_eliminadas_json


# Función para guardar tarea eliminada
def guardar_eliminada(tarea: dict[str, Any]) -> None:

    eliminadas: list[dict[str, Any]] = leer_eliminadas_json()
    # Agregar timestamp de cuando se eliminó
    tarea_eliminada: dict[str, Any] = tarea.copy()
    tarea_eliminada["fecha_eliminacion"] = datetime.now().isoformat()
    eliminadas.append(tarea_eliminada)

    with open(DELETED_JSON, "w", encoding="utf-8") as file:
        json.dump(eliminadas, file, indent=2, ensure_ascii=False)
