def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    for key in data:
        value = data[key]
        clean_dict[key] = converter(value)

    return clean_dict


def converter(value):
    """
    Converts the value to the wanted format
    """
    int_dict = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    # If list
    if type(value) is list:
        new_array = [converter(element) for element in value]
        return new_array

    # If dict
    if type(value) is dict:
        return refine_parameters(value)

    # If number
    counter = 0
    is_num = True
    if type(value) is str:
        while counter < len(value) and is_num:

            if value[counter] in int_dict and counter == len(value) - 1:
                return int(value)
            elif value[counter] not in int_dict:
                is_num = False

            counter += 1

        if value == "false":
            return False

        if value == "true":
            return True

    return value


print(refine_parameters({"countries": ["Canada", "USA"]}))
print(refine_parameters(challenge))
