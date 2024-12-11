SEGMENTS = ARGF.read.lines.map { _1.scan(/\d+/).map &:to_i }

def points s
  x1, y1, x2, y2 = s

  dx = x2 <=> x1
  dy = y2 <=> y1

  if dx == 0
    y1.step(y2, dy).map { [x1, _1] }
  elsif dy == 0
    x1.step(x2, dx).map { [_1, y1] }
  else
    x1.step(x2, dx).zip(y1.step(y2, dy))
  end
end

def count_overlapping_points segments
  segments.flat_map { |s| points(s) }.tally.values.count { _1 > 1 }
end


part_1 = count_overlapping_points SEGMENTS.select { |x1, y1, x2, y2| x1 == x2 or y1 == y2 }
part_2 = count_overlapping_points SEGMENTS

puts part_1
puts part_2
