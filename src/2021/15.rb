require 'pqueue'
require 'set'

GRID = ARGF.read.lines.map { |line| line.chomp.chars.map(&:to_i) }

def neighbours grid, position
  x, y = position

  yield [x + 1, y] if x + 1 < grid[0].size
  yield [x - 1, y] if x > 0
  yield [x, y + 1] if y + 1 < grid.size
  yield [x, y - 1] if y > 0
end


def lowest_total_risk grid
  start = [0, 0]
  target = [grid[0].size - 1, grid.size - 1]

  seen = Set.new
  queue = PQueue.new([[start, 0]]) do |a, b|
    a.last < b.last
  end

  until queue.empty?
    position, risk = queue.pop

    if seen.include? position
      next
    else
      seen << position
    end

    return risk if position == target

    neighbours(grid, position) do |x, y|
      queue << [[x, y], risk + grid[y][x]]
    end
  end
end

BIGGRID = []

5.times do |ny|
  GRID.size.times do |y|
    BIGGRID << []
    5.times do |nx|
      GRID[0].size.times do |x|
        value = GRID[y][x] + nx + ny
        value -= 9 while value > 9
        BIGGRID.last << value
      end
    end
  end
end

part_1 = lowest_total_risk(GRID)
part_2 = lowest_total_risk(BIGGRID)

puts part_1
puts part_2
