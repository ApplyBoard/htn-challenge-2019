
def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    # Write your code here.

    for n in data:
        if type(data[n]) == list:
            for m in range(len(data[n])):
                if data[n][m].isnumeric():
                    data[n][m] = int(data[n][m])
                elif data[n][m] == "true":
                    data[n][m] = True
                elif data[n][m] == "false":
                    data[n][m] = False
        elif type(data[n]) == dict:
            data[n] = refine_parameters(data[n])
        elif data[n].isnumeric():
            data[n] = int(data[n])
        elif data[n] == "true":
            data[n] = True
        elif data[n] == "false":
            data[n] = False


    clean_dict = data #just incase I was not allowed to touch the return clean_dict
    return clean_dict
