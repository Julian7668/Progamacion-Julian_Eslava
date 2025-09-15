from typing import Any, Callable, NoReturn, Optional, Union, ParamSpec, cast
from functools import wraps
import questionary
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.styles import Style
from questionary.constants import DEFAULT_QUESTION_PREFIX

from utils import finalized


P = ParamSpec("P")
type_of_exit_callback = Callable[[], Any]
type_of_wrapper = Union[Union[str, bool], Union[type_of_exit_callback, NoReturn]]


def questi_decorator(
    func: Callable[P, Optional[Union[str, bool]]],
) -> Callable[P, type_of_wrapper]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> type_of_wrapper:
        resultado: Union[Union[str, bool], None] = func(*args, **kwargs)
        if resultado is not None:
            return resultado
        exit_callback: Optional[type_of_exit_callback] = cast(
            Optional[type_of_exit_callback], kwargs.get("exit_callback")
        )
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
    exit_callback: Optional[type_of_exit_callback] = None,
    **kwargs: Any,
) -> Optional[str]:
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
