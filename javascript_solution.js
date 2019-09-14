const json = require('./tests/challenge.json');

const refineParameters = data => {
    //console.log(data);
    //Go through all json data
    for (var key in data) {
        if (data[key] === "false") {
            data[key] = false;
            //Boolean checks, true -> 1, false -> 0
        } else if (data[key] === "true") {
            data[key] = true;
            //Number conversions
        } else if (!isNaN(data[key])) {
            data[key] = Number(data[key]);
            //Recursively go through all values within arrays and nested objects
        } else if (Array.isArray(data[key])) {
            refineParameters(data[key]);
        } else if (typeof data[key] === 'object') {
            refineParameters(data[key]);
        }

    }
    return data;
}

// Comment out the line below to console.log and call your function to debug
//console.log('formattedJson: ', refineParameters(json));

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = refineParameters;
