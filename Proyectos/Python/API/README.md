# Documentación de la API de Gestión de Usuarios

Esta API permite gestionar una lista de usuarios mediante operaciones CRUD básicas. Está construida con **FastAPI** para el backend y utiliza un frontend simple en HTML/CSS/JavaScript para la interacción.

## Estructura del Proyecto

- `backend.py`: Servidor FastAPI con los endpoints de la API.
- `frontend.html`: Interfaz de usuario web.
- `main.js`: Lógica JavaScript para interactuar con la API.
- `styles.css`: Estilos CSS para el frontend.
- `users_data.json`: Archivo JSON donde se almacenan los datos de los usuarios.

## Instalación y Ejecución

### Requisitos Previos

- Python 3.7+
- FastAPI: `pip install fastapi`
- Uvicorn: `pip install uvicorn`
- Pydantic: `pip install pydantic`

### Ejecutar el Servidor

1. Navega al directorio `API/`:
   ```
   cd API
   ```

2. Ejecuta el servidor con Uvicorn:
   ```
   uvicorn backend:app --reload
   ```

3. Abre tu navegador y ve a `http://localhost:8000` para acceder al frontend, o usa `http://localhost:8000/docs` para la documentación interactiva de FastAPI.

## Endpoints de la API

### Modelo de Datos

Los usuarios tienen la siguiente estructura:

```json
{
  "id": 1,
  "name": "Nombre del usuario",
  "age": 25
}
```

### Endpoints Disponibles

#### 1. GET /
- **Descripción**: Mensaje de bienvenida.
- **Respuesta**:
  ```json
  {
    "message": "Bienvenido a la API de Usuarios"
  }
  ```

#### 2. GET /users
- **Descripción**: Obtiene la lista completa de usuarios.
- **Respuesta**:
  ```json
  [
    {
      "id": 1,
      "name": "Julian",
      "age": 15
    },
    ...
  ]
  ```

#### 3. POST /users
- **Descripción**: Crea un nuevo usuario.
- **Cuerpo de la solicitud**:
  ```json
  {
    "name": "Nuevo Usuario",
    "age": 30
  }
  ```
- **Respuesta**: No devuelve contenido específico, pero guarda el usuario en `users_data.json`.

#### 4. GET /users/{user_id}
- **Descripción**: Obtiene un usuario específico por ID.
- **Parámetros**:
  - `user_id` (int): ID del usuario.
- **Respuesta** (si existe):
  ```json
  {
    "id": 1,
    "name": "Julian",
    "age": 15
  }
  ```
- **Respuesta** (si no existe):
  ```json
  {
    "error": "Usuario no encontrado"
  }
  ```

## Notas Importantes

- Los datos se almacenan en `users_data.json` en el directorio raíz de la API.
- CORS está configurado para permitir todas las orígenes (`*`), pero en producción se recomienda restringir a dominios específicos.
- El frontend incluye funcionalidades para crear, listar y eliminar usuarios, pero la eliminación no está implementada en el backend (solo en el frontend). Para una implementación completa, agrega un endpoint DELETE en `backend.py`.
- La API genera IDs únicos automáticamente para nuevos usuarios.

## Uso del Frontend

1. Abre `frontend.html` en un navegador (o accede vía el servidor en `http://localhost:8000`).
2. Ingresa nombre y edad, luego haz clic en "Crear Usuario".
3. Haz clic en "Cargar Usuarios" para ver la lista actualizada.
4. Usa el botón "Eliminar" junto a cada usuario para removerlo (nota: requiere implementación backend).

## Contribución

Para mejoras o correcciones, edita los archivos correspondientes y reinicia el servidor.