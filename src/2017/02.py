import pathlib
from itertools import combinations

from utils import *

data = pathlib.Path("../../data/2017/02.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

spreadsheet = [ints(line) for line in lines]

part_1 = sum(max(row) - min(row) for row in spreadsheet)

print(part_1)

part_2 = 0

for row in spreadsheet:
    for combination in combinations(row, 2):
        div, mod = divmod(*sorted(combination, reverse=True))

        if mod == 0:
            part_2 += div
            break

print(part_2)
