
def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    # Write your code here.
    clean_dict = worker(data)

    print(clean_dict)

    return clean_dict


def worker(data):
    return {k: worker(v) for k, v in data.items()} if isinstance(data, dict) else cleaner(data)


def cleaner(v):
    # if list
    if type(v) == list:
        return [cleaner(x) for x in v]
    if v.isdigit():
        return int(v)
    if v.lower() == 'true':
        return True
    if v.lower() == 'false':
        return False
    return v
