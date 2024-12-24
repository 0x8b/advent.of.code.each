require 'set'

program = File.open("../../data/2020/08.txt").read.lines.map do |ins|
  op, arg = ins.scan(/(\w+) (-\d+|\+\d+)/).flatten

  [op, arg.to_i]
end.freeze


def run program
  accumulator = 0
  ip = 0
  seen = Set[]

  while ip < program.length do
    op, arg = program[ip]

    if seen.include? ip
      raise StandardError, accumulator
      break
    end

    seen.add(ip)

    case op
    when "acc"
      accumulator += arg
      ip += 1
    when "nop"
      ip += 1
    when "jmp"
      ip += arg
    end
  end

  accumulator
end

begin
  run program
rescue StandardError => acc
  part_1 = acc

  puts part_1
end

swap = { "nop" => "jmp", "jmp" => "nop" }

program.each_with_index do |instr, index|
  op = instr.first

  if swap.has_key? op
    program[index][0] = swap[op]
    begin
      accumulator = run program

      part_2 = accumulator

      puts part_2
    rescue StandardError => acc
    end
    program[index][0] = op
  end
end
