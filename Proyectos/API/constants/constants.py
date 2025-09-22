import os

# Archivos JSON donde guardaremos los datos
DIR_DATA = os.path.join(os.path.dirname(__file__), "../data")
DATA_JSON = os.path.join(DIR_DATA, "tareas.json")
DELETED_JSON = os.path.join(DIR_DATA, "tareas_eliminadas.json")
