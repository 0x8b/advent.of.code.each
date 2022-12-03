require 'set'

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
    [
      rucksack[...rucksack.size / 2],
      rucksack[(rucksack.size / 2)..]
    ]
      .map(&:to_set)
      .inject(&:intersection)
      .to_a
      .map(&priority) }
  .flatten
  .sum

p rucksacks
  .each_slice(3)
  .map { |group|
    group
      .map(&:to_set)
      .inject(&:intersection)
      .to_a }
  .flatten
  .map(&priority)
  .sum