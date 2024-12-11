dots, axes = ARGF.read.split "\n\n"

dots = dots.lines.map { |line| line.chomp.split(?,).map &:to_i }

sheet = dots.zip([true].cycle).to_h

axes = axes.lines.map do |line|
  axis, v = line.chomp.split.last.split ?=
  [axis, v.to_i]
end

first = true

axes.each do |axis, v|
  sheet.transform_keys! do |k|
    if axis == ?x and k[0] > v
      [v - (k[0] - v), k[1]]
    elsif axis == ?y and k[1] > v
      [k[0], v - (k[1] - v)]
    else
      k
    end
  end

  puts sheet.keys.size if first # part_1, part_2

  first = false
end

mx, my = sheet.keys.transpose.map &:max

(0..my).each do |y|
  (0..mx).each do |x|
    print (sheet[[x,y]] ? '@' : ' ')
  end
  puts
end
