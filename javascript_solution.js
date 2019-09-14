const json = require('./tests/challenge.json');

const parseBoolean = (b) => b === "true";

const refineParameters = data => {
  // Write your code here.
  // Remember to call this function to return the formatted json
  // with the json imported at the top of this file

  // Run this file with `node javascript_solution.js` in your CLI to verify your answer

  data.grade = Number(data.grade);
  data.grade_scale = Number(data.grade_scale);
  data.grading_scheme = Number(data.grading_scheme);
  data.has_ca_study_permit = parseBoolean(data.has_ca_study_permit);
  data.has_us_study_permit = parseBoolean(data.has_us_study_permit);
  data.only_direct = parseBoolean(data.only_direct);
  data.student_id = Number(data.student_id);
  data.student_information_id = Number(data.student_information_id);
  data.eng_test.r = Number(data.eng_test.r);
  data.eng_test.l = Number(data.eng_test.l);
  data.eng_test.s = Number(data.eng_test.s);
  data.eng_test.w = Number(data.eng_test.w);
  data.school_ids = data.school_ids.map(n => Number(n));
  data.school_types = data.school_types.map(n => Number(n));
  data.intakes.subValue = parseBoolean(data.intakes.subValue);

  return data;
}

// Comment out the line below to console.log and call your function to debug
// console.log('formattedJson: ', refineParameters(json));

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters;
