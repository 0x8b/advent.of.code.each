data = File.open("../../data/2020/09.txt").each_line.map &:to_i

invalid = data.each_cons(26).find do |*previous, target|
  previous.combination(2).all? { |c| c.sum != target }
end.last

part_1 = invalid

puts part_1

b, e = 0, 0

while b < data.length do
  if data[b..e].sum == invalid
    break if e > b # at least two numbers
  elsif data[b..e].sum < invalid
    e += 1
  else
    b += 1
  end
end

part_2 = data[b..e].minmax.sum

puts part_2
