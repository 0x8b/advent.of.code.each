POS = ARGF.read.chomp.split(?,).map(&:to_i)

def fuel
  (POS.min..POS.max).map do |target|
    POS.map do |position|
      yield (position - target).abs
    end.sum
  end.min
end

part_1 = fuel { |d| d }
part_2 = fuel { |d| d * d.succ / 2 }

puts part_1
puts part_2
