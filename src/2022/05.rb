stacks, _, instructions = ARGF.read.partition "\n\n"

instructions = instructions.split("\n").map { |line| line.scan(/\d+/).map(&:to_i) }

stacks = [
  %w(N S D C V Q T),
  %w(M F V),
  %w(F Q W D P N H M),
  %w(D Q R T F),
  %w(R F M N Q H V B),
  %w(C F G N P W Q),
  %w(W F R L C T),
  %w(T Z N S),
  %w(M S D J R Q H N)
]

instructions.each { |x, from, to|
  stacks[to - 1].push(*stacks[from - 1].pop(x))
}

p stacks.map(&:last).join

