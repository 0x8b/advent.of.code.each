instructions = File.open("../../data/2020/12.txt").map { |i| [i[0], i[1..].to_i] }

INITIAL_POS = Complex(0, 0)
D = {
  ?N => Complex( 0,  1),
  ?S => Complex( 0, -1),
  ?E => Complex( 1,  0),
  ?W => Complex(-1,  0),
  ?R => Complex( 0, -1),
  ?L => Complex( 0,  1),
}

p1 = INITIAL_POS
dir = D[?E]

p2 = INITIAL_POS
wp = 10 * D[?E] + D[?N]

instructions.each do |action, val|
  case action
  in ?N | ?S | ?W | ?E
    p1 += val * D[action]
    wp += val * D[action] # part 2
  in ?F
    p1 += val * dir
    p2 += val * wp # part 2
  in ?L | ?R
    n = val / 90
    dir *= D[action] ** n
    wp  *= D[action] ** n # part 2
  end
end

part_1 = p1.rect.sum &:abs
part_2 = p2.rect.sum &:abs

puts part_1
puts part_2
