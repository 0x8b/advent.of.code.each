exprs = File.open("../../data/2020/18.txt").each_line.map do |expr|
  expr.strip.gsub(/\d+/) do |d|
    "Int.new(#{d})"
  end
end

class Int
  attr_accessor :value

  def initialize value
    self.value = value
  end

  def - rhs; Int.new(value * rhs.value); end
  def + rhs; Int.new(value + rhs.value); end
end

part_1 = exprs.sum { |expr| eval(expr.tr '*', '-').value }

puts part_1

class Int
  def + rhs; Int.new(value * rhs.value); end
  def * rhs; Int.new(value + rhs.value); end
end

part_2 = exprs.sum { |expr| eval(expr.tr '+*', '*+').value }

puts part_2