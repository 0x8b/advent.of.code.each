d = ARGF.read.lines.map &:to_i

[2, 4].each {
  p d.each_cons(_1).count { |a, *, b| a < b }
}
