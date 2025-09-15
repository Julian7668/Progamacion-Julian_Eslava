import sys
from typing import NoReturn

mensaje_final = "Programa finalizado"


def finalized(mensaje: str = "") -> NoReturn:
    mensaje = mensaje or mensaje_final
    marco = "=" * (len(mensaje))
    print(
        f"""
{marco}
  {mensaje}
{marco}"""
    )
    sys.exit()


if __name__ == "__main__":
    finalized()
