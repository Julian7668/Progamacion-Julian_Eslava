"""
Módulo utils: Utilidades generales para el proyecto.

Contiene funciones de utilidad comunes como:
- Finalización de programa con mensaje formateado
- Simulación de lanzamiento de moneda
- Búsqueda de claves en diccionarios
- Obtención de ordinales en español
- Verificación de números primos
"""

from .MDfinalized import finalized
from .MDflip_coin import flip_coin
from .MDsearch_key_in_dict import search_key_in_dict
from .MDget_ordinal import get_ordinal
from .MDis_number_prime import is_number_prime

__all__ = [
    "finalized",
    "flip_coin",
    "search_key_in_dict",
    "get_ordinal",
    "is_number_prime",
]
