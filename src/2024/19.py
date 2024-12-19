import pathlib
from functools import cache

from utils import *

data = pathlib.Path("../../data/2024/19.txt").read_text(encoding="utf-8")
patterns, desired_designs = data.strip().split("\n\n")

patterns = tuple(pattern.strip() for pattern in patterns.split(", "))
desired_designs = [line.strip() for line in desired_designs.strip().split("\n")]


@cache
def count(pattern, patterns, design):
    if design == pattern:
        return 1

    if design.startswith(pattern):
        next_design = design[len(pattern) :]

        n = 0
        for next_pattern in patterns:
            if next_design.startswith(next_pattern):
                n += count(next_pattern, patterns, next_design)

        return n

    return 0


part_1 = 0
part_2 = 0

for design in desired_designs:
    if (n := count("", patterns, design)) > 0:
        part_1 += 1
        part_2 += n

print(part_1)
print(part_2)
