const json = require('./tests/challenge.json');



const isCharInt = (character) => {
    return character >= '0' && character <= '9';
}

const isWordNum = (word) => {
  let dotFound = false;
  for(let i=0; i<word.length; i++){
    if(!isCharInt(word[i])){
      if(!dotFound && word[i] === "."){
        dotFound = true;
      } else if (!(i === 0 && word[i] === "-" && word.length !== 1)) {
        return false;
      }
    }
  }
  return true;
}

const evaluateString = (s) => {
  if(s === null || s === undefined){
    return s;
  } else if(s === true || s === "true"){
    return true;
  } else if(s === false || s === "false"){
    return false;
  } else if(isWordNum(s)){
    return parseFloat(s);
  } else {
    return s;
  }
}


const refineParameters = data => {
  const keys = Object.keys(data);
  keys.forEach((key) => {
    const item = data[key];
    if(Array.isArray(item)){
      for (let i=0; i<item.length; i++){
        if(typeof item[i] === 'object'){
          refineParameters(item[i]);
        } else {
          item[i] = evaluateString(item[i]);
        }
      }
    } else if(typeof item === 'object') {
      refineParameters(item);
    } else {
      data[key] = evaluateString(item);
    }
  })
  return data;
}

// Comment out the line below to console.log and call your function to debug
console.log('formattedJson: ', refineParameters(json));

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters;
