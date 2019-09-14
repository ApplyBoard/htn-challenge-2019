# File:  tc_simple_number.rb

require_relative "../ruby_solution"
require "test/unit"
require "json"

class TestRefineParameters < Test::Unit::TestCase

  # test if the function converts the challenge json to the complete json
  def test_simple
    solution = JSON.parse(File.read('tests/complete.json'))
    input = JSON.parse(File.read('tests/challenge.json'))
    assert_equal(refineParameters(input), solution)
  end

  def test_null
    solution = JSON.parse(File.read('tests/completeWithNullValues.json'))
    input = JSON.parse(File.read('tests/challengeWithNullValues.json'))
    assert_equal(refineParameters(input), solution)
  end

  def test_floats
    solution = JSON.parse(File.read('tests/completeWithFloatValues.json'))
    input = JSON.parse(File.read('tests/challengeWithFloatValues.json'))
    assert_equal(refineParameters(input), solution)
  end
end
