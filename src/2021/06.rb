LANTERNFISH = ARGF.read.strip.split(?,).map(&:to_i)

def lanternfish epochs
  state = LANTERNFISH.clone.tally

  epochs.times do
    next_state = Hash.new 0

    state.to_a.flat_map do |k, v|
      k == 0 ? [[6, v], [8, v]] : [[k - 1, v]] # notice that 0 and 7 -> 6
    end.each do |k, v|
      next_state[k] += v
    end

    state.replace next_state
  end

  state.values.sum
end

part_1 = lanternfish 80
part_2 = lanternfish 256

puts part_1
puts part_2
