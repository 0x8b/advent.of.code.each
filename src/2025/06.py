import pathlib
import re
from functools import reduce

from utils import *

lines = pathlib.Path("../../data/2025/06.txt").read_text(encoding="utf-8").split("\n")


data = [line.split() for line in lines]

data = transpose(matrix(data, try_parse=True))

part_1 = 0

for a, b, c, d, op in data:
    if op == "+":
        part_1 += a + b + c + d

    elif op == "*":
        part_1 += a * b * c * d

print(part_1)

last_operator = None
nums = []

part_2 = 0

for i in range(len(lines[0]) + 1):
    try:
        op = lines[4][i]
    except:
        pass

    if op == "+" or op == "*":
        last_operator = op

    if i == len(lines[0]) or all(lines[j][i] == " " for j in range(5)):
        print(last_operator, nums)
        if last_operator == "*":
            part_2 += reduce(lambda x, y: x * y, nums)
        elif last_operator == "+":
            part_2 += sum(nums)

        nums = []

    else:
        nums.append(int("".join(lines[j][i] for j in range(4)).strip()))

print(part_2)
