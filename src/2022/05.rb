stacks, instructions = ARGF.read.split "\n\n"

stacks = stacks
  .lines
  .map { |line| line
    .chomp
    .chars }
  .transpose
  .filter { |column| column.last =~ /[1-9]/ }
  .map { |column| column
    .reject { |ch| ch == " " }
    .reverse
    .drop(1) }

instructions = instructions
  .split("\n")
  .map { |line| line
    .scan(/\d+/)
    .map(&:to_i) }


def procedure(stacks, instructions, same_order = false)
  stacks = stacks.map(&:clone)

  instructions.each do |n, from, to|
    crates = stacks[from - 1].pop(n)
    crates = crates.reverse unless same_order
    stacks[to - 1].push(*crates)
  end
  
  stacks.map(&:last).join
end


puts procedure(stacks, instructions)
puts procedure(stacks, instructions, true)