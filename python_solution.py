def refine_parameter(obj):
    """
    Refine a parameter
    Returns a parameter parsed to its expected type
    """
    if isinstance(obj, dict):
        return refine_parameters(obj)
    elif isinstance(obj, list):
        return [refine_parameter(o) for o in obj]
    else:
        try:
            return int(obj)
        except ValueError:
            if obj in ["true", "false"]:
                return obj == "true"
            return obj


def refine_parameters(data: dict):
    """
    Refine the parameters of a dictionary
    Returns a dictionary of cleaned input
    """
    clean_dict = {}
    for key, value in data.items():
        clean_dict[key] = refine_parameter(value)
    return clean_dict
