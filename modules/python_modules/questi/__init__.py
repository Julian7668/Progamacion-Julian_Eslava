"""
Módulo questi: Wrapper mejorado para la librería questionary.

Proporciona funciones para interactuar con el usuario mediante prompts,
con manejo robusto de cancelaciones (retorna None en cancelación) y callbacks opcionales.
"""

from .MDtext import text
from .MDselect import select
from .MDconfirm import confirm

__all__ = ["text", "select", "confirm"]
