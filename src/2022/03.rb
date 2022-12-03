require 'set'

items = ARGF
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

part1 = items
  .map { |compartments|
    [
      compartments[...compartments.size / 2],
      compartments[(compartments.size / 2)..]
    ]
      .map(&:to_set)
      .inject(&:intersection)
      .to_a
      .map(&priority) }
  .flatten
  .sum

part2 = items
  .each_slice(3)
  .map { |group| group.map(&:to_set).inject(&:intersection).to_a }
  .flatten
  .map(&priority)
  .sum

puts part1
puts part2