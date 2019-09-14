const json = require('./tests/challenge.json');

/**
 * 
 * Why reinvent the wheel?
 * JSON.stringify() provides a replacer as the second argument, 
 * which iterates recursively over key-value pairs. In the case 
 * that the value is meant to be boolean or a number, we replace 
 * it with the corresponding value. Otherwise, return the value as-is.
 * Further reading: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify
 * 
 * @param {string} _ The key of the json key value pair to transform
 * @param {*} value The value to be converted into the appropriate datatype.
 * @returns The transformed value.
 */
function _replacer(_, value) {
  if (value === "true") return true;
  if (value === "false") return false;
  if (!isNaN(value)) return Number(value);
  return value;
}

/**
 * Goes through a JSON object, turning each string into its appropriate datatype.
 * 
 * @param {Object} data The parameter object to be refined.
 * @returns The clean JSON object.
 */
const refineParameters = data => {
  return JSON.parse(JSON.stringify(data, _replacer))
}


// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters;
