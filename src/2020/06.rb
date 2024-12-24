groups = File.open("../../data/2020/06.txt").read.split("\n\n").map &:split

part_1 = groups.sum { |g| g.join.chars.uniq.size }

puts part_1

part_2 = groups.sum { |g| g.map(&:chars).inject(:&).size }

puts part_2
