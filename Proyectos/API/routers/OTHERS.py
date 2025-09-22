import os
from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/")
def read_root():
    return {"mensaje": "¡API de Tareas funcionando!", "documentacion": "/docs"}


@router.get("/app")
def get_frontend():
    static_path = os.path.join(os.path.dirname(__file__), "../static/index.html")
    return FileResponse(static_path)
