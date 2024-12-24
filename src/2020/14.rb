program = File.open("../../data/2020/14.txt").map do |line|
  line.scan /[01X]{36}|\d+/
end

def sum_memory program, &store
  memory = Hash.new { |h, k| h[k] = 0 }
  mask = ?X * 36

  program.each do |instruction|
    case instruction
      in [address, value]
        store[memory, address.to_i, value.to_i, mask]
      in [new_mask]
        mask = new_mask
    end
  end

  memory.values.sum
end

def combine_value_with_mask value, mask, &rules
  new_value = value.to_s(2).rjust(36, ?0).chars.zip(mask.chars).map do |v, m|
    rules[v, m]
  end.join

  if new_value.include? ?X
    [?0, ?1].repeated_permutation(new_value.count ?X).map do |bits_permutation|
      (new_value.gsub(?X, '%s') % bits_permutation).to_i 2
    end
  else
    [new_value.to_i(2)]
  end
end


part_1 = sum_memory(program) { |memory, address, value, mask|
  memory[address] = combine_value_with_mask(value, mask) { |value_bit, mask_bit|
    mask_bit == ?X ? value_bit : mask_bit
  }.first
}

puts part_1


part_2 = sum_memory(program) { |memory, address, value, mask|
  addresses = combine_value_with_mask(address, mask) { |address_bit, mask_bit|
    mask_bit == ?X ? ?X : mask_bit == ?0 ? address_bit : 1
  }

  addresses.each { |a| memory[a] = value }
}

puts part_2
