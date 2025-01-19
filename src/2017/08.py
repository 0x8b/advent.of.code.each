import operator
import pathlib
from collections import defaultdict

from utils import *

data = pathlib.Path("../../data/2017/08.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


operators = {
    "==": operator.eq,
    ">=": operator.ge,
    "<=": operator.le,
    "!=": operator.ne,
    "<": operator.lt,
    ">": operator.gt,
}

registers = defaultdict(int)

part_2 = 0

for line in lines:
    match line.strip().split():
        case [register, opcode, operand, "if", lhs, cmp_operator, rhs]:

            if operators[cmp_operator](registers[lhs], int(rhs)):
                registers[register] += (
                    int(operand) if opcode == "inc" else -1 * int(operand)
                )

                part_2 = max(part_2, registers[register])

part_1 = max(registers.values())

print(part_1)
print(part_2)
