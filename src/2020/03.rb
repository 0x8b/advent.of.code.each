map = File.open("../../data/2020/03.txt").read.strip.split

def count_trees map, dx, dy
  (0...map.size).step(dy).count do |y|
    x = ((y / dy) * dx) % map.first.size

    map[y][x] == "#"
  end
end

part_1 = count_trees(map, 3, 1)

puts part_1

part_2 = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]].map do |dx, dy|
  count_trees map, dx, dy
end.inject(:*)

puts part_2
