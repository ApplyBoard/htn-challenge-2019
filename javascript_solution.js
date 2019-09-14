const json = require('./tests/challenge.json');

// Converts parameters from strings to the correct type
function convertData(str){
  if(str === "true") return true;
  if(str === "false") return false;
  if(Number(str)) return Number(str);

  return str;
}

const refineParameters = data => {
  var refinedData = {};

  // Iterate over properties to refine
  for(var prop in data){
    // Recurse on objects or arrays
    if(typeof data[prop] ===  "object"){
      refinedData[prop] = refineParameters(data[prop]);
    }else{
      refinedData[prop] = convertData(data[prop]);
    }
  }

  return refinedData;
}

// Comment out the line below to console.log and call your function to debug
 console.log('formattedJson: ', refineParameters(json));

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters;
