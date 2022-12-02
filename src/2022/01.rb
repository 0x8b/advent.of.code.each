calories = ARGF
  .read
  .split("\n\n")
  .map { _1
    .lines
    .map(&:to_i)
    .sum }

puts calories.max
puts calories.max(3).sum