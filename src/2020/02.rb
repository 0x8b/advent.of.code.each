tokenizer = /(\d+)-(\d+) (\w): (\w+)/

records = File.open("../../data/2020/02.txt").read.scan tokenizer

part_1 = records.count do |min, max, letter, password|
  password.count(letter).between? min.to_i, max.to_i
end

puts part_1

part_2 = records.count do |i, j, letter, password|
  (password[i.to_i - 1] == letter) != (password[j.to_i - 1] == letter)
end

puts part_2
