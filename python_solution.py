

def refine_parameters(data):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    # Write your code here.

    #We will iterate over the keys in the given json
    for key in data:
    	try:
    		clean_dict[key] = int(data[key])
    	except:
    		if type(data[key]) == dict:
    			# Recursive case if there is another dictionary within the answer
    			print(data[str(key)])
    			clean_dict[key] = refine_parameters(data[str(key)])

    		elif type(data[key]) == list or type(data[key]) == tuple:
    			#  Case if there is an array, we need to refine all the parameters
    			clean_dict[key] = []
    			for item in data[key]:
    				try:
    					clean_dict[key].append(int(item))
    				except:
    					clean_dict[key].append(item)
    		elif data[key] == 'false':
    			clean_dict[key] = False
    		elif data[key] == 'true':
    			clean_dict[key] = True
    		else:
    			clean_dict[key] = data[key]

    return clean_dict
