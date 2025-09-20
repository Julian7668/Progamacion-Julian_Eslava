from typing import Union
import re
import questi
import validates as V

cantidad_total: float = float(
    (
        answer := questi.text(
            "Ingresa: cantidad_total/grupos_deseados/permite_medios (ej: 20/3/True)",
            validate=lambda x: (
                bool(match := re.search(r"^([^/]+)/([^/]+)/([^/]+)$", x))
                and (
                    V.validate_type(match.group(1), float)
                    and V.validate_range_num(
                        float(match.group(1)), ((0, False), float("inf"))
                    )
                    and (
                        not V.validate_type(match.group(1), float, strict=True)
                        or (
                            int(float(match.group(1))) == (float(match.group(1)) - 0.5)
                            or int(float(match.group(1))) == float(match.group(1))
                        )
                    )
                )
                and (
                    V.validate_type(match.group(2), int)
                    and V.validate_range_num(
                        int(match.group(2)), ((0, False), float("inf"))
                    )
                )
                and V.validate_type(match.group(3), bool)
                and (
                    int(match.group(2))
                    <= int(float(match.group(1)))
                    * (2 if match.group(3).capitalize() in ("T", "True") else 1)
                )
            ),
        ).split("/")
    )[0]
)
grupos_deseados: int = int(answer[1])
permite_medios: bool = answer[2].capitalize() in ("T", "True")


def redondeo_especial(num: float) -> float:
    return min(
        ((entero := int(num)), entero + 0.5, entero + 1), key=lambda x: abs(x - num)
    )


valores_redistribuidos: list[Union[float, int]] = [
    (redondeo_especial if permite_medios else round)(
        A := cantidad_total / grupos_deseados
    )
]
for i in range(grupos_deseados - 1):
    valores_redistribuidos.append(
        (redondeo_especial if permite_medios else round)(
            (i + 2) * A - sum(valores_redistribuidos)
        )
    )

print(valores_redistribuidos)
