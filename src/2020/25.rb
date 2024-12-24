card_public_key, door_public_key = File.open("../../data/2020/25.txt").each_line.map &:to_i


def encryption_key(subject_number, loop_size)
  key = 1

  loop_size.times do
    key = (key * subject_number) % 20201227
  end

  key
end


def find_loop_size public_key
  loop_size = 1

  current_key = 1

  loop do
    current_key = (current_key * 7) % 20201227

    if current_key == public_key
      return loop_size
    end

    loop_size += 1
  end
end

part_1 = encryption_key(door_public_key, find_loop_size(card_public_key))
part_2 = encryption_key(card_public_key, find_loop_size(door_public_key))

puts part_1
puts part_2
