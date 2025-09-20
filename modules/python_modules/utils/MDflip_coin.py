import random


def flip_coin() -> str:
    """
    Simula el lanzamiento de una moneda.

    Retorna aleatoriamente "Cara" o "Cruz" con igual probabilidad.

    Returns:
        str: "Cara" o "Cruz"

    Example:
        >>> flip_coin()
        'Cara'
        >>> flip_coin()
        'Cruz'
    """
    return random.choice(["Cara", "Cruz"])


if __name__ == "__main__":
    # Ejemplos de lanzamiento de moneda
    print("Lanzamientos de moneda:")
    for i in range(5):
        resultado = flip_coin()
        print(f"Lanzamiento {i+1}: {resultado}")
