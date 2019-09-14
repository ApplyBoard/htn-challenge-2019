const json = require('./tests/challenge.json');

const isBoolean = (string) => string.toLowerCase() === 'true' || string.toLowerCase() === 'false';
const isNumber = (string) => /^-?[0-9]+(\.[0-9]+)?$/.test(string);
const isArray = (object) => Array.isArray(object);
const isObject = (object) => typeof(object) === 'object';
const isNull = (string) => string.toLowerCase() === "null";

const parseBoolean = (b) => b === 'true';

const refineParameters = data => {
  // Write your code here.
  // Remember to call this function to return the formatted json
  // with the json imported at the top of this file

  // Run this file with `node javascript_solution.js` in your CLI to verify your answer
  if (typeof(data) == "string" && isBoolean(data)) {
    return parseBoolean(data);
  } else if (typeof(data) == "string" && isNull(data)) {
    return null;
  } else if (typeof(data) == "string" && isNumber(data)) {
    return parseFloat(data);
  } else if (isArray(data)) {
    return data.map(v => refineParameters(v));
  } else if (isObject(data)) {
    for (const key in data) {
      data[key] = refineParameters(data[key]);
    }
  }

  return data;
}

// Comment out the line below to console.log and call your function to debug
// console.log('formattedJson: ', refineParameters(json));

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters;
