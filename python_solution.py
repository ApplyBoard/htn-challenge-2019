
def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    #recursively refine every item in a list
    def refine_list(givenList : list):
        refined_list = []
        for unrefined_item in givenList:
            if type(unrefined_item) == dict:
                refined_list.append(refine_parameters(unrefined_item))
            elif type(unrefined_item) == list:
                refined_list.append(refine_list(unrefined_item))
            else:
                refined_list.append(refine_item(unrefined_item))
        return refined_list

        
    #refines non-list and non-dictionaries
    def refine_item(unrefined_item):
        refined_item = 0
        try:
            refined_item = int(unrefined_item)
        except ValueError:
            if unrefined_item.lower() == "true":
                refined_item = True
            elif unrefined_item.lower() == "false":
                refined_item = False
            else:
                refined_item = unrefined_item
        return refined_item

    clean_dict = {}

    #Recursively refine every item in a dictionary
    for item in data:
        if type(data[item]) == dict:
            clean_dict[item] = refine_parameters(data[item])
        elif type(data[item]) == list:
            clean_dict[item] = refine_list(data[item])
        else:
            clean_dict[item] = refine_item(data[item])
        


    return clean_dict
