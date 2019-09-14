def refine_parameters(data_input: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    def convert (val):
        # converts value to appropriate datatype
        try:
            return int (val)
        except:
            if val.upper () == "TRUE" or val.upper() == "FALSE":
                return bool (val)
            else:
                return val

    def iter_list (entry):
        # returns clean list
        entry_list = []
        for j in entry:
            entry_list.append (convert(j))
        return entry_list

    for i in data_input:
        entry = test[i]
        for j in entry:
            if type(test [i]) == type(dict()):
                entry_dict = {}
                for j in entry:
                    data = entry [j]
                    if type (data) == type(list()):
                        entry_dict [j] = iter_list (data)
                    else:
                        entry_dict [j] = convert (data)
                clean_dict [i] = entry_dict
            elif type (test [i]) == type(list()):
                clean_dict [i] = iter_list (entry)
            else:
                clean_dict [i] = convert (entry)
    # Write your code here.

    return clean_dict
