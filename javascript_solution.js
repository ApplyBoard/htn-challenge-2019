const json = require('./tests/challenge.json');

const checkNum = (item) => !isNaN(item)
const convertNum = (item) => Number(item)
const checkBool = (item) => item.toUpperCase() === 'TRUE' || item.toUpperCase() === 'FALSE'
const convertBool = (item) => (item.toUpperCase() === 'TRUE')
const checkUndef = (item) => item === "undefined"
const convertUndef = (item) => undefined
const checkNull = (item) => item === "null"
const convertNull = (item) => null
const checkAr = (item) => Array.isArray(item)
const convertAr = (item) => item.forEach(convertToType(item))
const checkObj = (item) => typeof(item) === 'object'
const convertObj = (item) => refineParameters(item)
const checkSci1 = (item) => item.match(/[0-9]+(\.[0-9]+)?x10\^[0-9]+/)
const convertSci1 = (item) => {numAr = item.toUpperCase().split("X10^"); return numAr[0] * Math.pow(10,numAr[1])}
const checkSci2 = (item) => item.match(/[0-9]+(\.[0-9]+)?e[0-9]+/)
const convertSci2 = (item) => {numAr = item.toUpperCase().split("X10^"); return numAr[0] * Math.pow(10,numAr[1])}

function convertToType(item) {
  if (checkNum(item)) {
    return convertNum(item)
  } else if (checkBool(item)) {
    return convertBool(item)
  } else if (checkUndef(item)) {
    return convertUndef(item)
  } else if (checkNull(item)) {
    return convertNull(item)
  } else if (checkAr(item)) {
    return convertAr(item)
  } else if (checkObj(item)) {
    return convertObj(item)
  } else if (checkSci1(item)) {
    return convertSci1(item)
  } else if (checkSci2(item)) {
    return convertSci2(item)
  } else {
    return item
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
