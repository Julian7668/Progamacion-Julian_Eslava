from typing import Union


def validate_range_num(
    number: Union[float, int],
    validation_range: tuple[
        Union[float, tuple[float, bool]], Union[float, tuple[float, bool]]
    ] = (float("-inf"), float("inf")),
) -> bool:
    if not isinstance(validation_range[0], tuple):
        minimo_rango: bool = number >= validation_range[0]
    else:
        minimo_rango: bool = (
            number >= validation_range[0][0]
            if validation_range[0][1]
            else number > validation_range[0][0]
        )
    if not minimo_rango:
        return minimo_rango

    if not isinstance(validation_range[1], tuple):
        maximo_rango: bool = number <= validation_range[1]
    else:
        maximo_rango: bool = (
            number <= validation_range[1][0]
            if validation_range[1][1]
            else number < validation_range[1][0]
        )
    return minimo_rango and maximo_rango
