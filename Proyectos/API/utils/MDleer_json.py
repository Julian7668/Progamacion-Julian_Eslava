import os
import json
from typing import Any
from ..constants import DATA_JSON


# Función para leer datos del archivo JSON
def leer_json() -> list[dict[str, Any]]:
    if not os.path.exists(DATA_JSON):
        return []
    try:
        with open(DATA_JSON, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
