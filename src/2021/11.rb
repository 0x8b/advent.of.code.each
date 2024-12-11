octopuses = ARGF.read.lines.map { _1.chomp.chars.map &:to_i }

ADJACENT_DIRS = [-1, 0, 1].repeated_permutation(2).to_a - [[0, 0]]

def adjacents x, y
  ADJACENT_DIRS.filter_map do |dx, dy|
    [x + dx, y + dy] if x + dx in 0...10 and y + dy in 0...10
  end
end

def find_energetic octopuses
  [*0..9].product([*0..9]).select do |x, y|
    octopuses[x][y] > 9
  end
end

def flash octopuses, x, y
  return if octopuses[x][y] == :flash
  return if octopuses[x][y] <= 9

  octopuses[x][y] = :flash

  to_visit = []

  adjacents(x, y).each do |x, y|
    if octopuses[x][y] != :flash
      octopuses[x][y] += 1
      to_visit << [x, y]
    end
  end

  to_visit.uniq.each do |x, y|
    flash octopuses, x, y
  end
end

def step octopuses
  octopuses = octopuses.map do |row|
    row.map do |energy_level|
      energy_level + 1
    end
  end

  find_energetic(octopuses).each do |x, y|
    flash octopuses, x, y
  end

  octopuses.map do |row|
    row.map do |o|
      if o == :flash
        0
      else
        o
      end
    end
  end
end

flashes = 0

(1..).each do |i|
  octopuses = step octopuses.map &:dup
  flashes += octopuses.flatten.count &:zero?

  part_1 = flashes if i == 100
  puts part_1

  if octopuses.flatten.all? { _1.zero? }
    part_2 = i
    puts part_2
    break
  end
end
