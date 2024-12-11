import pathlib
from collections import defaultdict

from utils import *

lines = (
    pathlib.Path("../../data/2023/04.txt")
    .read_text(encoding="utf-8")
    .strip()
    .split("\n")
)

data = [[ints(s) for s in line.replace(":", "|").split("|")] for line in lines]


part_1 = 0
part_2 = 0

instances = defaultdict(lambda: 1)

instances[1] = 1

for [card], winning_numbers, numbers in data:
    if intersection := set(winning_numbers) & set(numbers):
        part_1 += 2 ** (len(intersection) - 1)

        for i in range(len(intersection)):
            instances[card + i + 1] += instances[card]

print(part_1)

for [card], _, _ in data:
    part_2 += instances[card]

print(part_2)
