import pathlib
from itertools import chain

from utils import *

data = pathlib.Path("../../data/2016/20.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

ranges = sorted(tuple(map(int, line.split("-"))) for line in lines)

actual_ranges = []

for c, d in ranges:
    if not actual_ranges:
        actual_ranges.append([c, d])
        continue

    match actual_ranges[-1]:
        case [a, b] if c <= b + 1:
            actual_ranges[-1][1] = max(b, d)
        case [a, b] if b + 1 < c:
            actual_ranges.append([c, d])
        case _:
            print(actual_ranges[-1], c, d)


part_1 = actual_ranges[0][1] + 1

print(part_1)

part_2 = 0

for r1, r2 in zip(actual_ranges, actual_ranges[1:]):
    part_2 += r2[0] - r1[1] - 1

print(part_2)
