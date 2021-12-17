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

xs = (0..TARGETX.end)
ys = (TARGETY.begin..150) # might be higher than 150 for other input

ppm = []

ys.each do |vy|
  ppm << []
  xs.each do |vx|
    candidate = test(vx, vy)

    if candidate
      total += 1
      max_y = [candidate, max_y].max if candidate > max_y
    end

    ppm.last << if candidate
      [255, 0, 0]
    elsif vx == 0
      [0, 255, 0]
    elsif vy < 0
      [0, 0, 128]
    elsif vy == 0
      [255, 0, 255]
    else
      [0, 0, 255]
    end
  end

  ppm << ppm.pop.flatten.join(" ")
end

if ENV["PREVIEW"] == "true"
  File.write "preview.ppm", ["P3", "#{xs.size} #{ys.size}", "255", ppm.reverse].join("\n")
end

puts max_y # part 1
puts total # part 2
