
def convert_to_datatype(data: str):
    if data == "true":
        return True
    elif data == "false":
        return False
    elif type(data) is list: # convert each element if value is an array
        for i, entry in enumerate(data):
            data[i] = convert_to_datatype(entry)
        return data
    else:
        try: # try converting to int
            intdata = int(data)
            return intdata
        except ValueError: # if error, then it was a string
            return data

def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary
    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    for entry in data:
        if type(data[entry]) is dict: # recurse if value is a dictionary
            clean_dict[entry] = refine_parameters(data[entry])
        else: # otherwise do a single conversion using convert_to_datatype
            clean_dict[entry] = convert_to_datatype(data[entry])
                
    return clean_dict
