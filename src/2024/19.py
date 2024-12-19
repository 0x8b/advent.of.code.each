import pathlib
from functools import cache

from utils import *

data = pathlib.Path("../../data/2024/19.txt").read_text(encoding="utf-8")
patterns, desired_designs = data.strip().split("\n\n")

PATTERNS = tuple(pattern.strip() for pattern in patterns.split(", "))
DESIRED_DESIGNS = [line.strip() for line in desired_designs.strip().split("\n")]


@cache
def count(pattern, design):
    if pattern == design:
        return 1

    next_design = design[len(pattern) :]
    c = 0

    for next_pattern in PATTERNS:
        if next_design.startswith(next_pattern):
            c += count(next_pattern, next_design)

    return c


part_1, part_2 = 0, 0

for design in DESIRED_DESIGNS:
    c = count("", design)

    part_1 += int(c > 0)
    part_2 += c

print(part_1)
print(part_2)
