d = ARGF.read.lines.map { _1.split }.map { |c, u| [c.to_sym, u.to_i] }

h, v = 0, 0

d.each {
  case _1
  when :forward
    v += _2
  when :down
    h += _2
  when :up
    h -= _2
  end
}

part_1 = h * v

puts part_1

h, v, a = 0, 0, 0

d.each {
  case _1
  when :forward
    h += _2
    v += _2 * a
  when :down
    a += _2
  when :up
    a -= _2
  end
}

part_2 = h * v

puts part_2
