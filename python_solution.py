
def refine_val(x):
    return int(x) if x.isnumeric() else True if x == "true" else False if x == "false" else x
def refine_parameters(data):
    clean_dict = {}
    for key, value in data.iteritems():
        if type(value) == dict:
            clean_dict[key] = refine_parameters(value)
        elif type(value) == list:
            clean_dict[key] = [refine_val(x) for x in value] 
        else:
            clean_dict[key] = refine_val(value)

    return clean_dict
