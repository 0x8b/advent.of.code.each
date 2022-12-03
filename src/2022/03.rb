require 'set'

rucksacks = ARGF
  .read
  .lines
  .map { |line| line.strip.chars }

priority = -> (char) {
  if char.ord < 97
    char.ord - 64 + 26
  else
    char.ord - 96
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