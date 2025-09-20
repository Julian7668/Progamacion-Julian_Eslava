from typing import Union


def validate_type(
    x: str,
    target_type: type[Union[str, bool, int, float]],
    strict: bool = False,
) -> bool:
    """
    Valida si una cadena puede convertirse al tipo especificado.

    Realiza validación básica de formato para conversión de tipos desde string.

    Args:
        x: Cadena a validar.
        target_type: Tipo al que se quiere convertir (str, bool, int, float).
        strict: Si True, para float requiere punto decimal explícito.

    Returns:
        bool: True si la cadena puede convertirse al tipo, False en caso contrario.

    Examples:
        >>> validate_type("123", int)
        True
        >>> validate_type("true", bool)
        True
        >>> validate_type("3.14", float)
        True
        >>> validate_type("abc", int)
        False
    """
    if target_type is str:
        return True
    if target_type is bool:
        return x.capitalize() in ("T", "True", "F", "False")
    x = x.strip().lstrip("+-")

    if target_type is int:
        return x.isdigit()
    return ("." in x or not strict) and x.replace(".", "", 1).isdigit()


if __name__ == "__main__":
    # Ejemplos de validación de tipos
    test_cases: tuple[tuple[str, type], ...] = (
        ("123", int),
        ("true", bool),
        ("3.14", float),
        ("abc", int),
        ("True", bool),
        ("hello", str),
    )

    print("Ejemplos de validación de tipos:")
    for value, expected_type in test_cases:
        result = validate_type(value, expected_type)
        print(f"'{value}' -> {expected_type.__name__}: {result}")
