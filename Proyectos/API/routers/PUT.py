from fastapi import HTTPException, APIRouter

from ..constants import Tarea
from ..utils import leer_json, escribir_datos

router = APIRouter()


# PUT - Actualizar una tarea completa
@router.put("/{tarea_id}", response_model=Tarea)
def actualizar_tarea_completa(tarea_id: int, tarea: Tarea):
    """Actualiza completamente una tarea existente"""
    datos = leer_json()

    for i, tarea_existente in enumerate(datos):
        if tarea_existente["id"] == tarea_id:
            # Mantener el ID original
            tarea_actualizada = tarea.model_dump()
            tarea_actualizada["id"] = tarea_id
            datos[i] = tarea_actualizada
            escribir_datos(datos)
            return tarea_actualizada

    raise HTTPException(status_code=404, detail="Tarea no encontrada")
