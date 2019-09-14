
def convert_to_datatype(data: str):
    if data == "true":
        return True
    elif data == "false":
        return False
    elif type(data) is list:
        for i, entry in enumerate(data):
            data[i] = convert_to_datatype(entry)
        return data
    else:
        try:
            intdata = int(data)
            return intdata
        except ValueError:
            # just a string
            return data

def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary
    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    for entry in data:
        if type(data[entry]) is dict:
            clean_dict[entry] = refine_parameters(data[entry])
        else:
            clean_dict[entry] = convert_to_datatype(data[entry])

                
    return clean_dict
