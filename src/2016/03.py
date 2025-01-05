import itertools
import pathlib

from utils import *

data = pathlib.Path("../../data/2016/03.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

sides = [ints(line) for line in lines]

part_1 = 0
part_2 = 0

for a, b, c in sides:
    part_1 += int(a + b > c and a + c > b and b + c > a)


for column in transpose(sides):
    for a, b, c in itertools.batched(column, 3):
        part_2 += int(a + b > c and a + c > b and b + c > a)

print(part_1)
print(part_2)
