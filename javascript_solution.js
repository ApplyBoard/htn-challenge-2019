const json = require('./tests/challenge.json')

const numRegEx = /^[0-9]*$/

const checkKeys = obj => {
  const keys = Object.keys(obj)
  keys.forEach(key => {
    if (typeof obj[key] === 'object') obj[key] = checkKeys(obj[key])
    else if (Array.isArray(obj[key])) obj[key] = checkArr(obj[key])
    else if (obj[key] === 'true' || obj[key] === 'false') {
      obj[key] = obj[key] === 'true'
    } else if (numRegEx.test(obj[key])) {
      obj[key] = parseFloat(obj[key])
    }
  })
  return obj
}

const checkArr = arr =>
  arr.map(item => {
    if (typeof item === 'object') item = checkKeys(item)
    else if (item === 'true') return item === 'true'
    else if (numRegEx.test(item)) return parseFloat(item)
    else return item
  })

const refineParameters = data => {
  return typeof data === 'object' ? checkKeys(data) : checkArr(data)

  // Write your code here.
  // Remember to call this function to return the formatted json
  // with the json imported at the top of this file

  // Run this file with `node javascript_solution.js` in your CLI to verify your answer
}
// Comment out the line below to console.log and call your function to debug
// console.log('formattedJson: ', refineParameters(json));

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters
