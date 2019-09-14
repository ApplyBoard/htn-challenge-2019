
def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    for key, value in data.items():
        clean_dict[key] = convert(value)

    return clean_dict

def convert(value):
    new_value = value
    if isinstance(value, list):
        new_value = []
        for nested_value in value:
            new_value.append(convert(nested_value))
    elif isinstance(value, dict):
        new_value = {}
        for nested_key, nested_value in value.items():
            new_value[nested_key] = convert(nested_value)
    else:
        new_value = type_cast(value)
    return new_value

def type_cast(value: str):
    if value.lower() == 'true':
        return True
    if value.lower() == 'false':
        return False
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value
