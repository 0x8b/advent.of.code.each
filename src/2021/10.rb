LINES = ARGF.read.lines.map { |line| line.chomp.chars }

LBRACKETS = %w| ( [ { < |
RBRACKETS = %w| ) ] } > |

SYNTAX_ERROR_SCORE = RBRACKETS.zip([3, 57, 1197, 25137]).to_h
SYNTAX_ERROR_SCORE.default = 0

SCORE = RBRACKETS.zip([1, 2, 3, 4]).to_h

LEFT_TO_RIGHT = LBRACKETS.zip(RBRACKETS).to_h

def diagnose line
  stack = []

  line.each do |c|
    if LBRACKETS.include? c
      stack.push c
    else
      unless LEFT_TO_RIGHT[stack.pop] == c
        return { status: :corrupted, character: c }
      end
    end
  end

  return { status: :incomplete }
end

def is_corrupted? line
  diagnose(line)[:status] == :corrupted
end

def get_first_illegal_character corrupted_line
  diagnose(corrupted_line)[:character]
end

corrupted_lines = LINES.select { |line| is_corrupted? line }

syntax_error_scores = corrupted_lines.map { |line| get_first_illegal_character line }.map(&SYNTAX_ERROR_SCORE)

part_1 = syntax_error_scores.sum

puts part_1

def get_completion_of line
  completion = []
  stack = []

  until line.empty?
    c = line.pop

    if RBRACKETS.include? c
      stack.push c
    else
      if stack.empty?
        completion << LEFT_TO_RIGHT[c]
      else
        stack.pop
      end
    end
  end

  completion
end

incomplete_lines = LINES.reject { |line| is_corrupted? line }

completions = incomplete_lines.map do |line|
  get_completion_of line
end

scores = completions.map do |completion|
  completion.reduce(0) { |sum, character| 5 * sum + SCORE[character] }
end

middle_score = scores.sort.yield_self { |scores| scores[scores.size / 2] }

part_2 = middle_score

puts part_2
