import pathlib
from itertools import combinations

from utils import *

data = pathlib.Path("../../data/2015/17.txt").read_text(encoding="utf-8")
containers = tuple(ints(data))


part_1 = 0
counter = []

for size in range(1, len(containers) + 1):
    count = 0

    for combination in combinations(containers, size):
        if sum(combination) == 150:
            part_1 += 1
            count += 1

    if count > 0:
        counter.append(count)

part_2 = counter.pop(0)

print(part_1)
print(part_2)
