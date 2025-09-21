from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("")
def read_root():
    return {"mensaje": "¡API de Tareas funcionando!", "documentacion": "/docs"}


@router.get("/app")
def get_frontend():
    return FileResponse("static/index.html")
