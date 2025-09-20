from typing import Any, Callable, Optional, Union, ParamSpec, cast, TypeVar
from functools import wraps
import questionary
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.styles import Style
from questionary.constants import DEFAULT_QUESTION_PREFIX

from utils import finalized

P = ParamSpec("P")
T = TypeVar("T", bound=Optional[Union[str, bool]])


def questi_decorator(
    func: Callable[P, T],
) -> Callable[P, Union[T, Callable[[], Any]]]:
    """
    Decorador para funciones de questi que maneja la cancelación del usuario.

    Si la función subyacente retorna un valor no None, lo retorna directamente.
    Si retorna None (cancelación por teclado), maneja el exit_callback:
    - Si se proporciona exit_callback, retorna el callable para ejecución posterior.
    - Si no, llama a finalized() que termina el programa.

    Args:
        func: La función a decorar que retorna Optional[Union[str, bool]].

    Returns:
        La función decorada que puede retornar el resultado original o un callable.
    """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Union[T, Callable[[], Any]]:
        resultado = func(*args, **kwargs)
        if resultado is not None:
            return resultado
        # Si resultado es None (cancelación por teclado)
        exit_callback = cast(Optional[Callable[[], Any]], kwargs.get("exit_callback"))
        return exit_callback if exit_callback else finalized()

    return wrapper


@questi_decorator
def text(
    message: str,
    default: str = "",
    validate: Any = None,
    qmark: str = DEFAULT_QUESTION_PREFIX,
    style: Optional[Style] = None,
    multiline: bool = False,
    instruction: Optional[str] = None,
    lexer: Optional[Lexer] = None,
    exit_callback: Optional[Callable[[], Any]] = None,
    **kwargs: Any,
) -> Optional[str]:
    """
    Solicita entrada de texto al usuario con validación opcional.

    Esta función es un wrapper de questionary.text() con manejo de cancelación.

    Args:
        message: El mensaje a mostrar al usuario.
        default: Valor por defecto si el usuario no ingresa nada.
        validate: Función de validación para la entrada.
        qmark: Marcador de pregunta (por defecto '?').
        style: Estilo de prompt_toolkit para el prompt.
        multiline: Si permite entrada multilinea.
        instruction: Instrucciones adicionales para el usuario.
        lexer: Lexer para resaltar sintaxis.
        exit_callback: Función a llamar si el usuario cancela.
        **kwargs: Argumentos adicionales para questionary.text().

    Returns:
        La cadena ingresada por el usuario, o None si se cancela sin exit_callback,
        o el resultado de exit_callback si se proporciona.
    """
    return questionary.text(
        message,
        default,
        validate,
        qmark,
        style,
        multiline,
        instruction,
        lexer,
        **kwargs,
    ).ask()


if __name__ == "__main__":
    import questi
    import validates as V

    # * ejemplo sin exit_callback
    result = cast(
        str,
        questi.text(
            "Ingresa un entero entre el -10 y el 10:",
            validate=lambda x: V.validate_type(x, int)
            and V.validate_range_num(int(x), ((-10, False), (10, False))),
        ),
    )
    print(int(result))

    # * ejemplo con exit_callback
    from utils import flip_coin

    result = cast(
        Union[str, Callable[[], str]],
        questi.text(
            "Ingresa un flotante del 0 al 10:",
            validate=lambda x: V.validate_type(x, float)
            and V.validate_range_num(float(x), (0, 10)),
            exit_callback=flip_coin,
        ),
    )
    print(float(result) if isinstance(result, str) else result())
