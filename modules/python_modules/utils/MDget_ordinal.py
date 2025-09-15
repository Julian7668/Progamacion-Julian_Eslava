from typing import Literal
from pydantic import Field, validate_call
from ._ordinales_data import ORDINALES_MASCULINO, ORDINALES_FEMENINO


@validate_call
def get_ordinal(
    numero: int = Field(ge=1, le=30), genero: Literal["M", "F"] = "M"
) -> str:
    if genero == "M":
        return ORDINALES_MASCULINO[numero - 1]
    return ORDINALES_FEMENINO[numero - 1]
