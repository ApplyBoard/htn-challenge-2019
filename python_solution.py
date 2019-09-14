
def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = data   # Copy

    # Write your code here.
    for key in clean_dict:

        entry = clean_dict[key]

        # If item is string
        if type(entry) == str:
            if entry.isdigit():
                clean_dict[key] = int(entry)
            # Boolean
            elif entry == "true":   
                clean_dict[key] = True
            elif entry == "false":
                clean_dict[key] = False
        
        # If item is list
        elif type(entry) == list:
            if type(entry[0]) == str and entry[0].isdigit():
                # Convert strings to numbers in list
                for i, item in enumerate(entry):
                    clean_dict[key][i] = int(clean_dict[key][i])

        # If item is dict
        elif type(entry) == dict:
            refine_parameters(entry)
        

    return clean_dict
