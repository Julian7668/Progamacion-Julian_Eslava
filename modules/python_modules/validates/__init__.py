"""
Módulo validates: Funciones de validación para el proyecto.

Contiene funciones para validar:
- Conversión de tipos desde strings
- Rangos numéricos con límites inclusivos/exclusivos
"""

from .MDvalidate_type import validate_type
from .MDvalidate_range_num import validate_range_num

__all__ = ["validate_type", "validate_range_num"]
