datastream = ARGF.read.chomp.chars

def find_marker stream, distinct
  stream
    .each_cons(distinct)
    .find_index { |ary| ary
      .uniq
      .size == distinct } + distinct
end


part_1 = find_marker(datastream, 4)
part_2 = find_marker(datastream, 14)

puts part_1
puts part_2
