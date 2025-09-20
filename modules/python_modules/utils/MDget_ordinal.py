from typing import Literal
from pydantic import Field, validate_call

from utils._ordinales_data import ORDINALES_FEMENINO, ORDINALES_MASCULINO


@validate_call
def get_ordinal(
    numero: int = Field(ge=1, le=30), genero: Literal["M", "F"] = "M"
) -> str:
    """
    Obtiene el ordinal en español correspondiente a un número.

    Soporta números del 1 al 30 con género masculino o femenino.

    Args:
        numero: Número entero entre 1 y 30 (validado por pydantic).
        genero: Género del ordinal ("M" para masculino, "F" para femenino).

    Returns:
        str: El ordinal en español correspondiente.

    Raises:
        ValidationError: Si numero está fuera del rango 1-30.

    Examples:
        >>> get_ordinal(1, "M")
        'primer'
        >>> get_ordinal(2, "F")
        'segunda'
        >>> get_ordinal(21, "M")
        'vigésimo primer'
    """
    if genero == "M":
        return ORDINALES_MASCULINO[numero - 1]
    return ORDINALES_FEMENINO[numero - 1]


if __name__ == "__main__":
    # Ejemplos de uso
    print("Ejemplos de ordinales:")
    for i in [1, 2, 11, 21]:
        print(f"{i}º (M): {get_ordinal(i, 'M')}")
        print(f"{i}ª (F): {get_ordinal(i, 'F')}")
