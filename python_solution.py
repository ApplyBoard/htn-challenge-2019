
def refine_parameters(data: dict):
	'''Refine the parameters of a dictionary

	Returns:
		Return a dictionary of cleaned input
	'''
	clean_dict = {}
	
	conv_bool = {"has_ca_study_permit": "bool", "has_us_study_permit": "bool", "only_direct": "bool", "grade": "int", "grade_scale": "int", "grading_scheme": "int", "student_id": "int", "student_information_id": "int", "deadline": "string", "nationality": "string", "sort_by": "string", "studied_level": "string", "countries":"arr_string", "provinces":"arr_string"}
	conv_array_int = ["school_ids", "school_types"]
	
	conv_dict = ["eng_test", "intakes", "personal_information"]
	
	
	for item, type in conv_bool.items():
		if(type=="bool"):
			clean_dict[item] =bool(data[item])
		elif(type=="int"):
			clean_dict[item] =int(data[item])
		elif(type=="string"):
			clean_dict[item] = data[item]
		elif(type=="arr_string"):
			clean_dict[item] = data[item]
		elif(type=="arr_string"):
			a = 0;
			for subitem in clean_dict[item]:
				clean_dict[item][a] = int(subitem)
				a = a +1

	# Write your code here.
	#print(data)

	return clean_dict
