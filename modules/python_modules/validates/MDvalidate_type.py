def validate_type(x: str, type_objective: type = str, strict: bool = False) -> bool:
    return type_objective is str or (
        x.capitalize() in ("T", "True", "F", "False")
        if type_objective is bool
        else (
            x.strip().lstrip("+-").isdigit()
            if type_objective is int
            else (
                x.strip().lstrip("+-").replace(".", "", 1).isdigit()
                if "." in x or not strict
                else False
            )
        )
    )


print(validate_type("10", type))
