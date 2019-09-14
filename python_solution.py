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


test = {
    "personal_information": {
        "first_name": "Hack",
        "last_name": "North"
    },
    "grade": "90",
    "grade_scale": "100",
    "grading_scheme": "0",
    "has_ca_study_permit": "true",
    "has_us_study_permit": "true",
    "nationality": "NP",
    "only_direct": "false",
    "sort_by": "relevance",
    "student_id": "7419",
    "student_information_id": "29990",
    "studied_level": "grade_1",
    "eng_test": {
      "value": "toefl",
      "r": "9",
      "l": "9",
      "s": "9",
      "w": "9"
    },
    "countries": ["Canada", "USA"],
    "school_ids": ["2", "500", "1"],
    "school_types": ["1", "2", "3", "4"],
    "provinces": ["Ontario", "British Columbia"],
    "deadline": "2019-07-31",
    "intakes": {
      "subValue": "false",
      "value": ["2018-12-01", "2019-01-01", "2019-02-01", "2019-03-01", "2019-04-01", "2019-07-01"]
    }
}

print (refine_parameters(test))