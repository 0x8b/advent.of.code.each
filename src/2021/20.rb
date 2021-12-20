ALGORITHM, *INITIAL = ARGF.read.gsub("\n\n", "\n").lines.map do |line|
  line.chomp.chars.map { |c| c == "#" ? 1 : 0 }
end

IMAGE = {}
IMAGE.default = 0

IS_ALTERNATING = ALGORITHM.first == 1

INITIAL.size.times { |y|
  INITIAL.first.size.times { |x|
    IMAGE[[x, y]] = INITIAL[y][x]
  }
}

ADJACENT = [
  [-1, -1], [0, -1], [1, -1],
  [-1,  0], [0,  0], [1,  0],
  [-1,  1], [0,  1], [1,  1],
]

def adjacent x, y
  ADJACENT.map { |dx, dy| [x + dx, y + dy] }
end

def index hash, x, y
  adjacent(x, y).map(&hash).join.to_i(2)
end

[2, 50].each do |n|
  parent = IMAGE.clone

  n.times do
    minx, maxx, miny, maxy = parent.keys.transpose.map(&:minmax).flatten

    child = [*(minx - 1)..(maxx + 1)].product([*(miny - 1)..(maxy + 1)]).map { |x, y|
      [[x, y], ALGORITHM[index(parent, x, y)]]
    }.to_h

    if IS_ALTERNATING
      child.default = parent.default == 1 ? 0 : 1
    else
      child.default = 0
    end

    parent = child
  end

  puts parent.values.count(1) # part one and two
end
