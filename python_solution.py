def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''


    '''Helper function to recursively parse an object of unknown type
    Supports dist, list, and str'''
    def numberify(item):
        # Parse dictionaries
        if type(item) is dict:
            ret = {}
            for key in item.keys():
                ret[key] = numberify(item[key])  # Recurse
            return ret

        # Parse lists
        elif type(item) is list:
            ret = []
            for value in item:
                ret.append(numberify(value))  # Recurse
            return ret

        # Parse strings
        elif type(item) is str:
            # Handle booleans
            if item.lower() == "true":
                return True
            elif item.lower() == "false":
                return False

            # Handle integer values
            elif item.isdigit():
                return int(item)

            # No conversion, return string
            return item


    clean_dict = numberify(data)
    return clean_dict
