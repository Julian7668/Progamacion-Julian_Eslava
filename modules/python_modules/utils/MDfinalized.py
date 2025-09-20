import sys
from typing import NoReturn

mensaje_final = "Programa finalizado"


def finalized(mensaje: str = "") -> NoReturn:
    """
    Finaliza el programa con un mensaje formateado.

    Imprime un mensaje rodeado de un marco de caracteres '=' y termina
    la ejecución del programa usando sys.exit().

    Args:
        mensaje: Mensaje personalizado a mostrar. Si está vacío,
                usa el mensaje por defecto "Programa finalizado".

    Returns:
        NoReturn: Esta función nunca retorna, termina el programa.

    Example:
        >>> finalized("Proceso completado")
        ======================
          Proceso completado
        ======================
        # Programa termina aquí
    """
    mensaje = mensaje or mensaje_final
    marco = "=" * (len(mensaje) + 4)
    print(
        f"""
{marco}
  {mensaje}
{marco}"""
    )
    sys.exit()


if __name__ == "__main__":
    # Ejemplos de uso de finalized
    print("Ejemplo 1: Mensaje por defecto")
    # finalized()  # Esto terminaría el programa

    print("Ejemplo 2: Mensaje personalizado")
    # finalized("¡Hasta luego!")  # Esto también terminaría el programa

    print("Los ejemplos anteriores están comentados para evitar terminar el programa.")
    print("Descomenta las líneas para probarlos.")
