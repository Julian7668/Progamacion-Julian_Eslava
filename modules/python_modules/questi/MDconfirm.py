from typing import Any, Callable, Optional
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
    from utils import lanzar_moneda

    print(
        resultado
        if isinstance(
            resultado := questi.confirm(
                "¿Chanchi?",
                exit_callback=lanzar_moneda,
            ),
            bool,
        )
        else resultado()  # type: ignore
    )
