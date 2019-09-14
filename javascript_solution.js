const json = require('./tests/challenge.json')

const refineParameters = data => {
  const numArrays = [
    'grade',
    'grade_scale',
    'grading_scheme',
    'student_id',
    'student_information_id',
  ]
  const numNested = ['school_ids', 'school_types']
  const boolArr = ['has_ca_study_permit', 'has_us_study_permit', 'only_direct']
  const boolObj = {
    id: 'intakes',
    fields: ['subValue'],
  }
  const numObj = {
    id: 'eng_test',
    fields: ['l', 'r', 's', 'w'],
  }

  const keys = Object.keys(data)
  keys.forEach(key => {
    if (numArrays.includes(key)) {
      data[key] = parseInt(data[key])
    }
    if (numNested.includes(key)) {
      data[key] = data[key].map(i => parseInt(i))
    }
    if (boolArr.includes(key)) {
      data[key] = data[key] === 'true'
    }
    if (numObj.id == key) {
      numObj.fields.forEach(i => {
        data[key][i] = parseInt(data[key][i])
      })
    }
    if (boolObj.id == key) {
      boolObj.fields.forEach(i => {
        data[key][i] = data[key][i] === 'true'
      })
    }
  })
  return data

  // Write your code here.
  // Remember to call this function to return the formatted json
  // with the json imported at the top of this file

  // Run this file with `node javascript_solution.js` in your CLI to verify your answer
}

// Comment out the line below to console.log and call your function to debug
// console.log('formattedJson: ', refineParameters(json));

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters
