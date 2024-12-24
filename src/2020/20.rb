TILES = File.open("../../data/2020/20.txt").read.split("\n\n").map do |tile_metadata|
  tile_id, *tile = tile_metadata.lines.map &:strip

  [tile_id[5..].to_i, tile.map(&:chars)]
end.to_h

W = H = 12

def change_orientation tile, mode
  case mode
  when 0
    return tile
  when 1
    return tile.transpose.map(&:reverse)
  when 2
    return tile.reverse.map(&:reverse)
  when 3
    return tile.map(&:reverse).transpose
  when 4
    return tile.transpose
  when 5
    return tile.transpose.transpose.map(&:reverse)
  when 6
    return tile.transpose.reverse.map(&:reverse)
  when 7
    return tile.transpose.map(&:reverse).transpose
  end
end

def edge tile, side
  case side
  when :top
    tile.first.join
  when :bottom
    tile.last.join
  when :left
    tile.map(&:first).join
  when :right
    tile.map(&:last).join
  end
end

root_id = TILES.keys.first
root = [root_id, 0, [:top, :right, :bottom, :left].map { |side| edge(TILES[root_id], side) }]

sides = TILES.keys.reject { |id| id == root_id }.flat_map do |id|
  (0..7).map do |mode|
    o = change_orientation(TILES[id], mode)
    [id, mode, [:top, :right, :bottom, :left].map {|side| edge(o, side)}]
  end
end

sides << root
queue = [root]
processed = []

graph = Hash.new do |hash, key|
  hash[key] = {
    top: [],
    bottom: [],
    left: [],
    right: [],
  }
end

reversed = {
  top: :bottom,
  bottom: :top,
  left: :right,
  right: :left,
}

def side sides, dir
  sides[[:top, :right, :bottom, :left].index(dir)]
end

while queue.size > 0
  tile_id, tile_mode, tile_sides = queue.shift

  for dir in [:top, :bottom, :left, :right]
    graph[tile_id][dir] = sides.reject do |id, _, _|
      id == tile_id
    end.select do |i, m, s|
      side(tile_sides, dir) == side(s, reversed[dir])
    end

    for i, m, s in graph[tile_id][dir]
      unless processed.include? i
        queue << [i, m, s]
      end

      processed << i
    end
  end

  processed << tile_id
end

part_1 = graph.select { |k, v| [v[:top], v[:bottom], v[:left], v[:right]].map(&:size).count(0) == 2 }.keys.inject(:*)

puts part_1

top_left_id, _ = graph.find do |k,v|
  v[:left].empty? && v[:top].empty?
end

mapa_1 = Array.new(H) { |r| Array.new(W) { |c| 0 } }

queue = [
  [top_left_id, 0, 0, 0]
]

while queue.size > 0 do
  id, mode, r, c = queue.shift

  mapa_1[r][c] = change_orientation(TILES[id], mode)

  right  = graph[id][:right].first
  bottom = graph[id][:bottom].first

  if bottom
    queue << [graph[id][:bottom].first[0], graph[id][:bottom].first[1], r + 1, c]
  end

  if right
    queue << [graph[id][:right].first[0], graph[id][:right].first[1], r, c + 1]
  end
end

mapa_2 = Array.new(H * 8) { |r| Array.new(W * 8) { |c| 0 } }

H.times do |rr|
  W.times do |cc|
    8.times do |r|
      8.times do |c|
        mapa_2[rr * 8 + r][cc * 8 + c] = mapa_1[rr][cc][r + 1][c + 1]
      end
    end
  end
end

sea_monster = [
  "                  # ",
  "#    ##    ##    ###",
  " #  #  #  #  #  #   ",
].map &:chars

monster_points = []

sea_monster.size.times do |r|
  sea_monster.first.size.times do |c|
    if sea_monster[r][c] == ?#
      monster_points << [r, c]
    end
  end
end

for mode in 0..7
  transformed_map = change_orientation(mapa_2, mode)

  points_to_remove = []

  for r in (0..(mapa_2.size - sea_monster.size + 1))
    for c in (0..(mapa_2.first.size - sea_monster.first.size + 1))
      points = monster_points.map { |rr, cc| [r + rr, c + cc] }

      if points.all? { |y,x| transformed_map[y][x] == ?# }
        points_to_remove.push *points
      end
    end
  end

  points_to_remove.each do |r, c|
    transformed_map[r][c] = " "
  end

  if points_to_remove.size > 0
    part_2 = transformed_map.flatten.count ?#

    puts part_2
  end
end
