
def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}
    
    # Write your code here.
    def check(var):
        if type(var) == str:
            if var.lower() in ("true","false"):
                return  bool(var.lower()=="true")
            elif var.isnumeric():
                return int(var)
            else:
                return var
        elif type(var) == dict:
            return  refine_parameters(var)
        elif type(var) == list:
            return  [check(j) for j in var]

    for i in data.keys():
        clean_dict[i] = check(data[i])
            
            
    return clean_dict


