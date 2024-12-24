require 'set'

PARENTS  = Hash.new { |h, k| h[k] = [] }
CONTENTS = Hash.new { |h, k| h[k] = [] }

def parse_rule rule
  parent = rule.scan(/\w+ \w+/).first

  rule.scan(/(\d+) (\w+ \w+)/).each do |quantity, child|
    PARENTS[child].push parent
    CONTENTS[parent].push [quantity.to_i, child]
  end
end

File.open("../../data/2020/07.txt").each_line { |rule| parse_rule rule.strip }


parents = Set["shiny gold"]

loop do
  more_parents = PARENTS.values_at(*parents).flatten.to_set

  break if more_parents.subset? parents

  parents |= more_parents
end

part_1 = parents.size - 1

puts part_1


def count_content parent
  CONTENTS[parent].sum do |quantity, child|
    quantity + quantity * count_content(child)
  end
end

part_2 = count_content "shiny gold"

puts part_2
