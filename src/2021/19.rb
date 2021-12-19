MAP = ARGF.read.split("\n\n").map do |scanner|
  scanner.lines.drop(1).map do |bacon|
    bacon.chomp.split(",").map(&:to_i)
  end
end

SCANNERS = (0...MAP.size).zip(MAP).to_h

def roll ((x, y, z))
  yz = 1i * Complex(y, z)
  return x, yz.real, yz.imag
end

def pitch ((x, y, z))
  zx = 1i * Complex(z, x)
  return zx.imag, y, zx.real
end

def yaw ((x, y, z))
  xy = 1i * Complex(x, y)
  return xy.real, xy.imag, z
end

TRANSFORMATIONS = [
  -> (b) { b },
  -> (b) { yaw b },
  -> (b) { yaw yaw b },
  -> (b) { yaw yaw yaw b },

  -> (b) { roll b },
  -> (b) { yaw roll b },
  -> (b) { yaw yaw roll b },
  -> (b) { yaw yaw yaw roll b },

  -> (b) { roll roll b },
  -> (b) { yaw roll roll b },
  -> (b) { yaw yaw roll roll b },
  -> (b) { yaw yaw yaw roll roll b },

  -> (b) { roll roll roll b },
  -> (b) { yaw roll roll roll b },
  -> (b) { yaw yaw roll roll roll b },
  -> (b) { yaw yaw yaw roll roll roll b },

  -> (b) { pitch b },
  -> (b) { yaw pitch b },
  -> (b) { yaw yaw pitch b },
  -> (b) { yaw yaw yaw pitch b },

  -> (b) { pitch pitch pitch b },
  -> (b) { yaw pitch pitch pitch b },
  -> (b) { yaw yaw pitch pitch pitch b },
  -> (b) { yaw yaw yaw pitch pitch pitch b },
]


def relative_position from, to
  from.zip(to).map { |a, b| b - a }
end

require 'set'

BEACONS = SCANNERS.delete(0).to_set
SCANNERS_POSITIONS = [[0, 0]]

OFFSET = 3000 # very important

until SCANNERS.empty?
  scores = []

  SCANNERS.each do |scanner, beacons|
    TRANSFORMATIONS.each.with_index do |transformation, ti|
      moved = beacons.map { |b| transformation.call(b).map { |c| c + OFFSET } }

      most_common_distance, count = BEACONS.to_a.product(moved).map do |b1, b2|
        relative_position(b1, b2)
      end.tally.max_by { |distance, count| count }

      scores << [scanner, ti, most_common_distance.map{ |c| c - OFFSET }.map { |c| -c }, count]
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

puts BEACONS.size # part 1

puts SCANNERS_POSITIONS.combination(2).map { |b1, b2| # part 2
  relative_position(b1, b2).map(&:abs).sum
}.max
