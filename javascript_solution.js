const json = require('./tests/challenge.json');

const refineParameters = data => {
  const keys = Object.keys(data)
  for(let key of keys) {
    let entry = data[key]

    //booleans
    if ((entry==='true')||(entry==='false')) {
      data[key] = entry==='true' ? true : false
    }
    //integer
    else if (!/\D/.test(entry)){
      data[key] = parseInt(entry,10)
    }
    else if (entry instanceof Array){
      refineParametersArray(entry)
    }
    else if (entry instanceof Object){
      refineParameters(entry)
    }


  }
  return data

  // Run this file with `node javascript_solution.js` in your CLI to verify your answer
}

const refineParametersArray = data => {

  for(let i=0;i<data.length;i++) {
    let key = data[i]
        //booleans
      if ((key==='true')||(key==='false')) {
        data[i] = key==='true' ? true : false
      }
      //integer
      else if (!/\D/.test(key)){
        data[i] = parseInt(key,10)
      }
  }
}

// Comment out the line below to console.log and call your function to debug
// console.log('formattedJson: ', refineParameters(json));
refineParameters(json)

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters;
