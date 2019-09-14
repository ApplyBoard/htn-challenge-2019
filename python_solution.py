# Refines each element
# Returns cleaned inputs


def refine_element(element):
    # Checks if value could be boolean
    try:
        return {'true': True, 'false': False}[element]
    except (KeyError, TypeError):
        pass

    # Checks if the data type is an integer
    try:
        if element.isdigit():
            # if so, return the element as an integer
            return int(element)
    except AttributeError:
        pass

    # Checks if the data type is a dictionary
    if type(element) == dict:
        # If so, loop through the dictionary
        for i in element.keys():
            element[i] = refine_element(element[i])  # Recurse dictionary
        return element

    # Checks if the data type is a list
    if type(element) == list:

        # If so, it loops throught the list
        for idx, i in enumerate(element):
            element[idx] = refine_element(i)  # Recurse through list
        return element
    return element

# Refines the parameters of a dictionary
# Returns a dictionary of cleaned input


def refine_parameters(data: dict):

    # Creates an empty dictionary called clean_dict
    clean_dict = {}

    # Loop through each of the items in the dictionary
    for i in data.keys():  # i = keys
        clean_dict[i] = refine_element(data[i])
    return clean_dict
