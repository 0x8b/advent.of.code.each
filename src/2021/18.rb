SNAILFISH_NUMS = ARGF.read.lines.map { |line| eval(line.chomp) }

def explode list
  found = list.map(&:last).each_cons(2).find { |a, b| a == 5 and a == b }

  if found
    found = found.first
    case list
    in [[left, ^found], [right, ^found], [rregular, rlvl], *post]
      [[0, found - 1], [right + rregular, rlvl], *post]
    in [*pre, [lregular, llvl], [left, ^found], [right, ^found], [rregular, rlvl], *post]
      [*pre, [lregular + left, llvl], [0, found - 1], [right + rregular, rlvl], *post]
    in [*pre, [lregular, llvl], [left, ^found], [right, ^found]]
      [*pre, [lregular + left, llvl], [0, found - 1]]
    end
  else
    list
  end
end

def split list
  index = list.index { |number, level| number >= 10 }

  if index
    number, level = list.delete_at(index)
    list.insert(index, [number / 2, level + 1], [number - number / 2, level + 1])
    list
  else
    list
  end
end

def breakdown pair, level=1
  case pair
  in [Integer => left, Integer => right]
    [[left, level], [right, level]]
  in [Integer => left, Array => right]
    [[left, level], *breakdown(right, level + 1)]
  in [Array => left, Integer => right]
    [*breakdown(left, level + 1), [right, level]]
  in [Array => left, Array => right]
    [*breakdown(left, level + 1), *breakdown(right, level + 1)]
  end
end

def buildup list
  maxlvl = list.map(&:last).max

  return list.map(&:first) if maxlvl == 1

  case list
  in [a]
    buildup(a)
  in [a, 1]
    a
  in [a, Integer => n]
    buildup([a, n - 1])
  in [*pre, [a, ^maxlvl], [b, ^maxlvl], *post]
    buildup([*pre, [[a, b], maxlvl - 1], *post])
  end
end

def magnitude pair
  case pair
  in Integer => i
    i
  in [Integer => l, Integer => r]
    3 * l + 2 * r
  in [l, r]
    magnitude([magnitude(l), magnitude(r)])
  end
end

def reduce pair
  before = pair

  loop do
    after = buildup(explode(breakdown(before)))
    if after != before
      before.replace after
      next
    else
      after.replace buildup(split(breakdown(after)))
    end

    break if after == before

    before.replace after
  end

  before
end

def add numbers
  numbers.reduce do |a, b|
    reduce([a, b])
  end
end

puts magnitude(add(SNAILFISH_NUMS))

puts SNAILFISH_NUMS.permutation(2).map { |a, b|
  magnitude(add([a, b]))
}.max
