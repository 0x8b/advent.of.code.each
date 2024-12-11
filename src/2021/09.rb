MAP = ARGF.read.lines.map { _1.chomp.chars.map &:to_i }.transpose

def adjacent x, y
  [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]].select { |x, y|
    x in 0...100 and y in 0...100
  }
end

LOW_POINTS = [*0...100].to_a.product([*0...100]).filter_map { |x, y|
  [x, y] if adjacent(x, y).all? { |ax, ay| MAP[x][y] < MAP[ax][ay] }
}

part_1 = LOW_POINTS.sum { |x, y| MAP[x][y] + 1 }

puts part_1

def expand_basin basin
  10.times { # 10 was chosen arbitrarily
    basin = basin.concat(basin.flat_map { |x, y|
      adjacent(x, y).select { |ax, ay|
        MAP[ax][ay] != 9 and MAP[ax][ay] >= MAP[x][y]
      }
    }).uniq
  }

  basin
end

part_2 = LOW_POINTS.map { |x, y| expand_basin [[x, y]] }.map(&:size).max(3).reduce(:*)

puts part_2
