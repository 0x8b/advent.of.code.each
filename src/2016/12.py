import pathlib
from collections import defaultdict

from utils import *

data = pathlib.Path("../../data/2016/12.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


registers = defaultdict(int)

PART_2 = True
if PART_2:
    registers["c"] = 1


def is_register(operand):
    return operand.islower()


program = [line.strip().split() for line in lines]
ip = 0

while True:
    if ip >= len(program):
        break

    match program[ip]:
        case ["cpy", operand_1, operand_2]:
            registers[operand_2] = (
                registers[operand_1] if is_register(operand_1) else int(operand_1)
            )
            ip += 1

        case ["jnz", operand_1, operand_2]:
            value = registers[operand_1] if is_register(operand_1) else int(operand_1)

            if value != 0:
                ip += int(operand_2)
            else:
                ip += 1

        case ["dec", operand]:
            registers[operand] = registers[operand] - 1
            ip += 1

        case ["inc", operand]:
            registers[operand] = registers[operand] + 1
            ip += 1

answer = registers["a"]  # part_1, part_2

print(answer)
