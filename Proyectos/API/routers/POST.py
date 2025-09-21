from fastapi import APIRouter

from ..constants import Tarea
from ..utils import leer_json, obtener_proximo_id, escribir_datos

router = APIRouter()


# POST - Crear una nueva tarea
@router.post("", response_model=Tarea)
def crear_tarea(tarea: Tarea):
    """Crea una nueva tarea"""
    datos = leer_json()

    # Asignar ID automáticamente
    nueva_tarea = tarea.model_dump()
    nueva_tarea["id"] = obtener_proximo_id()

    # Agregar la nueva tarea a los datos
    datos.append(nueva_tarea)
    escribir_datos(datos)

    return nueva_tarea
