SNAILFISH_NUMS = ARGF.read.lines.map { |line| eval(line.chomp) }

def explode flat
  case flat
  in [[_, 5], [b, 5], [c, d], *tail]
    explode [[0, 4], [b + c, d], *tail]
  in [*head, [a, b], [c, 5], [d, 5], [e, f], *tail]
    explode [*head, [a + c, b], [0, 4], [d + e, f], *tail]
  in [*head, [a, b], [c, 5], [_, 5]]
    explode [*head, [a + c, b], [0, 4]]
  else
    flat
  end
end

def split flat
  case flat
  in [*head, [10.. => v, lvl], *tail]
    [*head, [v / 2, lvl + 1], [v - v / 2, lvl + 1], *tail]
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

  case flat
  in [[a, 1], [b, 1]]
    [a, b]
  in [*head, [a, ^maxlvl], [b, ^maxlvl], *tail]
    pairs([*head, [[a, b], maxlvl - 1], *tail])
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

def reduce before
  after = pairs(split(explode(flatten(before))))

  return after if before == after

  reduce(after)
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
