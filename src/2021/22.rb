STEPS = []
SPACE = {}

ARGF.read.lines.each do |line|
  [STEPS, SPACE].instance_eval <<~END
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

part_1 = SPACE.values.count(:on)
puts part_1

class Range
  def intersection range
    if self.include?(range.begin) or range.include?(self.begin)
      _, b, e, _ = [self.begin, self.end, range.begin, range.end].sort

      b..e
    end
  end

  alias_method :&, :intersection
end

class Cuboid
  attr_reader :type, :ranges

  def initialize type, x, y, z
    @type = type
    @ranges = [x, y, z]
  end

  def of_type type
    @type = type
    self
  end

  def volume
    vol = self.ranges.map(&:size).reduce(:*)

    self.type == :on ? vol : -vol
  end

  def intersect? other
    self.intersection(other).ranges.all?
  end

  def intersection other
    self.class.new(:on, *self.ranges.zip(other.ranges).map { |r, r2| r & r2 })
  end
end

CUBOIDS = STEPS.map { |type, x, y, z| Cuboid.new(type, x, y, z) }

part_2 = CUBOIDS.inject([]) { |processed, unseen_cuboid| # part two
  next_processed = processed.group_by(&:ranges).reject { |k, v| v.size % 2 == 0 }.values.flatten.flat_map { |cuboid|
  #next_processed = processed.flat_map { |cuboid|
    if cuboid.intersect?(unseen_cuboid)
      intersection = cuboid.intersection(unseen_cuboid)

      [cuboid, intersection.of_type(cuboid.type == :on ? :off : :on)]
    else
      [cuboid]
    end
  }

  next_processed << unseen_cuboid if unseen_cuboid.type == :on
  next_processed
}.map(&:volume).sum

puts part_2
