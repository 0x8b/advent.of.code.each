import pathlib
from functools import cache

from utils import *

data = pathlib.Path("../../data/2024/19.txt").read_text(encoding="utf-8")
patterns, desired_designs = data.strip().split("\n\n")

patterns = tuple(pattern.strip() for pattern in patterns.split(", "))
desired_designs = [line.strip() for line in desired_designs.strip().split("\n")]


@cache
def count(pattern, patterns, design):
    if design == "":
        return 1

    if pattern != "" and not design.startswith(pattern):
        return 0

    return sum([count(p, patterns, design[len(pattern) :]) for p in patterns])


part_1 = 0
part_2 = 0

for i, design in enumerate(desired_designs, 1):
    if (n := count("", patterns, design)) > 0:
        part_1 += 1
        part_2 += n

print(part_1)
print(part_2)
