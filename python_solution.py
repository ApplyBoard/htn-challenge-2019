def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    for key, value in data.items():
        if type(value) is dict:
            clean_dict[key] = refine_parameters(value)
        elif type(value) is list:
            try:
                clean_dict[key] = [int(val) for val in value]
            except:
                clean_dict[key] = value
        else:
            if value == "true" or value == "false":
                clean_dict[key] = value == "true"
            else:
                try:
                    clean_dict[key] = int(value)
                except:
                    clean_dict[key] = value

    return clean_dict
