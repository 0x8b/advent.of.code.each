BITS = ARGF.read.chomp.chars.flat_map do |c|
  c.to_i(16).to_s(2).rjust(4, "0").chars.map(&:to_i)
end

def parse bits
  version = bits.shift(3).join.to_i(2)
  type    = bits.shift(3).join.to_i(2)

  if type == 4
    groups = []

    loop do
      groups << bits.shift(5)

      break if groups.last.shift == 0
    end

    return [version, type, groups.flatten.join.to_i(2)]
  else
    mode = bits.shift
    operator = type

    if mode == 0
      binary_length = bits.shift(15).join.to_i(2)
      binary = bits.shift(binary_length)

      subpackets = []
      subpackets << parse(binary) until binary.empty?

      return [version, operator, subpackets]
    else
      no_of_subpackets = bits.shift(11).join.to_i(2)

      return [version, operator, (1..no_of_subpackets).map { parse(bits) }]
    end
  end
end

def sum packet
  case packet
  in [version, _, Integer]
    version
  in [version, _, Array => packets]
    version + packets.sum { |packet| sum(packet) }
  end
end

part_1 = sum(parse(BITS.clone))
puts part_1

def evaluate node
  case node
  in [_, 0, args]       then args.map { |a| evaluate(a) }.reduce(:+)
  in [_, 1, args]       then args.map { |a| evaluate(a) }.reduce(:*)
  in [_, 2, args]       then args.map { |a| evaluate(a) }.min
  in [_, 3, args]       then args.map { |a| evaluate(a) }.max
  in [_, 4, val]        then val
  in [_, 5, [lhs, rhs]] then evaluate(lhs)  > evaluate(rhs) ? 1 : 0
  in [_, 6, [lhs, rhs]] then evaluate(lhs)  < evaluate(rhs) ? 1 : 0
  in [_, 7, [lhs, rhs]] then evaluate(lhs) == evaluate(rhs) ? 1 : 0
  end
end

part_2 = evaluate(parse(BITS.clone))
puts part_2
