const json = require('./tests/challenge.json');

function convertToType(item) {
  if (isNaN(item)) {
    if (item.toUpperCase() === 'TRUE' || item.toUpperCase() === 'FALSE') {
      return (item.toUpperCase() === 'TRUE')
    } else {
      return item
    }
  } else if (item === "undefined") {
    return undefined
  } else if (item === "null") {
    return null
  } else if (Array.isArray(item)){
    return item.forEach(convertToType(item))
  } else if (typeof(item) === 'object'){
    return refineParameters(item)
  } else {
    return Number(item)
  }
}

const refineParameters = data => {
  let ar = Object.entries(data)
  ar.forEach((pair)=>{
    if (typeof(pair[1]) === 'object') {
      data[pair[0]] = refineParameters(pair[1])
    } else {
      data[pair[0]] = convertToType(pair[1])
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
module.exports = refineParameters;
