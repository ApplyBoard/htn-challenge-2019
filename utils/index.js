
const parseBool = (value) => (
    value == "false" ? false : true;
);

const parseArrayOfString = (dataArray) => {
    return dataArray.map((data) => (String(data)));
};

const parseArrayOfInt = (dataArray) => {
    return dataArray.map((data) => (parseInt(data)));
};

const parseArrayOfDates = (dataArray) => {
    return dataArray.map((data) => (Date.parse(data)));
};

module.exports = {
    parseBool,
    parseArrayOfString,
    parseArrayOfInt,
    parseArrayOfDates
};
