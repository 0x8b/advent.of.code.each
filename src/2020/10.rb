data = File.open("../../data/2020/10.txt").each_line.map &:to_i

data = [0, *data.sort, data.max + 3]

part_1 = data.each_cons(2).map { |a, b| b - a }.tally.values.inject(:*)

puts part_1

ways = [0] * data.size

ways[0] = 1

for i in (1...data.size) do
  for j in (1..3) do
    if i - j >= 0
      if data[i] - data[i - j] <= 3
        ways[i] += ways[i - j]
      end
    end
  end
end

part_2 = ways.last

puts part_2
