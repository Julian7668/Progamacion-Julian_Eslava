import sys
from typing import NoReturn

mensaje_final = "Programa finalizado"


def finalized(mensaje: str = "") -> NoReturn:
    print(
        f"""
{(marco := "=" * (len(mensaje := mensaje or mensaje_final) + 4))}
  {mensaje}
{marco}"""
    )
    sys.exit(0)


if __name__ == "__main__":
    finalized()
