SIGOUT = ARGF.read.lines.map do |signal|
  signal = signal.scan(/\w+/).map(&:chars)

  [signal.shift(10), signal]
end

DIGITS = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

def deduce signal, output
  m = {}
  d = signal.group_by(&:size)

  m[?d] = d[4].concat(d[5]).inject(:&).first
  m[?f] = d[2].concat(d[6]).inject(:&).first
  m[?c] = (d[2].first - [m[?f]]).first
  m[?a] = (d[3].first - [m[?f], m[?c]]).first
  m[?b] = (d[4].first - [m[?f], m[?c], m[?d]]).first
  m[?g] = (d[6].inject(:&) - m.values).first
  m[?e] = ('abcdefg'.chars - m.values).first

  output.map do |s|
    DIGITS.index(s.map(&m.invert).sort.join)
  end
end

p SIGOUT.map { |sigout| deduce *sigout }.flatten.count { |d| [1, 4, 7, 8].include? d }
p SIGOUT.map { |sigout| deduce *sigout }.map { |d| d.map(&:to_s).join.to_i }.sum
