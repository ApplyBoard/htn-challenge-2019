def boole(x):
    if x == "false":
        return False
    return True

def identity(x):
    return x

def eng_test(x):
    return {"value": x["value"],
            "r": int(x["r"]),
            "l": int(x["l"]),
            "s": int(x["s"]),
            "w": int(x["w"])}

def intakes(x):
    return {
      "subValue": boole(x["subValue"]),
      "value": x["value"]
    }
transformers = {
    "personal_information": identity,
    "grade": int,
    "grade_scale": int,
    "grading_scheme": int,
    "has_ca_study_permit": boole,
    "has_us_study_permit": boole,
    "nationality": identity,
    "only_direct": boole,
    "sort_by": identity,
    "student_id": int,
    "student_information_id": int,
    "studied_level": identity,
    "eng_test": eng_test, 
    "countries": identity,
    "school_ids": lambda x: [int(n) for n in x],
    "school_types": lambda x: [int(n) for n in x],
    "provinces": identity,
    "deadline": identity,
    "intakes": intakes
}

import json

def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    for k, v in data.items():
        clean_dict[k] = transformers[k](v)

    # Write your code here.

    return clean_dict
