
def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    # Write your code here.
    for d in data:
        if type(data[d]) == dict:
            clean_dict[d] = refine_parameters(data[d])
        elif type(data[d]) == list:
            refined = []
            for c in data[d]:
                if c.isnumeric():
                    refined.append(int(c))
                elif c == "true":
                    refined.append(True)
                elif c == "false":
                    refined.append(False)
                else:
                    refined.append(c)
            clean_dict[d] = refined
        else:
            if data[d].isnumeric():
                clean_dict[d] = int(data[d])
            elif data[d] == "true":
                clean_dict[d] =(True)
            elif data[d] == "false":
                clean_dict[d] =(False)
            else:
                clean_dict[d] = (data[d])


    return clean_dict
