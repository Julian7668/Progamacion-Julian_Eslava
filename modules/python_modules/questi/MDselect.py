from typing import Any, Callable, Dict, Optional, Sequence, Union, cast

import questionary
from prompt_toolkit.styles import Style
from questionary.constants import DEFAULT_QUESTION_PREFIX, DEFAULT_SELECTED_POINTER
from questionary.prompts.common import Choice

from questi.MDtext import questi_decorator


@questi_decorator
def select(
    message: str,
    choices: Sequence[Union[str, Choice, Dict[str, Any]]],
    default: Optional[Union[str, Choice, Dict[str, Any]]] = None,
    qmark: str = DEFAULT_QUESTION_PREFIX,
    pointer: Optional[str] = DEFAULT_SELECTED_POINTER,
    style: Optional[Style] = None,
    use_shortcuts: bool = False,
    use_arrow_keys: bool = True,
    use_indicator: bool = False,
    use_jk_keys: bool = True,
    use_emacs_keys: bool = True,
    use_search_filter: bool = False,
    show_selected: bool = False,
    show_description: bool = True,
    instruction: Optional[str] = None,
    exit_callback: Optional[Callable[[], Any]] = None,
    **kwargs: Any,
) -> Optional[str]:
    return questionary.select(
        message,
        choices,
        default,
        qmark,
        pointer,
        style,
        use_shortcuts,
        use_arrow_keys,
        use_indicator,
        use_jk_keys,
        use_emacs_keys,
        use_search_filter,
        show_selected,
        show_description,
        instruction,
        **kwargs,
    ).ask()


if __name__ == "__main__":
    import questi

    # * ejemplo sin exit_callback
    resultado = cast(
        str,
        questi.select(
            "Escoje el numero de tu animal favorito:", ("1.Pollito", "2.¡Chanchi!")
        ),
    )
    if int(resultado[0]) == 1:
        pass

    # * ejemplo con exit_callback
    from utils import flip_coin

    resultado = cast(
        Union[str, Callable[[], str]],
        questi.select(
            "Escoje tu animal favorito:",
            ("Pollito", "¡Chanchi!"),
            exit_callback=flip_coin,
        ),
    )
    print(resultado if isinstance(resultado, str) else resultado())
