def numberify(item):
    if type(item) is dict:
        ret = {}
        for key in item.keys():
            ret[key] = numberify(item[key])
        return ret
    elif type(item) is list:
        ret = []
        for item in item:
            ret.append(numberify(item))
        return ret
    elif type(item) is str:
        if item == "true":
            return True
        elif item == "false":
            return False
        elif item.isdigit():
            return int(item)
        return item


def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''

    clean_dict = numberify(data)

    return clean_dict
