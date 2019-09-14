def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    recur(data)
    # Write your code here.

    return data

def recur(data: dict):
    if type(data) == dict:
        for key,value in data.items():
            if type(value) == dict or type(value) == list:
                recur(data[key])
            else:
                data[key] = properChange(value)
    elif type(data) == list:
        for valuein in range(len(data)):
            if type(data[valuein]) == dict or type(data[valuein]) == list:
                recur(data[valuein])
            else:
                data[valuein] = properChange(data[valuein])

def properChange(inp):
    if inp in ["true", "True"]:
        return True
    elif inp in ["false", "False"]:
        return False
    elif str.isdigit(inp):
        return int(inp)
    else:
        return inp