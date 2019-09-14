import json

def refine_parameters_dict(input_dict):
    for k, v in input_dict.items():
        if isinstance(v, dict):
            input_dict[k] = refine_parameters_dict(v)
        elif isinstance(v, list):
            input_dict[k] = refine_parameters_list(v)
        else:
            input_dict[k] = visit(v)
    return input_dict


def refine_parameters_list(input_lst):
    for i, elem in enumerate(input_lst):
        if isinstance(elem, dict):
            input_lst[i] = refine_parameters_dict(elem)
        elif isinstance(elem, list):
            input_lst[i] = refine_parameters_list(elem)
        else:
            input_lst[i] = visit(elem)
            
    return input_lst

def visit(val):
    try:
        return int(val)
    except:
        pass
    try:
        return float(val)
    except:
        pass
    try: 
        return bool(val)
    except:
        pass

    return val

if __name__ == '__main__':
    with open('tests/challenge.json', 'r') as fi:
        input_dict = json.load(fi)
    print(json.dumps(refine_parameters_dict(input_dict), indent=2))