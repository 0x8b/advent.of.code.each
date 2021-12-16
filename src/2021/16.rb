BITS = ARGF.read.chomp.chars.flat_map { |c|
  c.to_i(16).to_s(2).rjust(4, "0").chars.map &:to_i
}


def parse bits, n = Float::INFINITY
  values = []

  loop do
    break if bits.size <= 6
    version = bits.shift(3).join.to_i(2)
    type_id = bits.shift(3).join.to_i(2)

    case type_id
    when 4
      groups = []

      loop do
        prefix, *group = bits.shift(5)
        groups << group
        break if prefix == 0
      end

      values << [version, type_id, groups.flatten.join.to_i(2)]
    else
      length_type_id = bits.shift.to_i
      operator = type_id

      if length_type_id == 0
        total_length_in_bits = bits.shift(15).join.to_i(2)

        values << [version, operator, parse(bits.shift(total_length_in_bits))]
      else
        num_of_subpackets = bits.shift(11).join.to_i(2)

        values << [version, operator, parse(bits, num_of_subpackets)]
      end
    end

    n -= 1

    if n == 0
      return values
    end
  end

  values
end

def sum_operators a_or_i
  case a_or_i
  in Array
    a_or_i.sum { |a| a.first + sum_operators(a.last) }
  in Integer
    0
  end
end

p sum_operators(parse(BITS.dup))

def eval_lisp ast
  case ast
  in [a, b]
    eval_lisp(a)
  in [a]
    eval_lisp(a)
  in [_, 4, value]
    value
  in [_, 0, [*operands]]
    operands.map { eval_lisp(_1) }.sum
  in [_, 1, [*operands]]
    operands.map { eval_lisp(_1) }.reduce(:*)
  in [_, 2, [*operands]]
    operands.map { eval_lisp(_1) }.min
  in [_, 3, [*operands]]
    operands.map { eval_lisp(_1) }.max
  in [_, 5, [left, right]]
    if eval_lisp(left) > eval_lisp(right) then 1 else 0 end
  in [_, 6, [left, right]]
    if eval_lisp(left) < eval_lisp(right) then 1 else 0 end
  in [_, 7, [left, right]]
    if eval_lisp(left) == eval_lisp(right) then 1 else 0 end
  end
end

p eval_lisp(parse(BITS.dup))
