import os
from typing import Any
import json
from constants import DELETED_JSON


# Función para leer tareas eliminadas
def leer_eliminadas_json() -> list[dict[str, Any]]:
    if not os.path.exists(DELETED_JSON):
        return []
    try:
        with open(DELETED_JSON, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
