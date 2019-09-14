bool (["false"])

def refine_parameters(data_input: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    def convert (val):
        # converts value to appropriate datatype
        try:
            return int (val)
        except:
            if val.upper () == "TRUE":
                return True
            elif val.upper() == "FALSE":
                return False
            else:
                return val

    def iter_list (entry):
        # returns clean list
        entry_list = []
        for j in entry:
            entry_list.append (convert(j))
        return entry_list

    for i in data_input:
        entry = test[i]
        for j in entry:
            if type(test [i]) == type(dict()):
                entry_dict = {}
                for j in entry:
                    data = entry [j]
                    if type (data) == type(list()):
                        entry_dict [j] = iter_list (data)
                    else:
                        entry_dict [j] = convert (data)
                clean_dict [i] = entry_dict
            elif type (test [i]) == type(list()):
                clean_dict [i] = iter_list (entry)
            else:
                clean_dict [i] = convert (entry)
    # Write your code here.

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


refine_parameters (test)
