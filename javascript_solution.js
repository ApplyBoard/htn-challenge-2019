const json = require('./tests/challenge.json');

function isBool(value) {
  var b = value === 'true' ? true :
    value === 'false' ? false :
      value;
  return b
}

function isInt(value) {
  return !isNaN(value) && (function (x) { return (x | 0) === x; })(parseFloat(value))
}

function isArray(value) {
  for (v in value) {
    if (isInt(v)) {
      v = Number(v)
    }
  }
}

var results = []

const refineParameters = data => {
  // Write your code here.
  // Remember to call this function to return the formatted json
  // with the json imported at the top of this file
  Object.keys(data).forEach(key => {
    if (isInt(data[key])) {
      data[key] = Number(data[key])
    }
    if (Array.isArray(data[key])) {
      isArray(data[key])
    }
    if (typeof data[key] === 'string') {
      data[key] = isBool(data[key])
    }
    if (typeof data[key] === 'object') {
      refineParameters(data[key])
    }
  })
  results.push(data)
  return results[results.length - 1]
  // Run this file with `node javascript_solution.js` in your CLI to verify your answer
}

// Comment out the line below to console.log and call your function to debug
console.log('formattedJson: ', refineParameters(json));

// ----- Do not modify anything below this line (needed for test suite) ------
// module.exports = refineParameters;
