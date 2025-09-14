from typing import Any, Callable, NoReturn, Optional, Union, ParamSpec
from functools import wraps
import questionary
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.styles import Style
from questionary.constants import DEFAULT_QUESTION_PREFIX

from utils import finalized


P = ParamSpec("P")
type_of_exit_callback = Callable[[], Any]


def questi_decorator(
    func: Callable[P, Optional[Union[str, bool]]],
) -> Callable[P, Any]:
    @wraps(func)
    def wrapper(
        *args: P.args, **kwargs: P.kwargs
    ) -> Union[Union[str, bool], Union[NoReturn, type_of_exit_callback]]:
        return (
            result
            if (result := func(*args, **kwargs)) is not None
            else (
                finalized()
                if not (exit_callback := kwargs.get("exit_callback"))
                else exit_callback
            )
        )  # type: ignore

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
    print(
        int(
            questi.text(
                "Ingresa un entero entre el -10 y el 10:",
                validate=lambda x: (  # type: ignore
                    V.validate_type(x, int)  # type: ignore
                    and V.validate_range_num(int(x), ((-10, False), (10, False)))  # type: ignore
                ),
            )
        )
    )

    # * ejemplo con exit_callback
    from utils import flip_coin

    print(
        float(resultado)
        if isinstance(
            resultado := questi.text(
                "Ingresa un flotante del 0 al 10:",
                validate=lambda x: (  # type: ignore
                    V.validate_type(x, float)  # type: ignore
                    and V.validate_range_num(float(x), (0, 10))  # type: ignore
                ),
                exit_callback=flip_coin,
            ),
            str,
        )
        else resultado()
    )
