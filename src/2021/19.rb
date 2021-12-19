MAP = ARGF.read.split("\n\n").map do |scanner|
  scanner.lines.drop(1).map do |position|
    position.chomp.split(",").map(&:to_i)
  end
end

SCANNERS = (0...MAP.size).zip(MAP).to_h

def roll ((x, y, z))
  yz = 1i * Complex(y, z)
  return x, yz.real, yz.imag
end

def pitch ((x, y, z))
  zx = 1i * Complex(z, x)
  return zx.real, y, zx.imag
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
