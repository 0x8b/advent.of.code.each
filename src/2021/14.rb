POLYMER, RULES = ARGF.read.split "\n\n"

RULES = RULES.lines.map do |line|
  line.chomp.split " -> "
end.to_h

def answer steps
  h = POLYMER.chars.each_cons(2).map(&:join).tally

  # pair insertion process
  steps.times do
    hh = {}
    hh.default = 0

    h.each_pair do |k,v|
      mid = RULES[k]
      hh[k[0] + mid] += h[k]
      hh[mid + k[1]] += h[k]
    end

    h.replace hh
  end

  # count elements
  e = {}
  e.default = 0
  h.each_pair do |k, v|
    e[k[0]] += v
    e[k[1]] += v
  end

  # almost all items are double-counted except the first and the last piece of starting polymer
  e[POLYMER.chars.first] += 1
  e[POLYMER.chars.last] += 1

  e.values.map { |v| v / 2 }.minmax.inject(:-).abs
end

puts answer 10
puts answer 40
