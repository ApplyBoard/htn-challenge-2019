def convert(string: str):
    # check for bools
    if string == 'true':
        return True
    if string == 'false':
        return False
    
    # check for ints and strings
    try:
        number = int(string)
        if str(number) == string:
            return number
        else:
            return string
    except (TypeError, ValueError) as e:
        return string
    
def refine_parameters(data: dict):
    
    clean_dict = {}

    for key, val in data.items():
        # if we encounter a dictionary - refine that
        if type(val) == dict:
            clean_dict[key] = refine_parameters(val)
            continue

        # if we encounter a list - convert each element
        if type(val) == list:
            clean_dict[key] = list(map(convert, val))
            continue

        # if we encounter anything else - convert that
        clean_dict[key] = convert(val)

    return clean_dict
