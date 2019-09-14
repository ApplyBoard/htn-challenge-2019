const json = require('./tests/challenge.json');

const refineParameters = (data) => {
  if (typeof data === 'object') {
    Object.entries(data).forEach(([k, v]) => data[k] = refineParameters(v));
  } else if (Array.isArray(data)) {
    return data.map(refineParameters);
  } else if (data === 'true') {
    return true;
  } else if (data === 'false') {
    return false;
  } else if (/^\d+$/.test(data)) {
    return parseInt(data);
  }

  return data;
}

module.exports = refineParameters;
