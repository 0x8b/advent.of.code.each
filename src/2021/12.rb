CONNECTIONS = ARGF.read.lines.map do |line|
  line.chomp.split ?-
end

MAP = {}
MAP.default_proc = proc { |h, k| h[k] = [] }

CONNECTIONS.each do |connection|
  if connection.include? "start"
    MAP["start"] << (connection - ["start"]).first
  elsif connection.include? "end"
    MAP[(connection - ["end"]).first] << "end"
  else
    a, b = connection
    MAP[a] << b
    MAP[b] << a
  end
end

def traverse track
  if track.last == "end"
    TRACKS << track
    return
  end

  MAP[track.last].each do |cave|
    if cave.upcase == cave
      traverse track.dup + [cave]
    elsif cave.downcase == cave
      if track.count(cave) == 0
        traverse track.dup + [cave]
      end
    end
  end
end

TRACKS = []
traverse ["start"]
puts TRACKS.size

# part 2

def traverse track
  if track.last == "end"
    TRACKS << track
    return
  end

  MAP[track.last].each do |cave|
    if cave.upcase == cave
      traverse track.dup + [cave]
    elsif cave.downcase == cave
      if track.count(cave) == 0
        traverse track.dup + [cave]
      elsif track.count(cave) == 1
        if track.select { _1.downcase == _1 }.yield_self { _1.size == _1.uniq.size }
          traverse track.dup + [cave]
        end
      end
    end
  end
end

TRACKS.clear
traverse ["start"]
puts TRACKS.size
