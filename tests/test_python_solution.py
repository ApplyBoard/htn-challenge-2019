import json
from python_solution import refine_parameters


def test_refine_parameters():
    challenge = {}
    expected_dict = {}

    with open('tests/challenge.json', 'rb') as challenge_json:
        challenge = json.load(challenge_json)

    with open('tests/complete.json', 'rb') as complete_json:
        expected_dict = json.load(complete_json)

    processed_dict = refine_parameters(data=challenge)

    assert processed_dict == expected_dict
