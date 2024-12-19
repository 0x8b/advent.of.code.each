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

    if not design.startswith(pattern):
        return 0

    if design.startswith(pattern):
        return sum(
            [
                count(next_pattern, patterns, design[len(pattern) :])
                for next_pattern in patterns
            ]
        )


part_1 = 0
part_2 = 0

for design in desired_designs:
    if (n := count("", patterns, design)) > 0:
        part_1 += 1
        part_2 += n

print(part_1)
print(part_2)
