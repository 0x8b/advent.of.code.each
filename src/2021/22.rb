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
  attr_reader :type, :x, :y, :z

  def initialize type, x, y, z
    @type = type
    @x = x
    @y = y
    @z = z
  end

  def oftype(type)
    @type = type
    self
  end

  def volume
    vol = self.x.count * self.y.count * self.z.count
    vol *= -1 if self.type == :off
    vol
  end

  def intersect? other
    cuboid = self.intersection(other)

    return cuboid.x && cuboid.y && cuboid.z
  end

  def intersection other
    self.class.new(:on, self.x & other.x, self.y & other.y, self.z & other.z)
  end
end

CUBOIDS = steps.map { |type, x, y, z| Cuboid.new(type, x, y, z) }

puts CUBOIDS.inject([]) { |prev, cuboid| # part two
  nxt = prev.flat_map { |c|
    if c.intersect?(cuboid)
      intersection = c.intersection(cuboid)

      [c, intersection.oftype(c.type == :on ? :off : :on)]
    else
      [c]
    end
  }

  nxt << cuboid if cuboid.type == :on
  nxt
}.map(&:volume).sum
