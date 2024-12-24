DIRS = {
  se: [0, -1, 1],
  sw: [-1, 0, 1],
  nw: [0, 1, -1],
  ne: [1, 0, -1],
  e: [1, -1, 0],
  w: [-1, 1, 0],
}

PATHS = File.open("../../data/2020/24.txt").each_line.map { |path| path.scan(/se|sw|nw|ne|e|w/).map &:to_sym }

GRID = Hash.new { |hash, key| hash[key] = :white }

def get_coords reference_tile=[0, 0, 0], dirs
  x, y, z = reference_tile

  dirs.each do |dir|
    x += DIRS[dir][0]
    y += DIRS[dir][1]
    z += DIRS[dir][2]
  end

  [x, y, z]
end

PATHS.map { |path| get_coords path }.each { |coords| GRID[coords] = GRID[coords] == :white ? :black : :white }

part_1 = GRID.values.count(:black)

puts part_1


100.times do |day|
  coords = GRID.keys.flat_map do |c|
    [c] + DIRS.keys.map do |d|
      get_coords(c, [d])
    end
  end.uniq

  bc = coords.map do |c|
    DIRS.keys.map do |dir|
      GRID[get_coords(c, [dir])]
    end.count :black
  end

  to_white = coords.each_with_index.filter { |c, i| GRID[c] == :black && bc[i] != 1 && bc[i] != 2 }.map &:first
  to_black = coords.each_with_index.filter { |c, i| GRID[c] == :white && bc[i] == 2 }.map &:first

  to_white.each { |c| GRID[c] = :white }
  to_black.each { |c| GRID[c] = :black }

  part_2 = "Day #{day + 1}: #{GRID.values.count :black}"

  puts part_2
end
