const json = require('./tests/challenge.json');

const refineParameters = data => {
  // Write your code here.
  // Remember to call this function to return the formatted json
  // with the json imported at the top of this file

  // Run this file with `node javascript_solution.js` in your CLI to verify your answer

  // Recursively iterate through every single possible key of the object
  Object.keys(data).forEach( (key) => {
    if(typeof data[key] === 'object'){
      return refineParameters(data[key])
    }
    data[key] = parseData(data[key])
  })
  return json
}

const parseData = (data) => {
  let newData
  try{
    // JSON.parse() can format either numbers or booleans
    // If it fails, it means that the data should be a string
    newData = JSON.parse(data)
  } catch(error) {
    newData = data
  }
  return newData
}
// Comment out the line below to console.log and call your function to debug
console.log('formattedJson: ', refineParameters(json));

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters;
