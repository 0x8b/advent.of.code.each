POS = ARGF.read.chomp.split(?,).map(&:to_i)

def fuel
  (POS.min..POS.max).map do |target|
    POS.map do |position|
      yield (position - target).abs
    end.sum
  end.min
end

p fuel { |d| d }
p fuel { |d| d * d.succ / 2 }
