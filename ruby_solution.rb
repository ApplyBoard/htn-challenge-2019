require "json"

def refineParameters input
  # If you want to use the input file before running the tests, uncomment the following line
  # input = JSON.parse(File.read(File.join(File.dirname(File.absolute_path(__FILE__)), 'tests/challenge.json')))
  
  output = parseHash(input)

  # Write your code here.
  return output
end

def parseHash(hash)
  hash.each do |k, v|
    if(v.is_a?(Hash))
      hash[k] = parseHash(v)
    elsif(v.is_a?(Array))
      v = v.map do |subValue|
        convertType(subValue)
      end

      hash[k] = v
    else
      hash[k] = convertType(v)
    end
  end

  hash
end

def convertType(value)
  if( value.casecmp("true") == 0)
    true
  elsif ( value.casecmp("false") == 0)
    false
  elsif ((value.to_i != 0 || value == "0") && !value.include?("-"))
    # to_i returns 0 if it can't parse the string. Checking for - means
    # dates don't get automatically converted
    value.to_i
  else
    value
  end
end
