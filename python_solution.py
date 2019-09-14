
def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}
    
    # Write your code here.
    def check(var):
        if type(var) == str:
            if var.lower() in ("true","false"):
                return  bool(var.lower()=="true")
            elif var.isnumeric():
                return int(var)
            else:
                return var
        elif type(var) == dict:
            return  refine_parameters(var)
        elif type(var) == list:
            return  [check(j) for j in var]

    for i in data.keys():
        clean_dict[i] = check(data[i])
            
            
    return clean_dict

jsonobj = {
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

# print(refine_parameters(jsonobj))