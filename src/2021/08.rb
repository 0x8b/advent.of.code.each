SIGNALS = ARGF.read.lines.map do |signal|
  signal = signal.scan /\w+/

  [signal.first(10).map(&:chars), signal.last(4).map(&:chars)]
end

MAPPING = {
    'abcefg' => 0,
    'cf' => 1,
    'acdeg' => 2,
    'acdfg' => 3,
    'bcdf' => 4,
    'abdfg' => 5,
    'abdefg' => 6,
    'acf' => 7,
    'abcdefg' => 8,
    'abcdfg' => 9,
}

def decode signal, output
  m = {}

  d = signal.group_by(&:size)

  m['d'] = d[4].concat(d[5]).inject(:&).first
  m['f'] = d[2].concat(d[6]).inject(:&).first
  m['c'] = (d[2].first - [m['f']]).first
  m['a'] = (d[3].first - [m['f'], m['c']]).first
  m['b'] = (d[4].first - [m['f'], m['c'], m['d']]).first
  m['g'] = (d[6].inject(:&) - m.values).first
  m['e'] = ('abcdefg'.chars - m.values).first

  m = m.invert

  output.map do |s|
    MAPPING[s.map(&m).sort.join]
  end
end

p SIGNALS.map { |signal| decode *signal }.flatten.count { |d| [1, 4, 7, 8].include? d }
p SIGNALS.map { |signal| decode *signal }.map { |d| d.map(&:to_s).join.to_i }.sum
