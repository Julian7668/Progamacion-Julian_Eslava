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
def load_users() -> list:
    """
    Carga la lista de usuarios desde el archivo JSON especificado.

    Returns:
        list: Lista de diccionarios con los datos de los usuarios. Si el archivo no existe o hay un error, retorna una lista vacía.
    """
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("users", [])
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []


# Función para guardar usuarios en JSON
def save_users(users_list) -> None:
    """
    Guarda la lista de usuarios en el archivo JSON especificado.

    Args:
        users_list (list): Lista de diccionarios con los datos de los usuarios.
    """
    data = {"users": users_list}
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


# Cargar usuarios al iniciar la aplicación
users_db = load_users()


@app.get("/")
def read_root() -> dict:
    """
    Endpoint raíz que devuelve un mensaje de bienvenida.

    Returns:
        dict: Diccionario con un mensaje de bienvenida.
    """
    return {"message": "Bienvenido a la API de Usuarios"}


@app.get("/users")
def get_all_users() -> list:
    """
    Endpoint para obtener la lista completa de usuarios.

    Returns:
        list: Lista de diccionarios con los datos de todos los usuarios.
    """
    return users_db


@app.post("/users")
def _create_user(user: User):
    """
    Endpoint para crear un nuevo usuario.

    Args:
        user (User): Objeto User con nombre y edad.

    Returns:
        dict: Usuario creado con su ID asignado.
    """
    # Generar ID único
    new_id = max((u.get("id", 0) for u in users_db), default=0) + 1

    user_dict = user.model_dump()
    user_dict["id"] = new_id

    # Primero agregar a la lista en memoria
    users_db.append(user_dict)

    # Luego guardar toda la lista en JSON
    save_users(users_db)  # ← Pasa toda la lista

    return user_dict  # ← Mejor devolver el usuario creado


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict:
    """
    Endpoint para obtener un usuario específico por ID.

    Args:
        user_id (int): ID del usuario a buscar.

    Returns:
        dict: Diccionario con los datos del usuario si existe, o un mensaje de error.
    """
    user = next((u for u in users_db if u["id"] == user_id), None)
    if user:
        return user
    return {"error": "Usuario no encontrado"}
