pairs = ARGF
  .read
  .lines
  .map { |line| line
    .strip
    .gsub('-', '..')
    .split(',')
    .map { |range| eval(range) } }

puts pairs.count { |a, b| a.cover?(b) or b.cover?(a) }
puts pairs.count { |a, b| (a.to_a & b.to_a).size > 0 }