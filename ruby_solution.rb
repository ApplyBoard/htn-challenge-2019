require "json"

def refineParameters(input)
  if input.class == Hash
    input.each { |key, value| input[key] = refineParameters(value) }
  elsif input.class == Array
    input.map { |v| refineParameters(v) }
  elsif input == 'true'
    true
  elsif input == 'false'
    false
  else
    Integer(input)
  end
rescue ArgumentError
  input
end
