POS = ARGF.read.lines.map { |line| line.chomp.split.last.to_i }.map &:pred
POS2 = POS.clone
SCORE = [0, 0]

DETERDICE = (1..100).cycle
rolls = 0
player = 0

loop do
  rolls += 3
  a = 3.times.map { DETERDICE.next }.sum

  POS[player] = (POS[player] + a) % 10
  SCORE[player] += POS[player] + 1

  if SCORE[player] >= 1000
    puts SCORE.min * rolls # part one
    break
  end

  player = (player + 1) % 2
end

MEMO = {}
POSSIBILITIES = [1, 2, 3].repeated_permutation(3).to_a

def count p1, p2, s1, s2
  return [1, 0] if s1 >= 21
  return [0, 1] if s2 >= 21
  return MEMO[[p1, p2, s1, s2]] if MEMO.include? [p1, p2, s1, s2]

  MEMO[[p1, p2, s1, s2]] = POSSIBILITIES.reduce([0, 0]) do |ans, poss|
    np1 = (p1 + poss.sum) % 10
    ns1 = s1 + np1 + 1

    ans.zip(count(p2, np1, s2, ns1).reverse).map(&:sum)
  end
end

puts count(*POS2, 0, 0).max # part two
