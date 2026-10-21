def validate_str(value, arg):
    if not isinstance(value, str):
        raise TypeError(f"{arg} must be string")
    elif value.strip() == "":
        raise ValueError(f"{arg} cannot be empty")
