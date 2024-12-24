numbers = File.open("../../data/2020/15.txt").read.split(",").map &:to_i

def number_on_nth_turn initial_numbers, nth
  counter = Hash.new { |h, k| h[k] = 0 }
  history = Hash.new { |h, k| h[k] = [] }

  lns = nil

  (1..nth).each do |turn|
    if turn <= initial_numbers.size
      lns = initial_numbers[turn - 1]
    else
      if history[lns].size < 2
        lns = 0
      else
        lns = history[lns].last(2).reverse.inject :-
      end
    end

    counter[lns] += 1
    history[lns].push turn
  end

  lns
end

part_1 = number_on_nth_turn numbers, 2020
part_2 = number_on_nth_turn numbers, 30000000

puts part_1
puts part_2
