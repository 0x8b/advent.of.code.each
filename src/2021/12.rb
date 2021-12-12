MAP = {}
MAP.default_proc = proc { |h, k| h[k] = [] }

ARGF.read.lines.each do |line|
  case line.chomp.split(?-)
  in "start", c
    MAP["start"] << c
  in c, "start"
    MAP["start"] << c
  in "end", c
    MAP[c] << "end"
  in c, "end"
    MAP[c] << "end"
  in c, cc
    MAP[cc] << c
    MAP[c] << cc
  end
end

def caveman track, &can_visit_small_cave
  if track.last == "end"
    TRACKS << track
  else
    MAP[track.last].each do |cave|
      if cave.upcase == cave or can_visit_small_cave.call(track, cave)
        caveman track + [cave], &can_visit_small_cave
      end
    end
  end
end

TRACKS = []
caveman(["start"]) { |track, cave| track.count(cave) == 0 }
puts TRACKS.size

TRACKS.clear
caveman(["start"]) { |track, cave| track.count(cave) == 0 or (track.count(cave) == 1 and track.select { _1.downcase == _1 }.yield_self { _1.size == _1.uniq.size })}
puts TRACKS.size
