from fastapi import HTTPException, APIRouter

from constants import Tarea, TareaUpdate
from utils import leer_json, escribir_datos

router = APIRouter()


# PATCH - Actualizar parcialmente una tarea
@router.patch("/{tarea_id}", response_model=Tarea)
def actualizar_tarea_parcial(tarea_id: int, tarea_update: TareaUpdate):
    """Actualiza parcialmente una tarea existente"""
    datos = leer_json()

    for i, tarea_existente in enumerate(datos):
        if tarea_existente["id"] == tarea_id:
            # Actualizar solo los campos proporcionados
            if tarea_update.titulo is not None:
                datos[i]["titulo"] = tarea_update.titulo
            if tarea_update.descripcion is not None:
                datos[i]["descripcion"] = tarea_update.descripcion
            if tarea_update.completada is not None:
                datos[i]["completada"] = tarea_update.completada

            escribir_datos(datos)
            return datos[i]

    raise HTTPException(status_code=404, detail="Tarea no encontrada")
