from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .routers import GET, POST, PUT, PATCH, DELETE, OTHERS

# Crear la aplicación FastAPI
app = FastAPI(
    title="API de Tareas", description="API para gestionar tareas", version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REGISTRAR TODOS LOS ROUTERS
app.include_router(GET.router, prefix="/tareas", tags=["📖 Obtener"])
app.include_router(POST.router, prefix="/tareas", tags=["➕ Crear"])
app.include_router(PUT.router, prefix="/tareas", tags=["📝 Actualizar"])
app.include_router(PATCH.router, prefix="/tareas", tags=["⚡ Parcial"])
app.include_router(DELETE.router, prefix="/tareas", tags=["🗑️ Eliminar"])
app.include_router(OTHERS.router, tags=["🌟 General"])

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
