require 'set'

p1, p2 = File.open("../../data/2020/22.txt").read.split("\n\n").map do |player|
  player.lines.map(&:strip).drop(1).map(&:to_i)
end

def play p1, p2, is_p2
  seen = Set[]

  while p1.size > 0 and p2.size > 0
    if seen.include?([p1, p2]) and is_p2
      return [true, p1]
    end

    seen.add([p1.dup, p2.dup])

    c1 = p1.shift
    c2 = p2.shift

    is_p1_winning = false

    if p1.size >= c1 and p2.size >= c2 and is_p2
      is_p1_winning, _ = play p1[...c1], p2[...c2], is_p2
    else
      is_p1_winning = c1 > c2
    end

    if is_p1_winning
      p1.push c1, c2
    else
      p2.push c2, c1
    end
  end

  if p1.size > 0
    return [true, p1]
  else
    return [false, p2]
  end
end

def score player
  (1..player.size).to_a.reverse.zip(player).map { |i, c| i * c }.sum
end

[false, true].each do |is_p2|
  _, winner = play(p1.dup, p2.dup, is_p2)

  puts score(winner) # part_1, part_2
end
