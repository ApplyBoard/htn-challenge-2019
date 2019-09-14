# Nancy Zhao

def clean_value(val: str):
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


def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    # Write your code here.
    for key in data:
        if isinstance(data[key], dict):
            clean_dict[key] = refine_parameters(data[key])
        elif isinstance(data[key], list):
            clean_dict[key] = []
            for item in data[key]:
                item = clean_value(item)
                clean_dict[key].append(item)
        else:
            clean_dict[key] = clean_value(data[key])
    return clean_dict
