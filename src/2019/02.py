import pathlib
from itertools import product

from utils import ints

data = pathlib.Path("../../data/2019/02.txt").read_text(encoding="utf-8")
program = ints(data.strip())
ip = 0

program[1] = 12
program[2] = 2

while True:
    if program[ip] == 1:
        program[program[ip + 3]] = program[program[ip + 1]] + program[program[ip + 2]]
        ip += 4
    elif program[ip] == 2:
        program[program[ip + 3]] = program[program[ip + 1]] * program[program[ip + 2]]
        ip += 4
    elif program[ip] == 99:
        break

part_1 = program[0]

print(part_1)

for noun, verb in product(range(100), range(100)):
    program = ints(data.strip())

    ip = 0

    program[1] = noun
    program[2] = verb

    while True:
        if program[ip] == 1:
            program[program[ip + 3]] = (
                program[program[ip + 1]] + program[program[ip + 2]]
            )
            ip += 4
        elif program[ip] == 2:
            program[program[ip + 3]] = (
                program[program[ip + 1]] * program[program[ip + 2]]
            )
            ip += 4
        elif program[ip] == 99:
            break

    if program[0] == 19690720:
        part_2 = 100 * noun + verb

        print(part_2)

        break
