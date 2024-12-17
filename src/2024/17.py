import pathlib
import itertools
import math
from utils import *

data = pathlib.Path("../../data/2024/17.txt").read_text(encoding="utf-8")

A, B, C, *program = ints(data)


def run(a, b, c, program):
    ip = 0
    output = []

    def combo(o):
        if 0 <= o <= 3:
            return o
        elif o == 4:
            return a
        elif o == 5:
            return b
        elif o == 6:
            return c
        else:
            raise ValueError(f"Invalid operand value: {o}")

    i = 0

    while True and i < 1_000_000:
        i += 1

        if ip + 1 > len(program) - 1:
            break

        match program[ip], program[ip + 1]:
            case 0, o:
                a = a // (2 ** combo(o))
                ip += 2

            case 1, o:
                b = b ^ o
                ip += 2

            case 2, o:
                b = combo(o) % 8
                ip += 2

            case 3, o:
                if a != 0:
                    ip = o
                else:
                    ip += 1
            case 4, o:
                b = b ^ c
                ip += 2

            case 5, o:
                output.append(combo(o) % 8)
                ip += 2

            case 6, o:
                b = a // (2 ** combo(o))
                ip += 2

            case 7, o:
                c = a // (2 ** combo(o))
                ip += 2

    return output


part_1 = ",".join(str(n) for n in run(A, B, C, program))

print(part_1)
