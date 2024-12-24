data = File.open("../../data/2020/19.txt").read.split "\n\n"

MESSAGES = data.last.lines.map &:strip

RULES = data.first.lines.map do |rule|
  symbol, expr = rule.split ?:

  expr = expr.strip.split.map do |term|
    if /\d+/ =~ term
      term.to_i
    elsif term == ?|
      term
    else
      term[1..-2]
    end
  end

  [symbol.to_i, expr]
end.to_h


def build_re symbol
  RULES[symbol].map do |term|
    if term.is_a? Integer
      ?( + build_re(term) + ?)
    else
      term
    end
  end.join
end

part_1 = MESSAGES.grep(/^#{build_re 0}$/).count

puts part_1



FINITE = (RULES.keys - [0, 8, 11])
  .map { |symbol| [symbol, build_re(symbol)] }
  .to_h

r42 = FINITE[42]
r11 = ("1".."10").map do |i| '((' + FINITE[42] + '){' + i + '}(' + FINITE[31] + '){' + i + '})' end.join('|')

part_2 = MESSAGES.grep(/^(#{r42})+(#{r11})$/).count # 422

puts part_2
