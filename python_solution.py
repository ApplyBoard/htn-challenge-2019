# Nancy Zhao


def clean_value(val: str):
    '''Clean the string value of a key in the dictionary

    Returns:
        Return the value in the proper data type
    '''
    if val == "true":
        return True
    elif val == "false":
        return False
    elif "." in val:
        try:
            return float(val)
        except ValueError:
            pass
    else:
        try:
            return int(val)
        except ValueError:
            return val


def clean_list(l: list):
    '''Clean the list value of a key in the dictionary recursively

    Returns:
        Return the list with values in proper data type
    '''
    new_list = []
    for item in l:
        if isinstance(item, list):
            new_item = clean_list(item)
        else:
            new_item = clean_value(item)
        new_list.append(new_item)
    return new_list


def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    for key in data:
        if isinstance(data[key], dict):
            # recursively clean dict values
            clean_dict[key] = refine_parameters(data[key])
        elif isinstance(data[key], list):
            # recursively clean list values
            clean_dict[key] = clean_list(data[key])
        else:
            clean_dict[key] = clean_value(data[key])

    return clean_dict
