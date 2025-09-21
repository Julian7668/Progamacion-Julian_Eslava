from fastapi import HTTPException, APIRouter

from ..constants import Tarea
from ..utils import leer_json, leer_eliminadas_json

router = APIRouter()


# GET - Obtener todas las tareas
@router.get("", response_model=list[Tarea])
def obtener_tareas():
    """Obtiene todas las tareas almacenadas"""
    return leer_json()


# GET - Obtener una tarea específica por ID
@router.get("/{tarea_id}", response_model=Tarea)
def obtener_tarea(tarea_id: int):
    """Obtiene una tarea específica por su ID"""
    datos = leer_json()

    # Buscar en tareas activas
    for tarea in datos:
        if tarea["id"] == tarea_id:
            return tarea

    # Si no está en activas, buscar en eliminadas
    eliminadas = leer_eliminadas_json()
    for tarea in eliminadas:
        if tarea["id"] == tarea_id:
            raise HTTPException(
                status_code=410,  # 410 = Gone (recurso eliminado)
                detail=f"La tarea con ID {tarea_id} fue eliminada el {tarea['fecha_eliminacion'][:10]}",
            )

    # Si no está en ningún lado, nunca existió
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
