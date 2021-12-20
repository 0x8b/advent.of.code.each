require 'set'

MAP = ARGF.read.split("\n\n").map do |scanner|
  scanner.lines.drop(1).map do |beacon|
    beacon.chomp.split(",").map(&:to_i)
  end
end

SCANNERS = (0...MAP.size).zip(MAP).to_h

def roll ((x, y, z), n=1)
  yz = 1i ** n * Complex(y, z)
  return x, yz.real, yz.imag
end

def pitch ((x, y, z), n=1)
  zx = 1i ** n * Complex(z, x)
  return zx.imag, y, zx.real
end

def yaw ((x, y, z), n=1)
  xy = 1i ** n * Complex(x, y)
  return xy.real, xy.imag, z
end

def method_missing method, *args, &block
  if /^(?<name>pitch|roll|yaw)(?<n>\d+)?$/ =~ method
    send(name.to_sym, *args, n && n.to_i || 1, &block)
  else
    super
  end
end

TRANSFORMATIONS = [
  -> (b) { b },
  -> (b) { yaw b },
  -> (b) { yaw2 b },
  -> (b) { yaw3 b },

  -> (b) { roll b },
  -> (b) { yaw roll b },
  -> (b) { yaw2 roll b },
  -> (b) { yaw3 roll b },

  -> (b) { roll2 b },
  -> (b) { yaw roll2 b },
  -> (b) { yaw2 roll2 b },
  -> (b) { yaw3 roll2 b },

  -> (b) { roll3 b },
  -> (b) { yaw roll3 b },
  -> (b) { yaw2 roll3 b },
  -> (b) { yaw3 roll3 b },

  -> (b) { pitch b },
  -> (b) { yaw pitch b },
  -> (b) { yaw2 pitch b },
  -> (b) { yaw3 pitch b },

  -> (b) { pitch3 b },
  -> (b) { yaw pitch3 b },
  -> (b) { yaw2 pitch3 b },
  -> (b) { yaw3 pitch3 b },
]

def relative_position from, to
  from.zip(to).map { |a, b| b - a }
end

BEACONS = SCANNERS.delete(0).to_set
SCANNERS_POSITIONS = [[0, 0]]

TRANSLATE = 3000

until SCANNERS.empty?
  scores = []

  SCANNERS.each do |scanner, beacons|
    TRANSFORMATIONS.each.with_index do |transformation, tindex|
      translated = beacons.map { |b| transformation.call(b).map { |v| v + TRANSLATE } }

      most_common_distance, count = BEACONS.to_a.product(translated).map do |b1, b2|
        relative_position(b1, b2)
      end.tally.max_by { |distance, count| count }

      scores << [scanner, tindex, most_common_distance.map { |v| v - TRANSLATE }.map { |v| -v }, count]
    end
  end

  scanner, transformation, most_common_distance, _ = scores.max_by(&:last)

  SCANNERS_POSITIONS << most_common_distance

  SCANNERS[scanner].map do |beacon|
    TRANSFORMATIONS[transformation].call(beacon)
  end.map do |beacon|
    beacon.zip(most_common_distance).map(&:sum)
  end.each do |beacon|
    BEACONS << beacon
  end

  SCANNERS.delete(scanner)
end

puts BEACONS.size # part one

puts SCANNERS_POSITIONS.combination(2).map { |b1, b2| # part two
  relative_position(b1, b2).map(&:abs).sum
}.max
