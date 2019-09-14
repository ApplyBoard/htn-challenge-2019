require "json"

def refineParameters(input)
  case input
  when Hash
    input.each { |key, value| input[key] = refineParameters(value) }
  when Array
    input.map { |v| refineParameters(v) }
  when 'null'
    nil
  when boolean?
    input == 'true'
  when float?
    input.to_f
  when integer?
    input.to_i
  else
    input
  end
end

def boolean?
  ->(value) { %w(true false).include?(value) }
end

def float?
  ->(value) { !!Float(value) rescue false }
end

def integer?
  ->(value) { !!Integer(value) rescue false }
end
