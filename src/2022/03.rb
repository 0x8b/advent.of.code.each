rucksacks = ARGF
  .read
  .lines
  .map { |line| line.strip.chars }

priority = -> (char) {
  if char in "a".."z"
    char.ord - "a".ord + 1
  else
    char.ord - "A".ord + 1 + 26
  end
}

part_1 = rucksacks
  .map { |rucksack|
    rucksack
      .each_slice(rucksack.size / 2)
      .inject(&:&) }
  .flatten
  .map(&priority)
  .sum

part_2 = rucksacks
  .each_slice(3)
  .map { |group| group.inject(&:&) }
  .flatten
  .map(&priority)
  .sum

puts part_1
puts part_2
