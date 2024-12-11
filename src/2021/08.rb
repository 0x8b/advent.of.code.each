SIGOUT = ARGF.read.lines.map do |line|
  sigout = line.scan(/\w+/).map(&:chars)

  [sigout.shift(10), sigout]
end

DIGITS = %w[abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg]

def deduce signal, output
  m = {}

  s = signal.sort_by &:size
  s2, s3, s4 = s.shift 3
  s5 = s.shift(3).reduce :&
  s6 = s.shift(3).reduce :&
  s7 = s.shift

  m[?d] = s4 & s5
  m[?f] = s2 & s6
  m[?c] = s2 - m[?f]
  m[?a] = s3 - m[?f] - m[?c]
  m[?b] = s4 - m[?f] - m[?c] - m[?d]
  m[?g] = s6 - m.values.flatten
  m[?e] = s7 - m.values.flatten

  m = m.transform_values(&:first).invert

  output.map do |s|
    DIGITS.index(s.map(&m).sort.join)
  end
end

part_1 = SIGOUT.map { |sigout| deduce *sigout }.flatten.count { [1, 4, 7, 8].include? _1 }
part_2 = SIGOUT.map { |sigout| deduce *sigout }.map { _1.map(&:to_s).join.to_i }.sum

puts part_1
puts part_2
