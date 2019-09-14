
def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    for key, value in dict.items():
        if str(int(dict[x])) == dict[x]:
            clean_dict[x] = int(dict[x])
        elif dict[x] == "True":
            clean_dict[x] = True
        elif dict[x] == "False":
            clean_dict[x] = False
        elif isinstance(dict[x], list):
            refine_parameters(dict[x])
        elif isinstance(dict[x], dict):
            refine_parameters(dict[x])
        else:
            clean_dict[x] = dict[x]

    return clean_dict
