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

def caveman track, &block
  if track.last == "end"
    TRACKS << track
    return
  end

  MAP[track.last].each do |cave|
    if cave.upcase == cave
      caveman track + [cave], &block
    elsif block.call(track, cave)
      caveman track + [cave], &block
    end
  end
end

TRACKS = []
caveman(["start"]) { |track, cave| track.count(cave) == 0 }
puts TRACKS.size

TRACKS.clear
caveman(["start"]) { |track, cave| track.count(cave) == 0 or (track.count(cave) == 1 and track.select { _1.downcase == _1 }.yield_self { _1.size == _1.uniq.size })}
puts TRACKS.size
