def process(data):
    if isinstance(data, dict):
        clean_dict = {}
        for key, value in data.items():
            clean_dict[key] = process(value)
        return clean_dict
    if isinstance(data, list):
        new_data = [process(datum) for datum in data]
        return new_data
    if isinstance(data, str):
        if data.isdigit():
            return int(data)
        elif data == "false":
            return False
        elif data == "true":
            return True
        else:
            return data
    else:
        return data


def refine_parameters(data: dict):
    """Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    """
    print(data)
    print(process(data))
    return process(data)
