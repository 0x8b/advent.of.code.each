import pathlib
from itertools import combinations
from functools import reduce

lines = (
    pathlib.Path("../../data/2020/01.txt")
    .read_text(encoding="utf-8")
    .strip()
    .split("\n")
)

entries = [int(entry) for entry in lines]

for r in [2, 3]:
    for combination in combinations(entries, r):
        if sum(combination) == 2020:
            print(reduce(lambda m, e: m * e, combination, 1))  # part_1, part_2
            break
