MAP = ARGF.read.lines.map { _1.chomp.chars.map &:to_i }.transpose

X, Y = MAP.first.size, MAP.size

def adjacent x, y
  [[0, 1], [1, 0], [0, -1], [-1, 0]].map { |dx, dy|
    [x + dx, y + dy]
  }.select { |ax, ay|
    (0...X) === ax and (0...Y) === ay
  }
end

LOW_POINTS = [*0...X].product([*0...Y]).filter_map { |x, y|
  [x, y] if adjacent(x, y).all? { |ax, ay| MAP[x][y] < MAP[ax][ay] }
}

p LOW_POINTS.sum { |x, y| MAP[x][y] + 1 } # part 1

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

p LOW_POINTS.map { |x, y| expand_basin [[x, y]] }.map(&:size).max(3).reduce(:*) # part 2
