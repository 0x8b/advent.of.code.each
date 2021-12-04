NUMBERS, _, BOARDS = ARGF.read.partition "\n\n"

NUMBERS = NUMBERS.scan(/\d+/).map(&:to_i)
BOARDS = BOARDS.scan(/\d+/).map(&:to_i).each_slice(5).each_slice(5).to_a

catch :take_me_out do
  NUMBERS.size.times { |s|
    BOARDS.each { |board|
      board.chain(board.transpose).each { |rorc|
        if rorc - NUMBERS[0..s] == []
          p (board.flatten - NUMBERS[0..s]).sum * NUMBERS[s]
          throw :take_me_out
        end
      }
    }
  }
end

NUMBERS.size.times { |s|
  BOARDS.dup.each { |board|
    board.chain(board.transpose).each { |rorc|
      if rorc - NUMBERS[0..s] == []
        if BOARDS.size == 1
          p (board.flatten - NUMBERS[0..s]).sum * NUMBERS[s]
          exit
        else
          BOARDS.delete(board)
          break
        end
      end
    }
  }
}
