VEINS = ARGF.read.lines.map &:chomp

GROUND = {}

GROUND.default = :sand

VEINS.each { |vein|
  GROUND.instance_eval <<~END
    #{vein.tr ',', ';'}

    case [x, y]
    in Integer, Range
      y.each { |y| self[[x, y]] = :clay }
    in Range, Integer
      x.each { |x| self[[x, y]] = :clay }
    end
  END
}

# TODO

# RENDER PREVIEW

MIN_X, MAX_X = GROUND.keys.map(&:first).minmax
MIN_Y, MAX_Y = GROUND.keys.map(&:last).minmax

MAP = []
OFFSET = 10

MAP << "P3"
MAP << "#{MAX_X - MIN_X + 1 + 2 * OFFSET} #{MAX_Y - MIN_Y + 1 + 2 * OFFSET}"
MAP << "255"
((MIN_Y - OFFSET)..(MAX_Y + OFFSET)).each { |y|
  MAP << ""
  ((MIN_X - OFFSET)..(MAX_X + OFFSET)).each { |x|
    color = case GROUND[[x, y]]
            when :sand
              [0, 0, 0]
            when :clay
              [255, 255, 255]
            when :water
              [0, 255, 0]
            when :stream
              [255, 0, 255]
            end
    MAP.last << color.map(&:to_s).join(" ") + " "
  }
}

File.write "./map.ppm", MAP.join("\n")
