from typing import cast
import questi
from utils import search_key_in_dict, get_ordinal, validate_type

estudiantes: dict[str, int] = {}
rango = int(
    cast(
        str,
        questi.text(
            "¿Cuantos estudiantes vinieron hoy a la clase?",
            validate=lambda x: validate_type(x, int) and 1 <= int(x) <= 100,
        ),
    )
)

for i in range(rango):
    nombre_estudiante = cast(
        str,
        questi.text(
            f"Ingrese el nombre del {get_ordinal(i + 1)} estudiante:",
            validate=lambda x: x.capitalize() not in estudiantes,
        ),
    ).capitalize()

    estudiantes[nombre_estudiante] = int(
        cast(
            str,
            questi.text(
                f"Ingrese la edad de {nombre_estudiante}:",
                validate=lambda x: validate_type(x, int)
                and (x := int(x)) not in estudiantes.values()
                and 1 <= x <= 100,
            ),
        )
    )
    print()

estudiantes_ordenados = sorted(estudiantes.values(), reverse=True)

print(search_key_in_dict(estudiantes, estudiantes_ordenados[0]), "Sera el profesor")
print(search_key_in_dict(estudiantes, estudiantes_ordenados[-1]), "Sera el asistente")
