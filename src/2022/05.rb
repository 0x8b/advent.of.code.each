stacks, _, instructions = ARGF.read.partition "\n\n"

stacks = stacks
  .lines
  .map { |line| line
    .chomp
    .chars }
  .transpose
  .filter { |c| c.last =~ /[1-9]/ }
  .map { |a| a.reject { |e| e == " " }.reverse.drop(1) }

instructions = instructions
  .split("\n")
  .map { |line| line
    .scan(/\d+/)
    .map(&:to_i) }

stacks_copy = stacks.map(&:clone)

instructions.each do |n, from, to|
  stacks[to - 1].push(*stacks[from - 1].pop(n).reverse)
end

puts stacks.map(&:last).join

instructions.each do |n, from, to|
  stacks_copy[to - 1].push(*stacks_copy[from - 1].pop(n))
end

puts stacks_copy.map(&:last).join

