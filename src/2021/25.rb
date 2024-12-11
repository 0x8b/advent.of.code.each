state = ARGF.read.lines.map { |line| line.chomp.chars }

h = state.size
w = state.first.size

steps = 1

loop do
  newstate = state.map { |row|
    r = (row + [row.first]).join.gsub(/>\./, '.>').chars

    if row.first == ?.
      r.drop(1).rotate(-1)
    else
      r.take(w)
    end
  }.transpose.map { |row|
    r = (row + [row.first]).join.gsub(/v\./, '.v').chars

    if row.first == ?.
      r.drop(1).rotate(-1)
    else
      r.take(h)
    end
  }.transpose

  break if newstate == state

  steps += 1

  state.replace newstate
end

part_1 = steps

puts part_1
