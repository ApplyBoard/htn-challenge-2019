
def is_boolean(string):
    ''' Return wheter a string is a number
    Returns:
        Whether a string is a number or not
    '''
    return string == "true" or string == "false"

def convert_boolean_string(string):
    ''' Converts a string to its' boolean representation
    Returns:
        The string as its' boolean representation
    '''
    if is_boolean:
        return string == "true"
    else:
        raise ValueError

def is_number(string):
    ''' Return wheter a string is a number
    Returns:
        Whether a string is a number or not
    '''
    try:
        int(string)
    except ValueError: 
        return False
    return True

def convert_string(string):
    ''' Converts a string to its' datatype representation if applicable
    Returns:
        A string as it's datatype representation if applicable
    '''
    if is_boolean(string):
        return convert_boolean_string(string)
    elif is_number(string):
        return int(string)
    else:
        return string

def refine_parameters(data):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    for key in data:
        new_value = data[key]

        if type(new_value) == dict:
            new_value = refine_parameters(new_value)
        elif type(new_value) == list:
            for i in range(len(new_value)):
                new_value[i] = convert_string(new_value[i])
        else:
            new_value = convert_string(new_value)
    
        clean_dict[key] = new_value

    return clean_dict
