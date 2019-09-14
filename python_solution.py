
def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    # Write your code here.
    clean_dict = convert_to_dict(data)


    return clean_dict


def convert():
    


def convert_to_dict(in_data):
    for idx in in_data.keys():
	in_data[idx] = convert(in_data[idx])

    return in_data
