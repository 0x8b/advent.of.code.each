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
  def intersects? other
    self.intersection(other) != nil
  end

  def intersection other
    intersection_begin = case
    when self.include?(other.begin)
      other.begin
    when other.include?(self.begin)
      self.begin
    else
      return nil
    end

    intersection_end = case self.end <=> other.end
    when -1
      self.end
    when 0
      self.end
    when 1
      other.end
    end

    self.class.new(intersection_begin, intersection_end)
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
    intersection = self.intersection(other)

    return intersection.x && intersection.y && intersection.z
  end

  def intersection other
    self.class.new(:on, self.x & other.x, self.y & other.y, self.z & other.z)
  end
end

CUBOIDS = steps.map { |type, x, y, z| Cuboid.new(type, x, y, z) }

puts CUBOIDS.inject([]) { |prev, cuboid| # part two
  nxt = prev.flat_map { |c|
    results = []

    if c.intersect?(cuboid)
      intersection = c.intersection(cuboid).oftype(:on)
      results << c

      if cuboid.type == :on
        results << intersection.oftype(c.type == :on ? :off : :on)
      else
        results << intersection.oftype(c.type == :on ? :off : :on)
      end
    else
      results << c
    end

    results
  }

  nxt << cuboid if cuboid.type == :on
  nxt
}.map(&:volume).sum
