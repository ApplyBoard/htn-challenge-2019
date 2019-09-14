const json = require('./tests/challenge.json');

const Utils = require('./utils');

const parseIntakes = (data) => ({
    "subValue": Utils.parseBool(data.subValue),
    "value": Utils.parseBool(data.value),
});

const testEngTest = () => ({
    "value": Utils.
})



const refineParameters = {
    "grade": parseInt,
    "grade_scale": parseInt,
    "grading_scheme": parseInt,
    "has_ca_study_permit": Utils.parseBool,
    "has_us_study_permit": Utils.parseBool,
    "only_direct": Utils.parseBool,
    "sort_by": String,
    "student_id": parseInt,
    "student_information_id": parseInt,
    "studied_level": String,
    "eng_test": testEngText
    "countries": Utils.parseArrayOfString,
    "school_ids": Utils.parseArrayOfInt,
    "school_types":  Utils.parseArrayOfInt,
    "provinces":  Utils.parseArrayOfString,
    "deadline": Date.parse,
    "intakes": parseIntakes
}

// Comment out the line below to console.log and call your function to debug
// console.log('formattedJson: ', refineParameters(json));
console.log(Utils.isOnlyString("12345"));
// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters;
