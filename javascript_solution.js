const json = require('./tests/challenge.json');

const refineParameters = data => {
  var JSONstring = String(JSON.stringify(data));

  var newJSONstring = JSONstring.replace(/\"true\"/g, "true").replace(/\"false\"/g, "false");
  console.log(newJSONstring)
  const regex = new RegExp("\"[0-9]+\"");
  var num;
  var arr = [];

  while(num = regex.exec(newJSONstring)){
    console.log(num);
    console.log(num[0]);
    newJSONstring = newJSONstring.replace(/\"[0-9]+\"/, parseInt(num[0].replace(/\"/g, "")));
  }
  console.log(arr);
  return JSON.parse(newJSONstring);
  // Write your code here.
  // Remember to call this function to return the formatted json
  // with the json imported at the top of this file

  // Run this file with `node javascript_solution.js` in your CLI to verify your answer
}

// Comment out the line below to console.log and call your function to debug
console.log('formattedJson: ', refineParameters(json));

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters;
