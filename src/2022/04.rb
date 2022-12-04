d = ARGF
  .read
  .lines
  .map { |line| line.strip.gsub("-", "..").split(",").map { |r| eval(r) } }

  p d.count { |a, b| a.cover?(b) or b.cover?(a) }
  p d.count { |a, b| (a.to_a & b.to_a).size > 0 }