import json


def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}
    for key, data in data.items():
        if isinstance(data, dict):
            clean_dict[key] = refine_parameters(data)
            continue

        if isinstance(data, list):
            sub_clean = []
            for x in data:
                sub_data = refine_parameters({'fill': x})
                sub_clean.append(sub_data['fill'])
            clean_dict[key] = sub_clean
            continue
            

        if data == 'false':
            clean_dict[key] = False
            continue
        if data == 'true':
            clean_dict[key] = True
            continue
        try:
            clean_dict[key] = int(data)
            continue
        except:
            pass

        clean_dict[key] = data

    return clean_dict
'''
a = refine_parameters({
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
})
b = {
  "countries": [
    "Canada",
    "USA"
  ],
  "deadline": "2019-07-31",
  "eng_test": {
    "l": 9,
    "r": 9,
    "s": 9,
    "value": "toefl",
    "w": 9
  },
  "grade": 90,
  "grade_scale": 100,
  "grading_scheme": 0,
  "has_ca_study_permit": True,
  "has_us_study_permit": True,
  "intakes": {
    "subValue": False,
    "value": [
      "2018-12-01",
      "2019-01-01",
      "2019-02-01",
      "2019-03-01",
      "2019-04-01",
      "2019-07-01"
    ]
  },
  "nationality": "NP",
  "only_direct": False,
  "personal_information": {
    "first_name": "Hack",
    "last_name": "North"
  },
  "provinces": [
    "Ontario",
    "British Columbia"
  ],
  "school_ids": [
    2,
    500,
    1
  ],
  "school_types": [
    1,
    2,
    3,
    4
  ],
  "sort_by": "relevance",
  "student_id": 7419,
  "student_information_id": 29990,
  "studied_level": "grade_1"
}
print(a == b)
'''
