calories = ARGF
  .read
  .split("\n\n")
  .map { _1
    .lines
    .map(&:to_i)
    .sum }

part_1 = calories.max
part_2 = calories.max(3).sum

puts part_1
puts part_2
