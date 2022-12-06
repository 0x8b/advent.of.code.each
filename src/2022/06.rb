datastream = ARGF.read.chomp.chars

def find_marker stream, distinct
  stream
    .each_cons(distinct)
    .find_index { |ary| ary
      .uniq
      .size == distinct } + distinct
end


puts find_marker(datastream, 4)
puts find_marker(datastream, 14)
