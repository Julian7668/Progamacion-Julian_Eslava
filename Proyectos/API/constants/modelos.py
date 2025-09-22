from typing import Optional
from pydantic import BaseModel


# Modelo de datos para las tareas
class Tarea(BaseModel):
    id: Optional[int] = None
    titulo: str
    descripcion: str
    completada: bool = False


class TareaUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    completada: Optional[bool] = None
