def convert(data):
    for x in data:
        if type(data[x]) is dict:
            convert(data[x])
        elif type(data[x]) is str:
            if data[x] == "true":
                data[x] = True;
            elif data[x] == "false":
                data[x] = False;
            elif data[x].isdigit():
                data[x] = int(data[x])
        else:
            for i in range(len(data[x])):
                if data[x][i].isdigit():
                    data[x][i] = int(data[x][i])
        


def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    # Write your code here.
    convert(data)
    clean_dict = data
    return clean_dict
