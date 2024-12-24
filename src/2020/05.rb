ids = File.open("../../data/2020/05.txt").read.lines.map { |bsp| bsp.strip.tr("FBLR", "0101").to_i 2 }

part_1 = ids.max

puts part_1

part_2 = (ids.min..ids.max).to_a - ids

puts part_2
