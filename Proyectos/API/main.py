import os
from typing import Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .constants import DIR_DATA, Tarea, TareaUpdate
from .utils import (
    leer_json,
    leer_eliminadas_json,
    obtener_proximo_id,
    escribir_datos,
    guardar_eliminada,
)

# Crear la aplicación FastAPI
app = FastAPI(
    title="API de Tareas", description="API para gestionar tareas", version="1.0.0"
)

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear directorio data si no existe
os.makedirs(DIR_DATA, exist_ok=True)


# ! ENDPOINTS DE LA API


# GET - Obtener todas las tareas
@app.get("/tareas", response_model=list[Tarea])
def obtener_tareas():
    """Obtiene todas las tareas almacenadas"""
    return leer_json()


# GET - Obtener una tarea específica por ID
@app.get("/tareas/{tarea_id}", response_model=Tarea)
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


# POST - Crear una nueva tarea
@app.post("/tareas", response_model=Tarea)
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


# PUT - Actualizar una tarea completa
@app.put("/tareas/{tarea_id}", response_model=Tarea)
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


# PATCH - Actualizar parcialmente una tarea
@app.patch("/tareas/{tarea_id}", response_model=Tarea)
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


# DELETE - Eliminar una tarea
@app.delete("/tareas/{tarea_id}")
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


# Endpoint raíz
@app.get("/")
def read_root():
    return {"mensaje": "¡API de Tareas funcionando!", "documentacion": "/docs"}


# Servir archivos estáticos (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Servir el archivo HTML principal
@app.get("/app")
def get_frontend():
    return FileResponse("static/index.html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
