from typing import Any
from fastapi import APIRouter, HTTPException

from utils import leer_json, guardar_eliminada, escribir_datos

router = APIRouter()


# DELETE - Eliminar una tarea
@router.delete("/{tarea_id}")
def eliminar_tarea(tarea_id: int) -> dict[str, Any]:
    """Elimina una tarea específica"""
    datos = leer_json()

    for i, tarea in enumerate(datos):
        if tarea["id"] == tarea_id:
            tarea_eliminada = datos.pop(i)

            # Guardar en historial de eliminadas
            guardar_eliminada(tarea_eliminada)

            # Actualizar archivo principal
            escribir_datos(datos)

            return {"mensaje": "Tarea eliminada exitosamente", "tarea": tarea_eliminada}

    raise HTTPException(status_code=404, detail="Tarea no encontrada")
