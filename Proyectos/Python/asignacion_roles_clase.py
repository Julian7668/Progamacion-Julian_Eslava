import questi
import validates as V
from utils import search_key_in_dict, get_ordinal

estudiantes: dict[str, int] = {}
for i in range(
    int(
        questi.text(
            "¿Cuantos estudiantes vinieron hoy a la clase?",
            validate=lambda x: V.validate_type(x, int)  # type: ignore
            and V.validate_range_num(int(x), (1, 100)),  # type: ignore
        )
    )
):
    nombre_estudiante = questi.text(
        f"Ingrese el nombre del {get_ordinal(i + 1)} estudiante:",
        validate=lambda x: x.capitalize() not in estudiantes,  # type: ignore
    ).capitalize()
    estudiantes[nombre_estudiante] = int(
        questi.text(
            f"Ingrese la edad de {nombre_estudiante}:",
            validate=lambda x: V.validate_type(x, int)  # type: ignore
            and V.validate_range_num((x := int(x)), (1, 100))  # type: ignore
            and x not in estudiantes.values(),
        )
    )
    print()

print(
    *(
        f"""{
            search_key_in_dict(
                estudiantes,
                sorted(estudiantes.values(), reverse=True)[(0 if i == 0 else -1)],
            )
        } sera el {"profesor" if i == 0 else "asistente"}"""
        for i in range(2)
    ),
    sep="\n",
)

