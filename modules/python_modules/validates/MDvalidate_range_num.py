from typing import Union


def validate_range_num(
    number: Union[float, int],
    validation_range: tuple[
        Union[float, tuple[float, bool]], Union[float, tuple[float, bool]]
    ] = (float("-inf"), float("inf")),
) -> bool:
    return (
        number >= validation_range[0]
        if not isinstance(validation_range[0], tuple)
        else (
            number >= validation_range[0][0]
            if validation_range[0][1]
            else number > validation_range[0][0]
        )
    ) and (
        number <= validation_range[1]
        if not isinstance(validation_range[1], tuple)
        else (
            number <= validation_range[1][0]
            if validation_range[1][1]
            else number < validation_range[1][0]
        )
    )
