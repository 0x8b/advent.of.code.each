area = ARGF.read.chomp.scan(/-?\d+/).map(&:to_i)

TARGETX = Range.new(*area.shift(2))
TARGETY = Range.new(*area.shift(2))

X, Y = 0, 0

def test vx, vy
  x, y, max_y = 0, 0, 0

  until TARGETX.include?(x) and TARGETY.include?(y)
    return if x > TARGETX.end or y < TARGETY.begin

    x += vx
    y += vy
    vx = [0, vx - 1].max
    vy -= 1
    max_y = [max_y, y].max
  end

  return max_y
end

max_y = 0
total = 0

(0..TARGETX.end).to_a.product((TARGETY.begin..1000).to_a).each do |vx, vy|
  candidate = test(vx, vy)

  if candidate
    total += 1
    max_y = [candidate, max_y].max if candidate > max_y
  end
end

puts max_y # part 1
puts total # part 2
