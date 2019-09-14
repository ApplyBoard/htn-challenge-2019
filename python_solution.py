# from pprint import pprint

def fixType(s):
    try:
        return int(s)
    except Exception:
        try:
            return float(s)
        except Exception:
            if s.lower() == 'true':
                return True
            elif s.lower() == 'false':
                return False
            else:
                return s

def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    # Write your code here.
    for i in data:
        if isinstance(data[i], dict):
            clean_dict[i] = refine_parameters(data[i])
        elif isinstance(data[i], list):
            clean_dict[i] = [fixType(s) for s in data[i]]
        else:
            clean_dict[i] = fixType(data[i])
        
    return clean_dict

# test_dict = {
#     "personal_information": {
#         "first_name": "Hack",
#         "last_name": "North"
#     },
#     "grade": "90",
#     "grade_scale": "100",
#     "grading_scheme": "0",
#     "has_ca_study_permit": "true",
#     "has_us_study_permit": "true",
#     "nationality": "NP",
#     "only_direct": "false",
#     "sort_by": "relevance",
#     "student_id": "7419",
#     "student_information_id": "29990",
#     "studied_level": "grade_1",
#     "eng_test": {
#       "value": "toefl",
#       "r": "9",
#       "l": "9",
#       "s": "9",
#       "w": "9"
#     },
#     "countries": ["Canada", "USA"],
#     "school_ids": ["2", "500", "1"],
#     "school_types": ["1", "2", "3", "4"],
#     "provinces": ["Ontario", "British Columbia"],
#     "deadline": "2019-07-31",
#     "intakes": {
#       "subValue": "false",
#       "value": ["2018-12-01", "2019-01-01", "2019-02-01", "2019-03-01", "2019-04-01", "2019-07-01"]
#     }
# }

# pprint(refine_parameters(test_dict))