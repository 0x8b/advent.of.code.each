SNAILFISH_NUMS = ARGF.read.lines.map { |line| eval(line.chomp) }

def explode flat
  case flat
  in [[left, 5], [right, 5], [right_regular, level], *nxt]
    [[0, 4], [right + right_regular, level], *nxt]
  in [*prv, [left_regular, left_level], [left, 5], [right, 5], [right_regular, right_level], *nxt]
    [*prv, [left_regular + left, left_level], [0, 4], [right + right_regular, right_level], *nxt]
  in [*prv, [left_regular, level], [left, 5], [right, 5]]
    [*prv, [left_regular + left, level], [0, 4]]
  else
    flat
  end
end

def split flat
  case flat
  in [*prv, [10.. => v, lvl], *nxt]
    [*prv, [v / 2, lvl + 1], [v - v / 2, lvl + 1], *nxt]
  else
    flat
  end
end

def flatten pair, level=1
  case pair
  in [Integer => left, Integer => right] then [[left, level], [right, level]]
  in [Integer => left, Array =>   right] then [[left, level], *flatten(right, level + 1)]
  in [Array =>   left, Integer => right] then [*flatten(left, level + 1), [right, level]]
  in [Array =>   left, Array =>   right] then [*flatten(left, level + 1), *flatten(right, level + 1)]
  end
end

def pairs flat
  maxlvl = flat.map(&:last).max

  return flat.map(&:first) if maxlvl == 1

  case flat
  in [a]
    pairs(a)
  in [a, 1]
    a
  in [a, Integer => n]
    pairs([a, n - 1])
  in [*pre, [a, ^maxlvl], [b, ^maxlvl], *post]
    pairs([*pre, [[a, b], maxlvl - 1], *post])
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
    after = pairs(explode(flatten(before)))
    if after != before
      before.replace after
      next
    else
      after.replace pairs(split(flatten(after)))
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

puts magnitude(add(SNAILFISH_NUMS)) # part 1

puts SNAILFISH_NUMS.permutation(2).map { |a, b| # part 2
  magnitude(add([a, b]))
}.max
