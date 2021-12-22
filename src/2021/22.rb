steps = []
space = {}

ARGF.read.lines.each do |line|
  [steps, space].instance_eval <<~END
    turn=:#{line.chomp.tr(", ", ";")}

    self[0] << [turn, x, y, z]

    if [x, y, z].all? { |range| (-50..50).cover? range }
      x.each { |x|
        y.each { |y|
          z.each { |z|
            self[1][[x, y, z]] = turn
          }
        }
      }
    end
  END
end

puts space.values.count(:on) # part one
