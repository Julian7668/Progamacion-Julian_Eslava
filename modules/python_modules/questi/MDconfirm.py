from typing import Any, Callable, Optional, Union, cast
import questionary
from prompt_toolkit.styles import Style
from questionary.constants import DEFAULT_QUESTION_PREFIX

from questi.MDtext import questi_decorator


@questi_decorator
def confirm(
    message: str,
    default: bool = True,
    qmark: str = DEFAULT_QUESTION_PREFIX,
    style: Optional[Style] = None,
    auto_enter: bool = True,
    instruction: Optional[str] = None,
    exit_callback: Optional[Callable[[], Any]] = None,
    **kwargs: Any,
) -> Optional[bool]:
    """
    Solicita confirmación al usuario (T/f).

    Esta función es un wrapper de questionary.confirm() con manejo de cancelación.

    Args:
        message: El mensaje a mostrar al usuario.
        default: Valor por defecto (True para sí, False para no).
        qmark: Marcador de pregunta (por defecto '?').
        style: Estilo de prompt_toolkit para el prompt.
        auto_enter: Si presionar Enter confirma el valor por defecto.
        instruction: Instrucciones adicionales para el usuario.
        exit_callback: Función a llamar si el usuario cancela.
        **kwargs: Argumentos adicionales para questionary.confirm().

    Returns:
        True si el usuario confirma, False si niega, o None si se cancela sin exit_callback,
        o el resultado de exit_callback si se proporciona.
    """
    return questionary.confirm(
        message,
        default,
        qmark,
        style,
        auto_enter,
        instruction,
        **kwargs,
    ).ask()


if __name__ == "__main__":
    import questi

    # * ejemplo sin exit_callback
    print(questi.confirm("¿Chanchi?"))

    # * ejemplo con exit_callback
    from utils import flip_coin

    resultado = cast(
        Union[bool, Callable[[], str]],
        questi.confirm("¿Chanchi?", exit_callback=flip_coin),
    )
    print(resultado if isinstance(resultado, bool) else resultado())
