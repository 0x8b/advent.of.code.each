guide = ARGF
  .read
  .lines
  .map { |line| line.strip.split(" ") }


def score(guide)
  guide.map { |a, b|
    [
      (a == "A" ? :rock : (a == "B" ? :paper : :scissors)),
      (b == "X" ? :rock : (b == "Y" ? :paper : :scissors))
    ]
  }.map { |a, b|
    case [a, b]
    when [:rock, :rock]
      [3 + 1, 3 + 1]
    when [:paper, :paper]
      [3 + 2, 3 + 2]
    when [:scissors, :scissors]
      [3 + 3, 3 + 3]
    when [:rock, :paper]
      [1, 6 + 2]
    when [:rock, :scissors]
      [6 + 1, 3]
    when [:paper, :rock]
      [6 + 2, 1]
    when [:paper, :scissors]
      [2, 6 + 3]
    when [:scissors, :rock]
      [3, 6 + 1]
    when [:scissors, :paper]
      [6 + 3, 2]
    else
      "other"
    end
  }.map(&:last).sum
end


part1 = score(guide)

new_guide = guide.map { |a, b|
  if b == "X"
    [a, (a == "A" ? "Z" : (a == "B" ? "X" : "Y"))]
  elsif b == "Y"
    [a, (a == "A" ? "X" : (a == "B" ? "Y" : "Z"))]
  elsif b == "Z"
    [a, (a == "A" ? "Y" : (a == "B" ? "Z" : "X"))]
  end
}

part2 = score(new_guide)

p part1
p part2