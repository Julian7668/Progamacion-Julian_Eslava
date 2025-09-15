def validate_type(x: str, target_type: type, strict: bool = False) -> bool:
    if target_type is str:
        return True
    if target_type is bool:
        return x.capitalize() in ("T", "True", "F", "False")
    x = x.strip().lstrip("+-")

    if target_type is int:
        return x.isdigit()
    return ("." in x or not strict) and x.replace(".", "", 1).isdigit()
