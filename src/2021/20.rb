ALGORITHM, *IMAGE = ARGF.read.gsub("\n\n", "\n").lines.map do |line|
  line.chomp.chars.map { |c| c == "#" ? 1 : 0 }
end

H = {}
H.default = 0

IMAGE.size.times { |y|
  IMAGE.first.size.times { |x|
    H[[x, y]] = IMAGE[y][x]
  }
}

ADJ = [
  [-1, -1], [0, -1], [1, -1],
  [-1,  0], [0,  0], [1,  0],
  [-1,  1], [0,  1], [1,  1],
]

def adjacent x, y
  ADJ.map { |dx, dy| [x + dx, y + dy] }
end

def index hash, x, y
  adjacent(x, y).map(&hash).join.to_i(2)
end

[2, 50].each do |n|
  parent = H.clone

  n.times do
    minx, maxx, miny, maxy = parent.keys.transpose.map(&:minmax).flatten

    child = [*(minx - 1)..(maxx + 1)].product([*(miny - 1)..(maxy + 1)]).map { |x, y|
      [[x, y], ALGORITHM[index(parent, x, y)]]
    }.to_h

    child.default = parent.default == 1 ? 0 : 1

    parent = child
  end

  puts parent.values.count(1) # part one and two
end
