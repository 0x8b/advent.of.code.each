LAYOUT = File.open("../../data/2020/11.txt").each_line.map { |row| row.strip.split '' }

SLOPES = [-1, 0, 1].repeated_permutation(2).to_a - [[0, 0]]

ROWS = LAYOUT.size
COLS = LAYOUT[0].size
SEATS = (0...ROWS).to_a.product((0...COLS).to_a).reject { |r, c| LAYOUT[r][c] == ?. }

def in_layout? r, c
  (0...ROWS) === r && (0...COLS) === c
end

def count_occupied min_no_of_occupied, &look_for_seats
  layout = LAYOUT.clone.map &:clone
  next_layout = nil

  loop do
    next_layout = layout.clone.map &:clone

    SEATS.each do |r, c|
      seat = layout[r][c]
      no_of_occupied = look_for_seats.call(layout, r, c).count ?#

      if seat == ?L && no_of_occupied.zero?
        next_layout[r][c] = ?#
      elsif seat == ?# && no_of_occupied >= min_no_of_occupied
        next_layout[r][c] = ?L
      end
    end

    break if layout == next_layout

    layout.replace next_layout
  end

  layout.flatten.count ?#
end

occupied = count_occupied 4 do |layout, r, c|
  SLOPES
    .map { |dr, dc| [r + dr, c + dc] }
    .filter_map { |r, c| layout[r][c] if in_layout? r, c }
end

part_1 = occupied

puts part_1

occupied = count_occupied 5 do |layout, r, c|
  SLOPES.filter_map do |dr, dc|
    (1..)
      .lazy
      .map        { |n|    [r + n * dr, c + n * dc] }
      .take_while { |r, c| in_layout? r, c }
      .map        { |r, c| layout[r][c] }
      .find       { |s|    s =~ /L|#/ }
  end
end

part_2 = occupied

puts part_2
