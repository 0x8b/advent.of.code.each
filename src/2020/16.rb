fields, your_ticket, nearby_tickets = File.open("../../data/2020/16.txt").read.split "\n\n"

fields = fields.lines.collect do |field|
  field.scan(/\d+/).map &:to_i
end.map do |frb, fre, srb, sre|
  [frb..fre, srb..sre]
end

your_ticket = your_ticket.lines[1].split(?,).map &:to_i

nearby_tickets = nearby_tickets.lines.drop(1).map { |line| line.split(?,).map &:to_i }

all_ranges = fields.flatten

error_rate = nearby_tickets.sum do |ticket|
  ticket.sum do |field_value|
    if all_ranges.any? do |range| range.include? field_value end
      0
    else
      field_value
    end
  end
end

part_1 = error_rate

puts part_1


valid_tickets = nearby_tickets.select do |ticket|
  ticket.all? do |field_value|
    all_ranges.any? do |range|
      range.include? field_value
    end
  end
end

all_matched_fields = valid_tickets.transpose.map do |column|
  fields.each_index.select do |i|
    column.all? do |value|
      fields[i].any? do |range|
        range === value
      end
    end
  end
end

correct_order = Array.new all_matched_fields.size

while j = all_matched_fields.each_index.find { |j| all_matched_fields[j].size == 1 } do
  correct_order[j] = all_matched_fields[j].first
  all_matched_fields = all_matched_fields.map { |s| s - all_matched_fields[j] }
end

d_fields_indices = correct_order.each_index.select do |i|
  (0..5).include? correct_order[i]
end

part_2 = your_ticket.values_at(*d_fields_indices).inject :*

puts part_2
