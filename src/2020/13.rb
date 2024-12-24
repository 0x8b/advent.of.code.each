data = File.open("../../data/2020/13.txt").map &:strip

earliest_timestamp = data[0].to_i
timestamps = data[1].split(",").zip(0..).filter_map { |id, i| [id.to_i, i] if id != ?x }

ids = timestamps.map &:first

minutes, bus_id = ids.map { |id| ((earliest_timestamp / id) + 1) * id }.zip(ids).min_by { |t, id| t - earliest_timestamp }

part_1 = bus_id * (minutes - earliest_timestamp)

puts part_1
