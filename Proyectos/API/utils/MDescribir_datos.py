from typing import Any
import json
from ..constants import DATA_JSON


# Función para escribir datos al archivo JSON
def escribir_datos(datos: list[dict[str, Any]]) -> None:
    with open(DATA_JSON, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=2, ensure_ascii=False)
