const json = require('./tests/challenge.json');

const refineParameters = overallData => {
  let stack = [overallData]; // to avoid recursion, we store nested objects in a stack
  let seen = []; // to handle edge case in which an object is inside itself
  while (stack.length > 0) {
    let data = stack[stack.length - 1];
    stack.pop();
    if (seen.includes(data)) {
      // Avoid recursing infinitely when objects are inside each other
      continue;
    }
    seen.push(data);
    let keys = Object.keys(data);
    for (let keyNum = 0; keyNum < keys.length; keyNum++) {
      let key = keys[keyNum];
      if (typeof data[key] === 'string') {
        // First, we try converting to various keyword values
        if (data[key] === 'true') {
          data[key] = true;
        } else if (data[key] === 'false') {
          data[key] = false;
        } else if (data[key] === 'null') {
          data[key] = null;
        } else if (data[key] === 'undefined') {
          data[key] = undefined;
        } else {
          // Try to convert it to a Number
          let convertedToNumber = Number(data[key]);
          if (!isNaN(convertedToNumber)) {
            // If it isn't NaN, it's converted successfully and we should replace it
            data[key] = convertedToNumber;
          } // If the Number representation is NaN, it's a regular string
        }
      } else if (typeof data[key] === 'object') {
        // We convert this object as well by adding it to the stack
        stack.push(data[key]);
      }
    }
  }
  return overallData;
}

// Comment out the line below to console.log and call your function to debug
// console.log('formattedJson: ', refineParameters(json));

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters;
