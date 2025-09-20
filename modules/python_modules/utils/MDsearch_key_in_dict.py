from typing import Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


def search_key_in_dict(diccionario: dict[K, V], valor: V) -> Optional[K]:
    """
    Busca la clave correspondiente a un valor específico en un diccionario.

    Retorna la primera clave que tenga el valor especificado, o None si no se encuentra.

    Args:
        diccionario: Diccionario en el que buscar.
        valor: Valor a buscar en el diccionario.

    Returns:
        Optional[K]: La clave correspondiente al valor, o None si no se encuentra.

    Examples:
        >>> d = {'a': 1, 'b': 2, 'c': 1}
        >>> search_key_in_dict(d, 1)
        'a'
        >>> search_key_in_dict(d, 3)
        None
    """
    return next((k for k, v in diccionario.items() if v == valor), None)


if __name__ == "__main__":
    # Ejemplos de búsqueda en diccionario
    ejemplo_dict = {
        'manzana_roja': 'roja',
        'banana': 'amarilla',
        'uva': 'morada',
        'manzana_verde': 'verde'
    }

    print("Diccionario de ejemplo:", ejemplo_dict)
    print("Buscar clave para 'amarilla':", search_key_in_dict(ejemplo_dict, 'amarilla'))
    print("Buscar clave para 'roja':", search_key_in_dict(ejemplo_dict, 'roja'))
    print("Buscar clave para 'azul':", search_key_in_dict(ejemplo_dict, 'azul'))
