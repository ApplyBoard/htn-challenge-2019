def clean(data):
	if (isinstance(data, list)):
		for ind in range(len(data)):
			try:
				data[ind] = int(data[ind])
			except:
				if (str(data[ind]).lower() in ['false', 'true']):
					data[ind] = [False, True][str(data[ind]).lower()=='true']
				else:
					data[ind] = clean(data[ind])
		return data
	if not (isinstance(data, dict)):
		return data
	res = {}
	for key in data:
		try:
			data[key] = int(data[key])
		except:
			if (str(data[key]).lower() in ['false', 'true']):
				data[key] = [False, True][str(data[key]).lower()=='true']
			else:
				data[key] = clean(data[key])
		res[key] = data[key]
	return res


def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    clean_dict = clean(data)

    return clean_dict
   