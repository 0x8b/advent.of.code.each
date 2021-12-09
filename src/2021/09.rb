MAP = ARGF.read.lines.map do |line|
  line.chomp.chars.map &:to_i
end

H, W = MAP.size, MAP[0].size

def adj y, x
  [[0, 1], [1, 0], [0, -1], [-1, 0]].map { |dy, dx|
    [y + dy, x + dx]
  }.select { |ny, nx|
    (0...H) === ny and (0...W) === nx
  }
end

LOW_POINTS = []
risk_level = 0

[*0...H].product([*0...W]).each { |y, x|
  is_low_point = adj(y, x).all? { |ny, nx|
    MAP[y][x] < MAP[ny][nx]
  }

  if is_low_point
    risk_level += MAP[y][x] + 1
    LOW_POINTS << [y, x]
  end
}

p risk_level

def expand_basin basin
  basin.concat(basin.flat_map { |y, x|
    adj(y, x).select { |ny, nx|
      MAP[ny][nx] != 9 and MAP[ny][nx] >= MAP[y][x]
    }
  }).uniq
end

p LOW_POINTS.map { |ly, lx|
  basin = [[ly, lx]]

  10.times { # 10 was chosen arbitrarily
    basin = expand_basin basin
  }

  basin.size
}.max(3).reduce(:*)
