exprs = File.open("../../data/2020/18.txt").each_line.map &:strip

def evaluate expr
  if /\(/ =~ expr
    match = /\([^\(]*?\)/.match expr

    slightly_reduced_expr = match.pre_match + evaluate(match[0][1..-2]).to_s + match.post_match

    evaluate slightly_reduced_expr
  elsif IS_PART_2 and /\+/ =~ expr
    match = /(\d+ \+ \d+)/.match expr
    lhs, _, rhs = match[0].split

    slightly_reduced_expr = match.pre_match + (lhs.to_i + rhs.to_i).to_s + match.post_match

    evaluate slightly_reduced_expr
  else
    tokens = expr.split.map { |d| /\d+/ =~ d ? d.to_i : d }
    result = tokens.shift

    while tokens.size > 0 do
      case tokens.shift 2
      in ?*, rhs
        result *= rhs
      in ?+, rhs
        result += rhs
      end
    end

    result
  end
end

IS_PART_2 = false
part_1 = exprs.sum { |expr| evaluate expr }

puts part_1

IS_PART_2 = true
part_2 = exprs.sum { |expr| evaluate expr }

puts part_2
