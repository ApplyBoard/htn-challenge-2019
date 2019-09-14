def convert_item(item):
    if item == 'false':
        return False
    elif item == 'true':
        return True
    try:
        return int(item)
    except:
        try:
            return float(item)
        except:
            return item

def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    if type(data) != dict:
        return convert_item(data)

    clean_dict = {}

    # Write your code here.
    for k, v in data.items():
        if type(v) == dict:
            clean_dict[k] = refine_parameters(v)
        elif type(v) == list:
            clean_dict[k] = [refine_parameters(i) for i in v]
        else:
            clean_dict[k] = convert_item(v)

    return clean_dict
