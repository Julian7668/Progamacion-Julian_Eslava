from typing import Union


def validate_range_num(
    number: Union[float, int],
    validation_range: tuple[
        Union[float, tuple[float, bool]], Union[float, tuple[float, bool]]
    ],
) -> bool:
    """
    Valida si un número está dentro de un rango especificado.

    Soporta rangos inclusivos y exclusivos mediante tuplas con booleanos.
    Si se pasa un número simple, se asume inclusivo.

    Args:
        number: Número a validar (int o float).
        validation_range: Tupla de dos elementos definiendo el rango:
            - Cada elemento puede ser:
                * float/int: Límite inclusivo
                * tuple[float/int, bool]: (límite, inclusivo)
                  donde bool=True significa inclusivo, False=exclusivo

    Returns:
        bool: True si el número está en el rango, False en caso contrario.

    Raises:
        ValueError: Si el formato del rango no es válido.

    Examples:
        >>> validate_range_num(5, (1, 10))  # 1 <= 5 <= 10
        True
        >>> validate_range_num(5, ((1, False), (10, True)))  # 1 < 5 <= 10
        True
        >>> validate_range_num(1, ((1, False), (10, True)))  # 1 < 1 <= 10
        False
    """
    try:
        if not isinstance(validation_range[0], tuple):
            minimo_rango: bool = number >= validation_range[0]
        else:
            if len(validation_range[0]) != 2:
                raise ValueError("Tupla de límite inferior debe tener exactamente 2 elementos")
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
            if len(validation_range[1]) != 2:
                raise ValueError("Tupla de límite superior debe tener exactamente 2 elementos")
            maximo_rango: bool = (
                number <= validation_range[1][0]
                if validation_range[1][1]
                else number < validation_range[1][0]
            )
        return minimo_rango and maximo_rango
    except (IndexError, TypeError) as e:
        raise ValueError(f"Formato de rango inválido: {e}") from e


if __name__ == "__main__":
    # Ejemplos de validación de rangos
    print("Ejemplos de validación de rangos:")

    # Rango simple inclusivo
    print("5 en rango (1, 10):", validate_range_num(5, (1, 10)))

    # Rango con límites exclusivos
    print("5 en rango ((1, False), (10, True)):", validate_range_num(5, ((1, False), (10, True))))

    # Caso fuera de rango
    print("15 en rango (1, 10):", validate_range_num(15, (1, 10)))

    # Caso límite
    print("1 en rango ((1, False), (10, True)):", validate_range_num(1, ((1, False), (10, True))))
