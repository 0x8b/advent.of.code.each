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

p rucksacks
  .map { |rucksack|
    rucksack
      .each_slice(rucksack.size / 2)
      .inject(&:&) }
  .flatten
  .map(&priority)
  .sum

p rucksacks
  .each_slice(3)
  .map { |group| group.inject(&:&) }
  .flatten
  .map(&priority)
  .sum