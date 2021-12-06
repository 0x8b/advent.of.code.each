LANTERNFISH = ARGF.read.strip.split(?,).map(&:to_i)

def lanternfish epochs
  state = LANTERNFISH.clone.tally

  epochs.times do
    state = state.to_a.flat_map do |k, v|
      k == 0 ? [[6, v], [8, v]] : [[k - 1, v]]
    end.map do |ary|
      [ary].to_h
    end.inject do |s, update|
      s.merge(update) do |_, v, u| v + u end
    end
  end

  state.values.sum
end

p lanternfish 80
p lanternfish 256
