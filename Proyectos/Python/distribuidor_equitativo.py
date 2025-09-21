from typing import Union
import re
import questi
from utils import validate_type

cantidad_total: float = 0.0
grupos_deseados: int = 0
permite_medios: bool = False


def validar_entrada(x: str) -> bool:
    match = re.search(r"^([^/]+)/([^/]+)/([^/]+)$", x)
    if not match:
        return False

    if not (
        validate_type(match.group(1), float)
        and validate_type(match.group(2), int)
        and validate_type(match.group(3), bool)
    ):
        return False
    if float(match.group(1)) <= 0 or int(match.group(2)) <= 0:
        return False

    global cantidad_total, grupos_deseados, permite_medios
    cantidad_total = float(match.group(1))
    grupos_deseados = int(match.group(2))
    permite_medios = match.group(3).capitalize() in ("T", "True")

    if permite_medios:
        if cantidad_total % 1 not in (0, 0.5):
            return False
    else:
        if cantidad_total % 1 != 0:
            return False

    return grupos_deseados <= (int(cantidad_total) * (2 if permite_medios else 1))


questi.text(
    "Ingresa: cantidad_total/grupos_deseados/permite_medios (ej: 20/3/True)",
    validate=validar_entrada,
)


def redondeo_especial(num: float) -> float:
    entero = int(num)
    return min((entero, entero + 0.5, entero + 1), key=lambda x: abs(x - num))


A: float = cantidad_total / grupos_deseados
valores_redistribuidos: list[Union[float, int]] = [
    (redondeo_especial if permite_medios else round)(A)
]
for i in range(grupos_deseados - 1):
    valores_redistribuidos.append(
        (redondeo_especial if permite_medios else round)(
            (i + 2) * A - sum(valores_redistribuidos)
        )
    )

print(*valores_redistribuidos)
