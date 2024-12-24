ns = File.open("../../data/2020/01.txt").each_line.map &:to_i

[2, 3].each do |n|
  puts ns.combination(n).find { |c| c.sum == 2020 }.inject(:*) # part_1, part_2
end
