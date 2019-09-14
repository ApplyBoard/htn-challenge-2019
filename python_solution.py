
def refine_parameters(data):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}
    # print(data)
    for key in data:
        if isinstance(data[key], dict):
            clean_dict[key] = refine_parameters(data[key])
        elif type(data[key]) == list:
            new_list = []
            for element in data[key]:
                new_list.append(check_type(element))
            clean_dict[key] = new_list
        else:
            element = data[key]
            clean_dict[key] = check_type(element)
    print(clean_dict)
    return clean_dict


def check_type(data):
    if is_num(data):
        return int(data)
    elif data == "true":
        return True
    elif data == "false":
        return False
    else:
        return data

def is_num(s):
    return all(i.isdigit() for i in s)


# def 

#     eng_test
#     grade
#     grade_scale
#     grading_scheme

    # Write your code here.

    # return clean_dict
