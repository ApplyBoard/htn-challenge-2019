
def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    # Check element types
    # print(set([type(x) for x in data.values()]))

    clean_dict = {}

    # Write your code here.

    for k, v in data.items():
        clean_dict[k] = convert_type(v)

    return clean_dict


def convert_type(src: object) -> object:
    # Composite types
    if type(src) is dict:
        result = src.copy()
        for k, v in result.items():
            result[k] = convert_type(v)
        return result
    elif type(src) is list:
        result = [convert_type(x) for x in src]
        return result
    # Elementary types
    if src.lower() in ["true", "false"]:
        return bool(src.lower() == "true")
    elif all([48 <= ord(x) <= 57 for x in src]):
        return int(src)
    else:
        return src
