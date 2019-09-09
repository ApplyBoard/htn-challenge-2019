const refineParameters = require('../javascript_solution');
const challenge_json = require('./challenge.json');
const complete_json = require('./complete.json');

test('test if the function converts the challenge json to the complete json', () => {
  expect(refineParameters(challenge_json)).toEqual(complete_json);
});
