from typing import Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


def search_key_in_dict(diccionario: dict[K, V], valor: V) -> Optional[K]:
    return next((k for k, v in diccionario.items() if v == valor), None)
