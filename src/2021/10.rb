LINES = ARGF.read.lines.map { _1.chomp.chars }

SYNTAX_ERROR_SCORE = {
  ?) => 3,
  ?] => 57,
  ?} => 1197,
  ?> => 25137,
}

SYNTAX_ERROR_SCORE.default = 0

O2C = %w|[ ] ( ) { } < >|.each_slice(2).to_h

def find_first_illegal line
  stack = []

  for paren in line
    if O2C.keys.include? paren
      stack << paren
    else
      return paren if not O2C[stack.pop] == paren
    end
  end

  return
end

p LINES.map { find_first_illegal _1 }.map(&SYNTAX_ERROR_SCORE).sum # part 1

INCOMPLETE = LINES.reject { find_first_illegal _1 }

SCORE = {
  ?) => 1,
  ?] => 2,
  ?} => 3,
  ?> => 4,
}

MEDIAN = INCOMPLETE.map { |line|
  stack = []
  completion = []

  until line.empty?
    paren = line.pop

    if %w|) ] } >|.include? paren
      stack.push paren
    else
      if not stack.empty?
        stack.pop
      else
        completion << O2C[paren]
      end
    end
  end

  completion
}.map { |a| a.inject(0) { |s, paren| 5 * s + SCORE[paren] } }.sort.yield_self { _1[_1.size / 2] }

p MEDIAN # part 2
