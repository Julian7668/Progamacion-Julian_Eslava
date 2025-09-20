import json
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción usar dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Modelo de datos
class User(BaseModel):
    name: str
    age: int


# Nombre del archivo JSON
JSON_FILE = "users_data.json"


# Función para cargar usuarios desde JSON
def load_users():
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("users", [])
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    else:
        return []


# Función para guardar usuarios en JSON
def save_users(users_list):
    data = {"users": users_list}
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


# Cargar usuarios al iniciar la aplicación
users_db = load_users()


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Usuarios"}


@app.get("/users")
def get_all_users():
    return users_db


@app.post("/users")
def _create_user(user: User):
    # Generar ID único
    new_id = max((u.get("id", 0) for u in users_db), default=0) + 1

    user_dict = user.model_dump()
    user_dict["id"] = new_id

    # Agregar a la lista en memoria
    users_db.append(user_dict)

    # Guardar en JSON
    save_users(users_db)


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users_db if u["id"] == user_id), None)
    if user:
        return user
    return {"error": "Usuario no encontrado"}
