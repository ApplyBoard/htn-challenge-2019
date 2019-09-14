const json = require('./tests/challenge.json');


function is_number(val) {
  return val.match("(\d+(\.\d+)?)");
}

function parse_object(data) {
  if (Array.isArray(data)) {
    for (let i = 0; i < data.length; i++) {
      if (is_number(data[i])) {
        data[i] = parseFloat(data[i]);
      }
    }
    return data;

  } else if (typeof data === 'string') {
    if (is_number(data)) {
      return parseFloat(data);
    } else if (data === 'true') {
      data = true;
    } else if (data === 'false') {
      data = false;
    }
    return data;
  } else {
    let keys = Object.keys(data);
    for (let key of keys) {
      data[key] = parse_object(data[key])
    }
  }
  return data;
}

const refineParameters = data => {
  // Write your code here.
  // Remember to call this function to return the formatted json
  // with the json imported at the top of this file

  // Run this file with `node javascript_solution.js` in your CLI to verify your answer

  return parse_object(data)
}




// Comment out the line below to console.log and call your function to debug
// console.log('formattedJson: ', refineParameters(json));

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters;

console.log(refineParameters(json))
