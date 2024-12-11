d = ARGF.read.lines.map &:to_i

part_1 = d.each_cons(2).count { |a, *, b| a < b }
part_2 = d.each_cons(4).count { |a, *, b| a < b }

puts part_1
puts part_2
